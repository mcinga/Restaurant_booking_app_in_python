# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:42:35 2024

@author: mcing
"""

import tkinter as tk
from tkinter import messagebox

def submit_reservation():
    # Retrieve the input values from the GUI
    date = date_entry.get()
    guests = guests_entry.get()
    special_requests = special_requests_entry.get('1.0', tk.END).strip()  # Using Text widget for multiline input
    
    # Validate the inputs
    try:
        d = str(int(date)) + " April 2024"  # Convert date to string and append month and year
        g = "Number of guests: " + str(int(guests))  # Convert guests to string and prepend label
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for date and guests.")
        return
    
    # Check for special requests
    if special_requests:
        details = (g, special_requests)
    else:
        details = g
    
    # Write the reservation details to the file
    with open("Reservation.txt", "a") as file:
        if isinstance(details, tuple):
            file.write(f"{d}: {details[0]}, Special requests: {details[1]}\n")
        else:
            file.write(f"{d}: {details}\n")
    
    # Show a confirmation message
    messagebox.showinfo("Success", "Thank you for booking with us, see you on " + d)
    
    # Clear the input fields for a new entry
    date_entry.delete(0, tk.END)
    guests_entry.delete(0, tk.END)
    special_requests_entry.delete('1.0', tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Ballito Restaurant Reservation System")

# Create and place the date label and entry field
date_label = tk.Label(root, text="Enter reservation date (day as number):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Create and place the guests label and entry field
guests_label = tk.Label(root, text="Number of guests:")
guests_label.pack()
guests_entry = tk.Entry(root)
guests_entry.pack()

# Create and place the special requests label and entry field
special_requests_label = tk.Label(root, text="Special requests (if any):")
special_requests_label.pack()
special_requests_entry = tk.Text(root, height=5, width=50)  # Using Text widget for multiline input
special_requests_entry.pack()

# Create a submit button that calls the submit_reservation function
submit_button = tk.Button(root, text="Submit Reservation", command=submit_reservation)
submit_button.pack()

# Start the Tkinter event loop
root.mainloop()
