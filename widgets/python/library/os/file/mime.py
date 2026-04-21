import sqlite3
from pathlib import Path
from typing import List

def mime(
	db_path: str | Path,
	perceived_type: str,
	dot: bool = True
) -> List[str]:
	"""
	Return a list of extensions from ext_details where perceived_type matches.

	Args:
		db_path: Path to the SQLite database.
		perceived_type: Value of the 'perceived_type' column to filter by.
		dot: If True, keep the leading '.' on extensions.
			If False, strip it.

	Returns:
		List of extensions as strings.
	"""
	db_path = str(db_path)
	results: List[str] = []
	con = sqlite3.connect(db_path)
	try:
		cur = con.cursor()
		cur.execute(
			"SELECT extension FROM ext_details WHERE perceived_type = ?",
			(perceived_type,)
		)
		rows = cur.fetchall()
		for (ext,) in rows:
			if ext:
				ext = ext.strip()
				if not dot and ext.startswith("."):
					ext = ext[1:]
				results.append(ext)
	finally:
		con.close()
	return results