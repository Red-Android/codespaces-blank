import sqlite3

DB_NAME = "hotel.db"  # This will be created automatically

def connect():
    return sqlite3.connect('hotel.db')

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
