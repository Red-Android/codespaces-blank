import sqlite3

DB_NAME = "hotel.db"  # SQLite DB file

def connect():
    return sqlite3.connect(DB_NAME)

def execute_query(query, values=()):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query, values)
        conn.commit()
        return True
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        conn.close()

def fetch_all(query, values=()):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute(query, values)
        return cursor.fetchall()
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        conn.close()

def table_exists(table_name):
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
    result = fetch_all(query, (table_name,))
    return len(result) > 0

def setup_tables():
    if not table_exists("customers"):
        execute_query("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            address TEXT
        );
        """)
        print("Table 'customers' created.")

    if not table_exists("rooms"):
        execute_query("""
        CREATE TABLE rooms (
            room_no INTEGER PRIMARY KEY,
            type TEXT,
            price REAL,
            is_available INTEGER DEFAULT 1
        );
        """)
        print("Table 'rooms' created.")

    if not table_exists("bookings"):
        execute_query("""
        CREATE TABLE bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            room_no INTEGER,
            check_in TEXT,
            check_out TEXT,
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(room_no) REFERENCES rooms(room_no)
        );
        """)
        print("Table 'bookings' created.")

    print("All necessary tables are ready.")

# Run table setup when db.py is imported/run
setup_tables()
