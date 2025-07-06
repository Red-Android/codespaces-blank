import tkinter as tk
from tkinter import ttk, messagebox
import db
from db import execute_query, fetch_all

# --- Functions ---

def refresh_customers():
    for row in tree.get_children():
        tree.delete(row)
    rows = fetch_all("SELECT * FROM customers;")
    for row in rows:
        tree.insert("", "end", values=row)

def add_customer():
    name = name_var.get()
    phone = phone_var.get()
    address = address_var.get()

    if not name or not phone or not address:
        messagebox.showwarning("Missing Info", "Please fill all fields.")
        return

    success = execute_query(
        "INSERT INTO customers (name, phone, address) VALUES (?, ?, ?);",
        (name, phone, address)
    )

    if success:
        messagebox.showinfo("Success", "Customer added!")
        name_var.set("")
        phone_var.set("")
        address_var.set("")
        refresh_customers()
    else:
        messagebox.showerror("Error", "Failed to add customer.")

def delete_customer():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select", "Please select a customer to delete.")
        return

    item = tree.item(selected[0])
    customer_id = item["values"][0]

    confirm = messagebox.askyesno("Confirm", f"Delete customer ID {customer_id}?")
    if confirm:
        success = execute_query("DELETE FROM customers WHERE id = ?;", (customer_id,))
        if success:
            messagebox.showinfo("Deleted", "Customer deleted.")
            refresh_customers()
        else:
            messagebox.showerror("Error", "Failed to delete customer.")

# --- GUI Setup ---

root = tk.Tk()
root.title("Hotel Customer Management")
root.geometry("600x400")
root.resizable(False, False)

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill="x")

name_var = tk.StringVar()
phone_var = tk.StringVar()
address_var = tk.StringVar()

tk.Label(input_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(input_frame, textvariable=name_var).grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Phone").grid(row=0, column=2, padx=5, pady=5)
tk.Entry(input_frame, textvariable=phone_var).grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Address").grid(row=0, column=4, padx=5, pady=5)
tk.Entry(input_frame, textvariable=address_var).grid(row=0, column=5, padx=5)

tk.Button(input_frame, text="Add Customer", command=add_customer).grid(row=0, column=6, padx=10)

# Treeview (Table)
tree = ttk.Treeview(root, columns=("ID", "Name", "Phone", "Address"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.heading("Address", text="Address")
tree.column("ID", width=40)
tree.column("Name", width=150)
tree.column("Phone", width=100)
tree.column("Address", width=200)
tree.pack(padx=10, pady=10)

# Delete Button
tk.Button(root, text="Delete Selected Customer", command=delete_customer).pack(pady=5)

# Load Data Initially
refresh_customers()

root.mainloop()
