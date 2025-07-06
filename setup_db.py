from db import execute_query

def setup_tables():
    execute_query("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        address TEXT
    );
    """)

    execute_query("""
    CREATE TABLE IF NOT EXISTS rooms (
        room_no INTEGER PRIMARY KEY,
        type TEXT,
        price REAL,
        is_available INTEGER DEFAULT 1
    );
    """)

    execute_query("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        room_no INTEGER,
        check_in TEXT,
        check_out TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id),
        FOREIGN KEY(room_no) REFERENCES rooms(room_no)
    );
    """)

    print("SQLite Database & Tables created successfully.")

# 🧷 Anchor point (bhool gaya tha, ab le bhai):
if __name__ == "__main__":
    setup_tables()
