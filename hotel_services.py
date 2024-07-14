import tkinter as tk
from tkinter import ttk

def show_info(service):
    info = {
        'Accommodation Services':'Room Types, Housekeeping,',
        'Dining Services':'Restaurants and Bars, Room Service',
        'Concierge Services':'Concierge Desk, Valet Parking',
        'Recreational Facilities':'Fitness Center, Swimming Pool and Spa',
        'Business and Event Services':'Meeting Rooms, Business Center',
        'Entertainment and Leisure Services':'Entertainment, Kids Club',
        'Additional Services':'Wi-Fi and Connectivity, Airport Shuttle, Pet-Friendly Services'
    }
    
    label.config(text=info.get(service, "Service not found"))
    
    
root = tk.Tk()
root.title('Hotel services')

# Create a label to display information
label = ttk.Label(root, text="Select a service to see its description.", wraplength=400, padding=10)
label.pack(pady=20)

# Create a dropdown menu
services = ["Accommodation Services", "Dining Services","Concierge Services",
            "Recreational Facilities","Business and Event Services",
            "Entertainment and Leisure Services", "Additional Services"]
combo = ttk.Combobox(root, values=services)
combo.set("Select the hotel service")
combo.pack(pady=10)

# Add a button to show information
button = ttk.Button(root, text="Show Info", command=lambda: show_info(combo.get()))
button.pack(pady=10)

# Run the application
root.mainloop()