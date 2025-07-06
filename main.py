# Ensures hotel.db is initialized with tables
import db
from db import execute_query, fetch_all

def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    success = execute_query(
        "INSERT INTO customers (name, phone, address) VALUES (?, ?, ?);",
        (name, phone, address)
    )

    if success:
        print("Customer added successfully!")
    else:
        print("Failed to add customer.")

def view_customers():
    customers = fetch_all("SELECT * FROM customers;")
    if customers:
        print("\n--- Customers ---")
        for cust in customers:
            print(f"ID: {cust[0]} | Name: {cust[1]} | Phone: {cust[2]} | Address: {cust[3]}")
    else:
        print("No customers found.")

def delete_customer():
    view_customers()
    customer_id = input("\nEnter the ID of the customer to delete: ")

    success = execute_query(
        "DELETE FROM customers WHERE id = ?;",
        (customer_id,)
    )

    if success:
        print("Customer deleted.")
    else:
        print("Failed to delete customer.")

def main():
    while True:
        print("\n=== Customer Menu ===")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
