import tkinter as tk
from tkinter import messagebox
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
def clear_tasks():
    task_listbox.delete(0, tk.END)
root = tk.Tk()
root.title("To-Do List")
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
task_listbox.pack()
root.mainloop()
