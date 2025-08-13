from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkinter import PhotoImage

tasks = []
completed_tasks = []

window = Tk()
window.title("To-Do-List")
window.geometry("1000x800")
window.configure(bg="#fff3e6")
icon = PhotoImage(file="icone.png")
window.iconphoto(False, icon)

def add_task():
    if task_entry.get() != "":
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        full_task = f"{task_entry.get()} - {timestamp}"
        tasks.append(full_task)
        task_entry.delete(0, END)
        save_task_to_file()
        display_tasks()

def save_task_to_file():
    with open("tasks.txt","w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")

def save_completed_task_to_file():
    with open("completed_tasks.txt","w", encoding="utf-8") as file:
        for task in completed_tasks:
            file.write(f"{task}\n")


def load_from_file():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for l in f:
                cleaned_task = l.strip()
                if cleaned_task:
                    tasks.append(cleaned_task)
    except FileNotFoundError:
        pass

def load_completed_task_from_file():
    completed_tasks.clear()
    try:
        with open("completed_tasks.txt", "r", encoding="utf-8") as f:
            for l in f:
                cleaned_task = l.strip()
                if cleaned_task:
                    completed_tasks.append(cleaned_task)
    except FileNotFoundError:
        pass


def display_tasks():
    tasks_text.delete("1.0", END)
    for i, task in enumerate(tasks,1):
        tasks_text.insert(END, f"{i}. {task}\n")


def mark_as_donne():
    try:
        task_num = int(completed_task_entry.get())
        if 1 <= task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            completed_tasks.append(task)
            display_tasks()
            display_completed_tasks()
            completed_task_entry.delete(0, END)
            save_task_to_file()
            save_completed_task_to_file()
        else:
            messagebox.showerror("error", "invalid task number")
    except ValueError:
        messagebox.showerror("error", "please enter a valid number")

def display_completed_tasks():
    completed_tasks_text.delete("1.0", END)
    for i, task in enumerate(completed_tasks, 1):
        completed_tasks_text.insert(END, f"{i}. {task}\n")


def delete_task():
    try:
        task_num = int(task_number_entry.get())
        if 1 <= task_num <= len(tasks):
            del tasks[task_num-1]
            display_tasks()
            task_number_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Invalid task number")
    except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    save_task_to_file()


def clear_tasks():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
    if confirm:
        tasks.clear()
        display_tasks()
        save_task_to_file()

def clear_completed_tasks():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all completed tasks?")
    if confirm:
        completed_tasks.clear()
        display_completed_tasks()
        save_completed_task_to_file()



title_label = Label(window, text="To-Do-List", font="Helvetica 40 bold", pady=10, fg="#e67700", bg="#fff3e6")
title_label.place(x=350, y=3)

label1 = Label(window, text="enter a task: ", pady=10, font="Helvetica 14",  bg="#fff3e6")
label1.place(x=3, y=65)

task_entry = Entry(window, font="Arial 16")
task_entry.place(x=112, y=75, relwidth=0.9, width=-110)

add_task_button = Button(window, text="+", font="Helvetica 14", width=3, command=add_task, padx=5, bg="#ff8400", fg="white")
add_task_button.place(x=915, y=70)

scrollbar1 = Scrollbar(window)
scrollbar1.place(x=480, y=150, height=245)

scrollbar2 = Scrollbar(window)
scrollbar2.place(x=965, y=150, height=245)

tasks_text_title = Label(window, text=" Incomplete Tasks", pady=10, font="Helvetica 14",  bg="#fff3e6")
tasks_text_title.place(x=20, y=110)

tasks_text = Text(window, font="Arial 16", yscrollcommand=scrollbar1.set)
tasks_text.place(x=20, y=150, relwidth=0.47, width=-20, relheight=0.6, height=-180)


completed_tasks_text = Text(window, font="Arial 16", yscrollcommand=scrollbar2.set)
completed_tasks_text.place(x=510, y=150, relwidth=0.59, width=-150, relheight=0.56, height=-150)

completed_tasks_title = Label(window, text=" Completed Tasks ", pady=10, font="Helvetica 14",  bg="#fff3e6")
completed_tasks_title.place(x=500, y=105)

scrollbar1.config(command=tasks_text.yview)

scrollbar2.config(command=completed_tasks_text.yview)


label2 = Label(window, text="enter task number to delete: ", pady=10, font="Helvetica 14",  bg="#fff3e6")
label2.place(x=3, y=400)

task_number_entry = Entry(window,  font="Arial 16")
task_number_entry.place(x=250, y=410, relwidth=0.97, width=-250)

delete_button = Button(window, text="Delete task", font="Helvetica 14", width=12, height=1, command=delete_task, bg="#ff8400", fg="white")
delete_button.place(x=400, y=455)

label3 = Label(window, text="enter task number to mark as done: ", pady=10, font="Helvetica 14",  bg="#fff3e6")
label3.place(x=3, y=505)

completed_task_entry = Entry(window, font="Arial 16")
completed_task_entry.place(x=305, y=515, relwidth=0.97, width=-305)

mark_as_donne_button = Button(window, text="Mark as Done", font="Helvetica 14", width=12, height=1, bg="#ff8400", fg="white")
mark_as_donne_button.place(x=400, y=560)

mark_as_donne_button.config(command=mark_as_donne)

delete_tasks_button = Button(window, text="Delete All Tasks", font="Helvetica 14", width=15, height=1, bg="#ff8400", fg="white")
delete_tasks_button.place(x=200, y=620)

delete_tasks_button.config(command=clear_tasks)

delete_completed_tasks_button = Button(window, text="Delete Completed Tasks", font="Helvetica 14", width=20, height=1, bg="#ff8400", fg="white")
delete_completed_tasks_button.place(x=550, y=620)

delete_completed_tasks_button.config(command=clear_completed_tasks)

load_from_file()
display_tasks()

load_completed_task_from_file()
display_completed_tasks()

window.mainloop()