import tkinter as tk
from tkinter import messagebox

from constants import ROOM_COST_1_20,ROOM_COST_21_42,POOL_COST,GYM_COST

def calculate_cost(room_number, pool, gym):
    """Calculate the total cost based on room number and additional services."""
    if 1 <= room_number <= 20:
        room_cost = ROOM_COST_1_20
    elif 21 <= room_number <= 42:
        room_cost = ROOM_COST_21_42
    else:
        return 0  # Invalid room number

    total_cost = room_cost
    if pool:
        total_cost += POOL_COST
    if gym:
        total_cost += GYM_COST

    return total_cost

def book_room():
    """Handle the booking logic and display the total cost."""
    try:
        room_number = int(room_number_entry.get())
        pool = pool_var.get()
        gym = gym_var.get()

        # Calculate the cost
        total_cost = calculate_cost(room_number, pool, gym)

        # Display the result
        if total_cost > 0:
            messagebox.showinfo("Booking Confirmation", f"Total cost: ${total_cost:.2f}")
        else:
            messagebox.showwarning("Invalid Room Number", "Room number must be between 1 and 42.")
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid room number.")

# Create the main window
root = tk.Tk()
root.title("Hotel")

# Room Rate Description
description_text = (
    "Room Rates:\n"
    "Rooms 1-20: $85 per night\n"
    "Rooms 21-42: $95 per night\n\n"
    "Additional Costs:\n"
    "Pool: $22\n"
    "Gym: $22\n"
    "Three meals a day are free."
)
tk.Label(root, text=description_text, justify=tk.LEFT).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Room Number
tk.Label(root, text="Enter Room Number (1-42):").grid(row=1, column=0, padx=10, pady=10)
room_number_entry = tk.Entry(root)
room_number_entry.grid(row=1, column=1, padx=10, pady=10)

# Pool
pool_var = tk.BooleanVar()
tk.Checkbutton(root, text="Pool ($22)", variable=pool_var).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Gym
gym_var = tk.BooleanVar()
tk.Checkbutton(root, text="Gym ($22)", variable=gym_var).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Book Button
tk.Button(root, text="Book Now", command=book_room).grid(row=4, column=0, columnspan=2, padx=10, pady=20)

# Run the application
root.mainloop()