import sqlite3
import random
import threading
import time
import os
import yaml
from datetime import datetime
from termcolor import colored
import json

# Function to create the database and insert 100 records
def create_database(db_name="test.db"):
    if os.path.exists(db_name):
        print(f"Database '{db_name}' already exists. Skipping creation.")
        return

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table
    cursor.execute("""
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            data INTEGER
        )
    """)
    conn.commit()

    # Insert 100 random records
    for i in range(1, 101):
        cursor.execute("INSERT INTO test_table (id, data) VALUES (?, ?)", (i, random.randint(1, 1000)))
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created with 100 records.")

# Function to simulate a write operation (insert or update)
# Function to simulate a write operation (insert or update)
def write_data_stress(db_name, errors, write_attempts, success_tracker):
    delay = random.uniform(0.1, 0.5) / 1000
    time.sleep(delay)
    try:
        conn = sqlite3.connect(db_name, timeout=0.1)
        cursor = conn.cursor()
        try:
            # Randomly choose to insert or update
            if random.choice(["insert", "update"]) == "insert":
                new_id = random.randint(101, 200)
                new_data = random.randint(1, 1000)
                cursor.execute("INSERT INTO test_table (id, data) VALUES (?, ?)", (new_id, new_data))
            else:
                random_id = random.randint(1, 100)
                new_data = random.randint(1, 1000)
                cursor.execute("UPDATE test_table SET data = ? WHERE id = ?", (new_data, random_id))
            conn.commit()
            success_tracker["count"] += 1
            print(colored("Write operation successful.", "green"))
        except sqlite3.OperationalError as e:
            errors.append({
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "active_threads": threading.active_count()
            })
            print(colored(f"Error: {e}", "red"))
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

        # Save failed write to ./queue/{epoch}.json
        epoch_time = int(time.time())
        queue_dir = "./queue"
        os.makedirs(queue_dir, exist_ok=True)
        failed_write = {
            "timestamp": datetime.now().isoformat(),
            "error": str(e),
            "active_threads": threading.active_count()
        }
        with open(f"{queue_dir}/{epoch_time}.json", "w") as f:
            json.dump(failed_write, f, indent=4)
    finally:
        if 'conn' in locals():
            conn.close()

# Function to initiate stress testing with maximum threads
def stress_test(db_name="test.db"):
    success_tracker = {"count": 0}
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
    stress_test()
