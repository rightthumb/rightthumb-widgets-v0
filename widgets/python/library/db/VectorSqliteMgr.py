import os
import re
import sys
import time
import json
import sqlite3
import threading
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union

# ------------------------------------------------------------
# Optional sqlite-vec
#   pip install sqlite-vec
# ------------------------------------------------------------
try:
    import sqlite_vec  # type: ignore
    _HAS_SQLITE_VEC = True
except Exception:
    sqlite_vec = None
    _HAS_SQLITE_VEC = False


# ------------------------------------------------------------
# FileLocker (no dependency on _v; uses env var or local folder)
# ------------------------------------------------------------
class FileLocker:
    @staticmethod
    def lockName(path: str) -> str:
        return re.sub(r"[^\w\-_\. ]", "_", path)

    @staticmethod
    def _base_dir() -> str:
        # You can set SQLITEMGR_LOCKS=/some/path if you want
        base = os.getenv("SQLITEMGR_LOCKS", "")
        if base.strip():
            return base
        # default: local .filelocks folder
        return os.path.join(os.getcwd(), ".filelocks")

    @staticmethod
    def lockPath(path: str) -> str:
        folder_path = FileLocker._base_dir()
        if not os.path.exists(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        return os.path.join(folder_path, FileLocker.lockName(path))

    @staticmethod
    def lock(path: str, timeout: float = 10.0) -> None:
        lock_path = FileLocker.lockPath(path)
        lock_file = lock_path + ".lock"
        start_time = time.time()
        while True:
            try:
                # Acquire lock by renaming (atomic on same filesystem)
                os.rename(lock_path, lock_file)
                return
            except FileNotFoundError:
                # If base lock file doesn't exist, create the .lock directly
                with open(lock_file, "w", encoding="utf-8") as f:
                    f.write("")
                return
            except OSError:
                if time.time() - start_time > timeout:
                    raise TimeoutError("Timeout waiting for lock")
                time.sleep(0.05)

    @staticmethod
    def unlock(path: str) -> None:
        lock_path = FileLocker.lockPath(path)
        lock_file = lock_path + ".lock"
        try:
            os.rename(lock_file, lock_path)
        except FileNotFoundError:
            pass

    @staticmethod
    def check(path: str) -> None:
        lock_path = FileLocker.lockPath(path)
        lock_file = lock_path + ".lock"
        while os.path.exists(lock_file):
            time.sleep(0.05)


# ------------------------------------------------------------
# sqliteMgr + sqlite-vec vector helpers
# ------------------------------------------------------------
EmbeddingLike = Union[str, List[float], Tuple[float, ...], "Any"]  # allow numpy arrays too


class sqliteMgr:
    def __init__(self, database: str, *, pragmas: bool = True):
        self.logs: List[str] = []
        self.database_name = database

        # Main connection used for normal single-thread ops
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        if pragmas:
            self._apply_pragmas(self.conn)

        self.structure = False
        self.table_structure: Dict[str, bool] = {}

        # Threaded buffers
        self.threadData: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        self.activeSuffix: Dict[str, str] = {}
        self.threadLock = threading.Lock()
        self.threadTimeoutSeconds: Dict[str, float] = {}

        # Load sqlite-vec (if available)
        self._vec_loaded = False
        self._try_load_vec(self.conn)

    # --------------------------
    # Basics
    # --------------------------
    def _apply_pragmas(self, conn: sqlite3.Connection) -> None:
        # Reasonable defaults for local apps (adjust if you want)
        try:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            conn.execute("PRAGMA temp_store=MEMORY;")
            conn.execute("PRAGMA foreign_keys=ON;")
        except Exception as e:
            self.logs.append(f"PRAGMA error: {type(e).__name__}: {e}")

    def _connect_thread(self) -> sqlite3.Connection:
        # New connection per worker thread (safer)
        c = sqlite3.connect(self.database_name)
        c.row_factory = sqlite3.Row
        self._apply_pragmas(c)
        self._try_load_vec(c)
        return c

    def _try_load_vec(self, conn: sqlite3.Connection) -> None:
        if self._vec_loaded:
            return
        if not _HAS_SQLITE_VEC:
            self.logs.append("sqlite-vec not installed; vector features disabled (pip install sqlite-vec).")
            return
        try:
            conn.enable_load_extension(True)
            sqlite_vec.load(conn)  # official loader
            conn.enable_load_extension(False)
            self._vec_loaded = True
            try:
                ver, = conn.execute("select vec_version()").fetchone()
                self.logs.append(f"sqlite-vec loaded: vec_version={ver}")
            except Exception:
                self.logs.append("sqlite-vec loaded.")
        except Exception as e:
            self.logs.append(f"Failed to load sqlite-vec: {type(e).__name__}: {e}")

    def safe_log_sql(self, sql: str, params: Optional[Sequence[Any]] = None) -> None:
        if params:
            param_str = ", ".join(repr(p) for p in params)
            self.logs.append(f"{sql} | PARAMS: {param_str}")
        else:
            self.logs.append(f"SQL: {sql}")

    def sql(self, sql: str, params: Optional[Sequence[Any]] = None, fetch: bool = False):
        self.logs.append("fn: sql")
        self.logs.append(f"Executing SQL: {sql}")
        if params:
            self.safe_log_sql(sql, params)
        try:
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            if fetch:
                columns = [desc[0] for desc in self.cursor.description]
                results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
                self.logs.append(f"Fetched {len(results)} rows")
                return results
            self.conn.commit()
            self.logs.append("SQL executed successfully.")
            return True
        except Exception as e:
            self.logs.append(f"Error executing SQL: {type(e).__name__}: {e}")
            return None

    # --------------------------
    # Table helpers (your originals, lightly tightened)
    # --------------------------
    def table_exists(self, table_name: str) -> bool:
        self.logs.append("fn: table_exists")
        sql = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?"
        self.logs.append(sql)
        self.cursor.execute(sql, (table_name,))
        return self.cursor.fetchone()[0] > 0

    def fields(self, table_name: str) -> List[str]:
        self.logs.append("fn: fields")
        try:
            sql = f'PRAGMA table_info("{table_name}")'
            self.logs.append(sql)
            self.cursor.execute(sql)
            return [row[1] for row in self.cursor.fetchall()]
        except Exception as e:
            self.logs.append(f"Error retrieving fields: {str(e)}")
            return []

    def get_type(self, val: Any) -> str:
        if isinstance(val, int):
            return "INTEGER"
        if isinstance(val, float):
            return "REAL"
        if isinstance(val, bool):
            return "BOOLEAN"
        if isinstance(val, (dict, list)):
            return "TEXT"
        return "TEXT"

    def createTable(self, table_name: str, records: Union[Dict[str, Any], List[Dict[str, Any]]]) -> None:
        self.logs.append("fn: createTable")
        fields: Dict[str, str] = {}

        if isinstance(records, dict):
            records = [records]

        for record in records:
            if isinstance(record, dict):
                for key, value in record.items():
                    fields[key] = self.get_type(value)

        if not fields:
            raise ValueError(f'No valid fields found to create table "{table_name}"')

        columns_sql = ", ".join(f'"{k}" {v}' for k, v in fields.items())
        sql = f'CREATE TABLE "{table_name}" ({columns_sql})'
        self.logs.append(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        self.logs.append(f"Table created: {table_name}")

    def ensure_columns_exist(self, table_name: str, records: List[Dict[str, Any]]) -> None:
        self.logs.append("fn: ensure_columns_exist")
        current_fields = set(self.fields(table_name))
        for record in records:
            for key, val in record.items():
                if key not in current_fields and key != "id":
                    try:
                        sql = f'ALTER TABLE {table_name} ADD COLUMN "{key}" {self.get_type(val)}'
                        self.logs.append(sql)
                        self.cursor.execute(sql)
                        self.conn.commit()
                        self.logs.append(f"Added column {key}")
                        current_fields.add(key)
                    except Exception as e:
                        self.logs.append(f"Error adding column {key}: {str(e)}")

    def structureMgr(self, table_name: str, records: List[Dict[str, Any]]) -> None:
        self.logs.append("fn: structureMgr")
        try:
            if not self.table_exists(table_name):
                self.createTable(table_name, records)
            self.ensure_columns_exist(table_name, records)
            self.table_structure[table_name] = True
        except Exception as e:
            self.logs.append(f"Error in structureMgr: {str(e)}")

    # --------------------------
    # CRUD
    # --------------------------
    def insert(self, table_name: str, records: Union[Dict[str, Any], List[Dict[str, Any]]]) -> None:
        self.logs.append("fn: insert")
        if not records:
            return

        if isinstance(records, dict):
            records = [records]
        if not isinstance(records, list):
            raise TypeError(f"records must be dict or list of dicts, got {type(records)}")

        if not self.table_exists(table_name):
            self.createTable(table_name, records)

        self.ensure_columns_exist(table_name, records)

        for record in records:
            columns = [f'"{col}"' for col in record.keys()]
            placeholders = ["?" for _ in record]
            sql = f'INSERT INTO {table_name} ({", ".join(columns)}) VALUES ({", ".join(placeholders)})'
            params = tuple(record.values())
            self.safe_log_sql(sql, params)
            try:
                self.cursor.execute(sql, params)
            except Exception as e:
                self.logs.append(f"Insert error: {str(e)}")
        self.conn.commit()

    def read(self, table_name: str, conditions: Dict[str, Any] = {}):
        self.logs.append("fn: read")
        if conditions and not self.structure:
            self.structureMgr(table_name, [conditions])

        where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ""
        select_sql = f"SELECT * FROM {table_name} {where_sql}"
        self.logs.append(select_sql)
        try:
            self.cursor.execute(select_sql, tuple(conditions.values()))
            columns = [desc[0] for desc in self.cursor.description]
            results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
            self.logs.append(f"Read {len(results)} records from table {table_name}")
            return results
        except Exception as e:
            self.logs.append(f"Error: {str(e)}")
            return []

    def delete(self, table_name: str, conditions: Dict[str, Any]) -> None:
        self.logs.append("fn: delete")
        where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ""
        delete_sql = f"DELETE FROM {table_name} {where_sql}"
        try:
            self.cursor.execute(delete_sql, tuple(conditions.values()))
            self.conn.commit()
            self.logs.append(f"Deleted {self.cursor.rowcount} records from {table_name}")
        except Exception as e:
            self.logs.append(f"Error deleting from {table_name}: {str(e)}")

    def update_or_insert(self, table_name: str, conditions: Dict[str, Any], record: Dict[str, Any]) -> None:
        self.logs.append("fn: update_or_insert")
        if not self.structure:
            self.structureMgr(table_name, [record, conditions])

        where_clause = " AND ".join(f'"{k}" = ?' for k in conditions.keys())
        set_clause = ", ".join(f'"{k}" = ?' for k in record.keys())

        select_sql = f"SELECT 1 FROM {table_name} WHERE {where_clause} LIMIT 1"
        self.safe_log_sql(select_sql, tuple(conditions.values()))

        self.cursor.execute(select_sql, tuple(conditions.values()))
        exists = self.cursor.fetchone()

        if exists:
            update_sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            params = tuple(record.values()) + tuple(conditions.values())
            self.safe_log_sql(update_sql, params)
            try:
                self.cursor.execute(update_sql, params)
                self.conn.commit()
                self.logs.append(f"Updated record in table {table_name}")
            except Exception as e:
                self.logs.append(f"Error updating: {str(e)}")
        else:
            self.insert(table_name, [{**conditions, **record}])
            self.logs.append(f"Inserted record into table {table_name}")

    # --------------------------
    # Streaming (kept)
    # --------------------------
    def streamGen(self, table_name: str, conditions: Dict[str, Any] = {}):
        self.logs.append("fn: streamGen")
        if conditions and not self.structure:
            self.structureMgr(table_name, [conditions])

        where_clauses = [f'"{key}" = ?' for key in conditions.keys()]
        where_sql = f'WHERE {" AND ".join(where_clauses)}' if where_clauses else ""
        select_sql = f"SELECT * FROM {table_name} {where_sql}"
        self.logs.append(select_sql)

        try:
            self.cursor.execute(select_sql, tuple(conditions.values()))
            columns = [desc[0] for desc in self.cursor.description]
            while True:
                row = self.cursor.fetchone()
                if row is None:
                    break
                yield dict(zip(columns, row))
        except Exception as e:
            self.logs.append(f"Error in streamGen: {str(e)}")

    # --------------------------
    # Threaded buffered inserts (safer)
    # --------------------------
    def initThreadedTable(self, table: str, timeout_seconds: float = 5.0) -> None:
        with self.threadLock:
            if table in self.threadData:
                return
            self.threadData[table] = {"a": [], "b": []}
            self.activeSuffix[table] = "a"
            self.threadTimeoutSeconds[table] = timeout_seconds

    def threadInsert(self, table: str, record: Dict[str, Any], timeout_seconds: float = 5.0) -> None:
        if table not in self.threadData:
            self.initThreadedTable(table, timeout_seconds)
        active = self.activeSuffix[table]
        with self.threadLock:
            self.threadData[table][active].append(record)

    def flushTable(self, table: str) -> None:
        with self.threadLock:
            active = self.activeSuffix[table]
            inactive = "b" if active == "a" else "a"
            self.activeSuffix[table] = inactive
            to_save = self.threadData[table][active]
            self.threadData[table][active] = []

        if to_save:
            threading.Thread(target=self.flushWorker, args=(table, to_save), daemon=True).start()

    def flushWorker(self, table: str, records: List[Dict[str, Any]]) -> None:
        lock_file = FileLocker.lockPath(table)
        FileLocker.lock(lock_file)
        try:
            # Separate connection for thread worker
            conn = self._connect_thread()
            cur = conn.cursor()

            # Ensure table + columns using this thread connection
            if not self._table_exists_conn(cur, table):
                self._create_table_conn(cur, conn, table, records)
            self._ensure_columns_conn(cur, conn, table, records)

            for record in records:
                cols = [f'"{c}"' for c in record.keys()]
                placeholders = ["?"] * len(record)
                insert_sql = f'INSERT INTO {table} ({", ".join(cols)}) VALUES ({", ".join(placeholders)})'
                cur.execute(insert_sql, tuple(record.values()))
            conn.commit()
            conn.close()
        except Exception as e:
            self.logs.append(f"FlushWorker error: {type(e).__name__}: {e}")
        finally:
            FileLocker.unlock(lock_file)

    def _table_exists_conn(self, cur: sqlite3.Cursor, table_name: str) -> bool:
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cur.fetchone()[0] > 0

    def _create_table_conn(self, cur: sqlite3.Cursor, conn: sqlite3.Connection, table_name: str, records: List[Dict[str, Any]]) -> None:
        fields: Dict[str, str] = {}
        for r in records:
            for k, v in r.items():
                fields[k] = self.get_type(v)
        if not fields:
            raise ValueError(f'No valid fields found to create table "{table_name}"')
        columns_sql = ", ".join(f'"{k}" {v}' for k, v in fields.items())
        sql = f'CREATE TABLE "{table_name}" ({columns_sql})'
        cur.execute(sql)
        conn.commit()

    def _ensure_columns_conn(self, cur: sqlite3.Cursor, conn: sqlite3.Connection, table_name: str, records: List[Dict[str, Any]]) -> None:
        cur.execute(f'PRAGMA table_info("{table_name}")')
        current = {row[1] for row in cur.fetchall()}
        for r in records:
            for k, v in r.items():
                if k not in current and k != "id":
                    sql = f'ALTER TABLE {table_name} ADD COLUMN "{k}" {self.get_type(v)}'
                    cur.execute(sql)
                    conn.commit()
                    current.add(k)

    # --------------------------
    # Vector helpers (sqlite-vec)
    # --------------------------
    def _require_vec(self) -> None:
        if not self._vec_loaded:
            raise RuntimeError("sqlite-vec not loaded. Install with: pip install sqlite-vec")

    def _to_vec_blob(self, embedding: EmbeddingLike):
        """
        sqlite-vec accepts:
          - JSON string '[...]'
          - compact float32 blob (recommended)
          - numpy float32 array (buffer protocol)
        We'll prefer blob when given list/tuple.
        """
        self._require_vec()

        # If user already passes JSON text
        if isinstance(embedding, str):
            return embedding

        # Numpy arrays can pass through (cast recommended)
        try:
            import numpy as np  # type: ignore

            if isinstance(embedding, np.ndarray):
                return embedding.astype(np.float32)
        except Exception:
            pass

        # List/tuple -> blob
        try:
            return sqlite_vec.serialize_float32(list(embedding))  # type: ignore
        except Exception:
            # last resort: JSON
            return json.dumps(list(embedding))

    def vecEnsure(
        self,
        prefix: str,
        dim: int = 1536,
        *,
        meta_columns_sql: str = 'content TEXT, meta TEXT'
    ) -> None:
        """
        Creates:
          - {prefix}_docs   (rowid = your id, metadata columns)
          - {prefix}_vec    (vec0 virtual table keyed by rowid)

        We keep vectors in vec0, and keep metadata in a regular table.
        Join on rowid for results.
        """
        self._require_vec()
        docs = f"{prefix}_docs"
        vec = f"{prefix}_vec"

        # docs table
        if not self.table_exists(docs):
            sql_docs = f'CREATE TABLE "{docs}" (id INTEGER PRIMARY KEY, {meta_columns_sql})'
            self.sql(sql_docs)

        # vec virtual table (vec0) — uses rowid as the key
        # Example syntax from sqlite-vec README:
        #   create virtual table vec_examples using vec0(sample_embedding float[8]);
        # :contentReference[oaicite:5]{index=5}
        if not self.table_exists(vec):
            sql_vec = f'CREATE VIRTUAL TABLE "{vec}" USING vec0(embedding float[{dim}]);'
            self.sql(sql_vec)

    def vecUpsert(
        self,
        prefix: str,
        id: int,
        embedding: EmbeddingLike,
        *,
        content: Optional[str] = None,
        meta: Optional[Union[dict, list, str]] = None,
        extra: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Upserts metadata into {prefix}_docs and vector into {prefix}_vec using rowid=id.
        """
        self._require_vec()
        docs = f"{prefix}_docs"
        vec = f"{prefix}_vec"

        # Ensure exists (safe no-op if already)
        if not self.table_exists(docs) or not self.table_exists(vec):
            self.vecEnsure(prefix)

        # docs upsert
        doc_rec: Dict[str, Any] = {}
        if content is not None:
            doc_rec["content"] = content
        if meta is not None:
            doc_rec["meta"] = meta if isinstance(meta, str) else json.dumps(meta)
        if extra:
            doc_rec.update(extra)

        if doc_rec:
            self.update_or_insert(docs, {"id": id}, doc_rec)

        # vec upsert: easiest is delete+insert for that rowid
        # (vec0 is a virtual table; UPDATE support can vary—this is reliable.)
        blob = self._to_vec_blob(embedding)
        self.sql(f'DELETE FROM "{vec}" WHERE rowid=?', (id,))
        self.sql(f'INSERT INTO "{vec}"(rowid, embedding) VALUES (?, ?)', (id, blob))

    def vecSearch(
        self,
        prefix: str,
        embedding: EmbeddingLike,
        *,
        k: int = 10,
        where_sql: str = "",
        where_params: Sequence[Any] = ()
    ) -> List[Dict[str, Any]]:
        """
        Returns joined results:
          id, distance, content, meta, ...

        KNN query pattern from sqlite-vec README uses:
          WHERE embedding MATCH ?
          ORDER BY distance
          LIMIT k
        :contentReference[oaicite:6]{index=6}
        """
        self._require_vec()
        docs = f"{prefix}_docs"
        vec = f"{prefix}_vec"

        blob = self._to_vec_blob(embedding)

        # Optional filtering on docs (where_sql should reference docs alias "d")
        where_clause = ""
        params: List[Any] = [blob]
        if where_sql.strip():
            where_clause = f" AND ({where_sql})"
            params.extend(list(where_params))

        params.append(k)

        sql = f"""
            SELECT
                v.rowid as id,
                v.distance as distance,
                d.*
            FROM "{vec}" v
            JOIN "{docs}" d ON d.id = v.rowid
            WHERE v.embedding MATCH ? {where_clause}
            ORDER BY v.distance
            LIMIT ?
        """.strip()

        return self.sql(sql, tuple(params), fetch=True) or []

    # --------------------------
    # Convenience aliases (kept)
    # --------------------------
    def ti(self, table: str, record: Dict[str, Any], timeout_seconds: float = 5.0):
        return self.threadInsert(table, record, timeout_seconds)

    def r(self, table_name: str, conditions: Dict[str, Any] = {}):
        return self.read(table_name, conditions)

    def get(self, table_name: str, conditions: Dict[str, Any] = {}):
        return self.read(table_name, conditions)

    def create(self, table_name: str, record: Dict[str, Any]):
        return self.insert(table_name, record)

    def c(self, table_name: str, record: Dict[str, Any]):
        return self.insert(table_name, record)

    def I(self, table_name: str, record: Dict[str, Any]):
        return self.insert(table_name, record)

    def ui(self, table_name: str, conditions: Dict[str, Any], record: Dict[str, Any]):
        return self.update_or_insert(table_name, conditions, record)

    def d(self, table_name: str, conditions: Dict[str, Any] = {}):
        return self.delete(table_name, conditions)

    def close(self) -> None:
        try:
            self.conn.close()
        finally:
            self.logs.append("Database closed.")
