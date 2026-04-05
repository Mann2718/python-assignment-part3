import requests
from datetime import datetime
import json

# --- TASK 4: ERROR LOGGER ---
def log_error(location, error_type, message):
    """Writes timestamped error entries to error_log.txt in append mode."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR in {location}: {error_type} — {message}\n"
    
    with open("error_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

# --- TASK 1: FILE I/O ---
def task_1_file_io():
    print("\n--- Running Task 1: File Operations ---")
    filename = "python_notes.txt"
    initial_notes = [
        "Topic 1: Variables store data. Python is dynamically typed.",
        "Topic 2: Lists are ordered and mutable.",
        "Topic 3: Dictionaries store key-value pairs.",
        "Topic 4: Loops automate repetitive tasks.",
        "Topic 5: Exception handling prevents crashes."
    ]

    # Write initial notes
    with open(filename, "w", encoding="utf-8") as f:
        for line in initial_notes:
            f.write(line + "\n")
    print("File written successfully.")

    # Append custom lines
    with open(filename, "a", encoding="utf-8") as f:
        f.write("Topic 6: File I/O is essential for data persistence.\n")
        f.write("Topic 7: API integration allows apps to communicate.\n")
    print("Lines appended.")

# --- TASK 2 & 3: API & EXCEPTION HANDLING ---
def task_2_and_3_logic():
    print("\n--- Running Task 2 & 3: API & Exceptions ---")
    url = "https://dummyjson.com/products?limit=20"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        products = response.json()['products']
        
        # Display Table
        print(f"{'ID':<3} | {'Title':<25} | {'Price':<8} | {'Rating'}")
        print("-" * 55)
        filtered = [p for p in products if p['rating'] >= 4.5]
        sorted_products = sorted(filtered, key=lambda x: x['price'], reverse=True)
        
        for p in sorted_products:
            print(f"{p['id']:<3} | {p['title'][:25]:<25} | ${p['price']:<7} | {p['rating']}")

    except requests.exceptions.RequestException as e:
        log_error("task_2_logic", type(e).__name__, str(e))
        print(f"API Error logged: {e}")

# --- TASK 4: TRIGGER LOGS ---
def task_4_triggers():
    print("\n--- Running Task 4: Logging Triggers ---")
    # Trigger 1: Connection Error
    try:
        requests.get("https://not-a-real-site-xyz-123.com", timeout=2)
    except Exception as e:
        log_error("fetch_products", "ConnectionError", "No connection could be made")

    # Trigger 2: HTTP 404
    res = requests.get("https://dummyjson.com/products/999")
    if res.status_code != 200:
        log_error("lookup_product", "HTTPError", f"{res.status_code} Not Found for product ID 999")

if __name__ == "__main__":
    task_1_file_io()
    task_2_and_3_logic()
    task_4_triggers()
    print("\nAll tasks completed. Check .txt files for output.")