import sqlite3
import random
import threading
import time
import os
import yaml
from datetime import datetime
from termcolor import colored
import json

class LockWait:
    """Class to handle SQLite locking and waiting to reduce failures."""
    @staticmethod
    def execute_with_lock(cursor, query, params=None, max_retries=100, retry_delay=0.1):
        retries = 0
        while retries < max_retries:
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return True  # Success
            except sqlite3.OperationalError as e:
                if "locked" in str(e):
                    retries += 1
                    time.sleep(retry_delay)
                    print(colored(f"Database locked. Retrying ({retries}/{max_retries})...", "yellow"))
                else:
                    raise
        print(colored("Max retries reached. Query failed.", "red"))
        return False

# Function to create the database and insert 100 records
def mitigate_failures(db_name):
    """Enable settings to mitigate SQLite contention and failures."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Enable Write-Ahead Logging (WAL) for better concurrency
    cursor.execute("PRAGMA journal_mode=WAL;")

    # Increase the busy timeout to wait longer for database locks to clear
    cursor.execute("PRAGMA busy_timeout = 5000;")  # Wait up to 5000 ms

    conn.commit()
    conn.close()
    print("Failure mitigation applied: WAL mode enabled and busy timeout set.")


def create_database(db_name="test.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data INTEGER
        )
    """)
    conn.commit()

    # Insert 100 random records
    for i in range(1, 101):
        LockWait.execute_with_lock(cursor, "INSERT INTO test_table (data) VALUES (?)", (random.randint(1, 1000),))
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' ready with 100 records.")

# Function to simulate a write operation (insert or update)
def write_data_stress(db_name, errors, write_attempts, success_tracker):
    delay = random.uniform(0.1, 0.5) / 1000
    time.sleep(delay)

    max_retries = 100
    retries = 0

    while retries < max_retries:
        try:
            conn = sqlite3.connect(db_name, timeout=0.1)
            cursor = conn.cursor()
            try:
                # Randomly choose to insert or update
                if random.choice(["insert", "update"]) == "insert":
                    new_data = random.randint(1, 1000)
                    if LockWait.execute_with_lock(cursor, "INSERT INTO test_table (data) VALUES (?)", (new_data,)):
                        success_tracker["count"] += 1
                        print(colored("Write operation successful.", "green"))
                        return  # Exit the loop on success
                else:
                    random_id = random.randint(1, 100)
                    new_data = random.randint(1, 1000)
                    if LockWait.execute_with_lock(cursor, "UPDATE test_table SET data = ? WHERE id = ?", (new_data, random_id)):
                        success_tracker["count"] += 1
                        print(colored("Update operation successful.", "green"))
                        return  # Exit the loop on success
            except sqlite3.OperationalError as e:
                retries += 1
                wait_time = random.uniform(0.1, 2) / 1000  # Random delay between 0.1 ms and 2 ms
                time.sleep(wait_time)
                print(colored(f"Retrying due to error: {e} (Attempt {retries}/{max_retries})", "yellow"))
            finally:
                write_attempts.append({
                    "timestamp": datetime.now().isoformat(),
                    "threads": threading.active_count()
                })
        except Exception as e:
            errors.append({
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "active_threads": threading.active_count()
            })
            print(colored(f"Unexpected Error: {e}", "red"))
            break  # Exit the loop on unexpected errors
        finally:
            if 'conn' in locals():
                conn.close()

    # If max retries reached
    if retries == max_retries:
        errors.append({
            "timestamp": datetime.now().isoformat(),
            "error": "Max retries reached",
            "active_threads": threading.active_count()
        })
        print(colored("Max retries reached. Write failed.", "red"))

        # Save failed write to ./queue/{epoch}.json
        epoch_time = int(time.time())
        queue_dir = "./queue"
        os.makedirs(queue_dir, exist_ok=True)
        failed_write = {
            "timestamp": datetime.now().isoformat(),
            "retries": retries,
            "active_threads": threading.active_count()
        }
        with open(f"{queue_dir}/{epoch_time}.json", "w") as f:
            json.dump(failed_write, f, indent=4)

# Function to initiate stress testing with maximum threads
def stress_test(db_name="test.db"):
    success_tracker = {"count": 0}  # Initialize the success tracker
    max_threads = threading.active_count()
    threads = []
    errors = []
    write_attempts = []

    def worker():
        for _ in range(300):  # Stress test for 300 write attempts per thread
            write_data_stress(db_name, errors, write_attempts, success_tracker)

    # Launch maximum threads
    for _ in range(max_threads):
        t = threading.Thread(target=worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Generate YAML report
    report = {
        "errors": errors,
        "write_attempts": write_attempts,
        "total_errors": len(errors),
        "total_write_attempts": len(write_attempts),
    }

    with open("stress_test_report.yaml", "w") as f:
        yaml.dump(report, f)

    success_percentage = (success_tracker["count"] / len(write_attempts)) * 100 if write_attempts else 0
    failure_count = len(errors)
    failure_percentage = (failure_count / len(write_attempts)) * 100 if write_attempts else 0

    print(colored(f"Successes: {success_tracker['count']}", "green"))
    print(colored(f"Failures: {failure_count}", "red"))
    print(colored(f"Success Rate: {success_percentage:.2f}%", "green"))
    print(colored(f"Failure Rate: {failure_percentage:.2f}%", "red"))
    print("Stress test complete. Report saved to 'stress_test_report.yaml'.")

# Example usage
if __name__ == "__main__":
    create_database()
    mitigate_failures("test.db")
    stress_test()