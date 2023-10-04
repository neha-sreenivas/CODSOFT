import tkinter as tk
from tkinter import messagebox
contacts = []
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        clear_entries()
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone fields are required.")
def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['Name']} | {contact['Phone']}")

def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['Name'].lower() or query in contact['Phone']:
            contact_list.insert(tk.END, f"{contact['Name']} | {contact['Phone']}")
def update_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        if name and phone:
            contacts[index] = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            clear_entries()
            update_contact_list()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone fields are required.")
    else:
        messagebox.showerror("Error", "Select a contact to update.")

# Function to delete a contact
def delete_selected_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Select a contact to delete.")
def load_selected_contact(event):
    selected_index = contact_list.curselection()
    if selected_index:
        index = selected_index[0]
        contact = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["Name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["Phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["Email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["Address"])
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
window = tk.Tk()
window.title("Contact Management System")
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

phone_label = tk.Label(window, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

address_label = tk.Label(window, text="Address:")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack()

search_label = tk.Label(window, text="Search:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()
search_button = tk.Button(window, text="Search", command=search_contact)
search_button.pack()

update_button = tk.Button(window, text="Update Contact", command=update_selected_contact)
update_button.pack()

delete_button = tk.Button(window, text="Delete Contact", command=delete_selected_contact)
delete_button.pack()
contact_list = tk.Listbox(window, width=50, height=15)
contact_list.pack()
contact_list.bind("<<ListboxSelect>>", load_selected_contact)


update_contact_list()

window.mainloop()
