import tkinter as tk 
from tkinter import messagebox 
import json

##File to store inventory data

DATA_FILE = "inventory.json"

def load_inventory():
    try: 
        with open(DATA_FILE, "r") as file: 
            return json.load(file) 
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_inventory(data): 
    with open(DATA_FILE, "w") as file: 
        json.dump(data, file, indent=4)

class InventoryManager(tk.Tk): 
    def __init__(self): 
        super().__init__()
        self.title("Inventory Management System") 
        self.inventory = load_inventory()

# UI Components
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Product Name:").grid(row=0, column=0)
        self.product_name = tk.Entry(self)
        self.product_name.grid(row=0, column=1)

        tk.Label(self, text="Quantity:").grid(row=1, column=0)
        self.quantity = tk.Entry(self)
        self.quantity.grid(row=1, column=1)

        tk.Label(self, text="Price:").grid(row=2, column=0)
        self.price = tk.Entry(self)
        self.price.grid(row=2, column=1)

        tk.Button(self, text="Add Product", command=self.add_product).grid(row=3, column=0, columnspan=2)
        tk.Button(self, text="View Inventory", command=self.view_inventory).grid(row=4, column=0, columnspan=2)

    def add_product(self):
        name = self.product_name.get()
        quantity = self.quantity.get()
        price = self.price.get()
    
        if not name or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
            messagebox.showerror("Input Error", "Please enter valid product details")
            return
    
        quantity = int(quantity)
        price = float(price)

        self.inventory[name] = {"quantity": quantity, "price": price}
        save_inventory(self.inventory)
        messagebox.showinfo("Success", "Product added successfully")
        self.product_name.delete(0, tk.END)
        self.quantity.delete(0, tk.END)
        self.price.delete(0, tk.END)

    def view_inventory(self):
        inventory_str = "\n".join([f"{k}: {v['quantity']} units - ${v['price']} each" for k, v in self.inventory.items()])
        messagebox.showinfo("Inventory", inventory_str if inventory_str else "No products in inventory")

if __name__ == "__main__":
    
    app = InventoryManager()
    app.mainloop()