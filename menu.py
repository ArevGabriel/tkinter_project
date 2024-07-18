import tkinter as tk 
from tkinter import ttk

class MenuItem:
    def __init__(self, name, price, category):
       self.name = name 
       self.price = price
       self.category = category
         
    def __str__(self):
        return f'{self.name} ({self.category}):{self.price:.2f}'
    
class Menu:
    def __init__(self):
        self.items=[]
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_name):
        self.items=[item for item in self.items if item.name!=item_name]
    
    def get_items(self):
        return self.items
    
class Restaurant:
    def __init__(self, name):
        self.name = name 
        self.menu = Menu()
    
    def add_menu_item(self, name, price, category):
        item = MenuItem(name, price, category)
        self.menu.add_item(item)
        
    def remove_menu_item(self, name):
        self.menu.remove_item(name)
        
    def get_menu(self):
        return self.menu.get_items()
    
class RestaurantApp:
    def __init__(self, root, restaurant):
        self.root = root
        self.restaurant = restaurant
        self.root.title(f'{restaurant.name} Menu')  
        
        self.setupui()
        
    def setupui(self):
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E,tk.N, tk.S))
        self.menu_list=tk.Listbox(self.frame, height = 10, width=50)
        self.menu_list.grid(row=0,column=0, columnspan=2, pady=10)
        
        self.name_label = ttk.Label(self.frame, text = 'Name:')
        self.name_label.grid(row = 1, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.frame, width=20)
        self.name_entry.grid(row=1, column= 1, sticky = tk.W)
        
        self.category_label = ttk.Label(self.frame, text = 'Category:')
        self.category_label.grid(row = 2, column=0, sticky=tk.W)
        self.category_entry = ttk.Entry(self.frame, width=20)
        self.category_entry.grid(row=2, column= 1, sticky = tk.W)
        
        self.price_label = ttk.Label(self.frame, text = 'Price:')
        self.price_label.grid(row = 3, column=0, sticky=tk.W)
        self.price_entry = ttk.Entry(self.frame, width=20)
        self.price_entry.grid(row=3, column= 1, sticky = tk.W)
        
        self.add_button = ttk.Button(self.frame, text = 'Add button',command=self.add_item)
        self.add_button.grid(row=4, column=1, pady=5)
        
        self.remove_button = ttk.Button(self.frame, text = 'Remove button',command=self.remove_item)
        self.remove_button.grid(row=4, column=2, pady=5)
        
        self.update_menu_list()
        
    def update_menu_list(self):
        self.menu_list.delete(0, tk.END)
        for item in self.restaurant.get_menu():
            self.menu_list.insert(tk.END, str(item))
            
    def add_item(self):
        name = self.name_entry.get()
        price = float(self.price_entry.get())
        category = self.category_entry.get()
        self.restaurant.add_menu_item(name, price, category)
        
        self.update_menu_list()
        
    def remove_item(self):
        selected_item = self.menu_list.get(tk.ACTIVE)
        item_name = selected_item.split(" (")[0]
        self.restaurant.remove_menu_item(item_name)
        self.update_menu_list()
        
restaurant=Restaurant("Delicious Bites")
restaurant.add_menu_item('Bruschetta ', 8.95, 'Main Course')
restaurant.add_menu_item('Caesar Salad', 9.50, 'Starter')
restaurant.add_menu_item('Grilled Salmon', 18.95, 'Main Course')
restaurant.add_menu_item('Filet Mignon', 27.95, 'Main Course')
restaurant.add_menu_item('Chocolate Lava Cake', 7.95, 'Dessert')
restaurant.add_menu_item('Tiramisu', 6.50, 'Dessert')
restaurant.add_menu_item('Soft Drinks', 2.50, 'Drink')
restaurant.add_menu_item('Wine Selection', 12.50, 'Drink')
    

root = tk.Tk()
app = RestaurantApp(root, restaurant)
root.mainloop()