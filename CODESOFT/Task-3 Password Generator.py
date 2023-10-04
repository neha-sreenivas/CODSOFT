import tkinter as tk
from tkinter import ttk
import random
import string
def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        result_label.config(text="Invalid length")
        return

    complexity = complexity_combobox.get()
    if complexity == "Easy":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text="Generated Password: " + password)
root = tk.Tk()
root.title("Password Generator")
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root)
complexity_label = ttk.Label(root, text="Password Complexity:")
complexity_combobox = ttk.Combobox(root, values=["Easy", "Medium", "Hard"])
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
result_label = ttk.Label(root, text="")

length_label.pack(pady=10)
length_entry.pack()
complexity_label.pack(pady=10)
complexity_combobox.pack()
generate_button.pack(pady=10)
result_label.pack()
root.mainloop()
