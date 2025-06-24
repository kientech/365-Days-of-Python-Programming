# 365 Days of Python Programming
# Author: KienTech


import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the path to the data file
DATA_FILE = "data.json"

# Function to load the shopping list from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save the shopping list to the JSON file
def save_data(items):
    with open(DATA_FILE, "w") as file:
        json.dump(items, file, indent=4)

# Function to refresh the listbox with the current shopping list
def refresh_listbox():
    listbox.delete(0, tk.END)
    for item in shopping_list:
        listbox.insert(tk.END, item)

# Function to add an item to the shopping list
def add_item():
    item = entry.get().strip()
    if item:
        shopping_list.append(item)
        save_data(shopping_list)
        refresh_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter an item.")

# Function to modify the selected item in the shopping list
def modify_item():
    selected_index = listbox.curselection()
    if selected_index:
        item = entry.get().strip()
        if item:
            shopping_list[selected_index[0]] = item
            save_data(shopping_list)
            refresh_listbox()
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a new value for the item.")
    else:
        messagebox.showwarning("Warning", "Please select an item to modify.")

# Function to delete the selected item from the shopping list
def delete_item():
    selected_index = listbox.curselection()
    if selected_index:
        shopping_list.pop(selected_index[0])
        save_data(shopping_list)
        refresh_listbox()
    else:
        messagebox.showwarning("Warning", "Please select an item to delete.")

# Load the existing shopping list from the data file
shopping_list = load_data()

# Initialize the Tkinter window
root = tk.Tk()
root.title("Shopping List Manager")

# Create the UI components
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create buttons for adding, modifying, and deleting items
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=0, padx=5)

modify_button = tk.Button(button_frame, text="Modify Item", command=modify_item)
modify_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Item", command=delete_item)
delete_button.grid(row=0, column=2, padx=5)

# Populate the listbox with the current shopping list
refresh_listbox()

# Run the application
root.mainloop()
