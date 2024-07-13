import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    room_type = room_type_var.get()
    check_in = check_in_entry.get()
    check_out = check_out_entry.get()
    
    if not all([name, email, phone, room_type, check_in, check_out]):
        messagebox.showerror('Error','Registration failed')
        return
    
    with open('hotel_registration.txt','a') as file:
    
          file.write(f'{name},{email},{phone},{room_type},{check_in},{check_out}')
          
          messagebox.showinfo('Success','Registration successfully completed')
          clear_form()
          
#function to delete form
def clear_form():
    name_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    room_type_var.set('')
    check_in_entry.delete(0, tk.END)
    check_out_entry.delete(0, tk.END)
    
#Main app window

root = tk.Tk()
root.title('Registration form')

#Form 
tk.Label(root, text='Enter name:').grid(row=0, column=0,padx=10,pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10,pady=10)
    
    
tk.Label(root, text='Enter email:').grid(row=1, column=0,padx=10,pady=10)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10,pady=10)
 
tk.Label(root, text='Enter phone:').grid(row=2, column=0,padx=10,pady=10)
phone_entry = tk.Entry(root)
phone_entry.grid(row=2, column=1, padx=10,pady=10)  

tk.Label(root, text='Enter room type:').grid(row=3, column=0,padx=10,pady=10)
room_type_var = tk.StringVar()
tk.OptionMenu(root, room_type_var,  'Single', 'Double', 'Suite').grid(row=3, column=1, padx=10,pady=10)

tk.Label(root, text='Check in :').grid(row=4, column=0,padx=10,pady=10)
check_in_entry = tk.Entry(root)
check_in_entry.grid(row=4, column=1, padx=10,pady=10)

tk.Label(root, text='Check out: ').grid(row=5, column=0,padx=10,pady=10)
check_out_entry = tk.Entry(root)
check_out_entry.grid(row=5, column=1, padx=10,pady=10)

#Submit Button
submit_button=tk.Button(root, text='Submit',command=submit_form)
submit_button.grid(row=6 ,column=0, columnspan=2, pady= 20)

root.mainloop()

