import tkinter as tk
root=tk.Tk()
root.title("Your daily planner")
root.geometry("500x600")
root.configure(bg="#150B3C")
title=tk.Label(
    root,
    text="To do list",
    font=("Times New Roman",24),
    bg="#150B3C",
    fg="#FFFBF7"
)
title.pack(pady=20)
task_entry=tk.Entry(
    root,
    font=("Times New Roman",18),
    width=25,
    bg="#FFF0F5",
    fg="#111048"
)
task_entry.pack(pady=10)
task_list=tk.Listbox(
    root,
    font=("Times New Roman",16),
    width=30,
    height=10,
    bg="#FFF0F5",
    fg="#111048"
)
task_list.pack(pady=20)
def add_task():
    task=task_entry.get().strip()
    if task=="":
        return
    task_list.insert(tk.END,task)
    task_entry.delete(0,tk.END)
def delete_task():
    selected_task=task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)
def complete_task():
    selected_task=task_list.curselection()
    if selected_task:
        task=task_list.get(selected_task)
        task_list.delete(selected_task)
        task_list.insert(selected_task, "✅ " + task)
def save_task():
    tasks=task_list.get(0,tk.END)
    with open("task.txt","w", encoding="utf-8",) as file:
        for task in tasks:
            file.write(task +"\n")
def load_task():
    try:
        with open("task_txt","r",encoding="utf-8")as file:
            tasks=file.readlines()
            for task in tasks:
                task=task.strip()
                task_list.insert(tk.END,task)
    except FileNotFoundError:
        pass
def clear_all():
    task_list.delete(0,tk.END)
button_frame=tk.Frame(
    root,
    bg="#150B3C"
)
button_frame.pack(pady=10)
add_button=tk.Button(
    button_frame,
    text="Add the task",
    font=("Times New Roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=add_task
)
add_button.grid(row=0,column=1,padx=5,pady=5)
delete_button=tk.Button(
    button_frame,
    text="Delete the task",
    font=("Times New roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=delete_task
)
delete_button.grid(row=1,column=0,padx=5,pady=5)
complete_button=tk.Button(
    button_frame,
    text="Mark as a completed task",
    font=("Times New Roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=complete_task
)
complete_button.grid(row=0,column=0,padx=5,pady=5)
save_button=tk.Button(
   button_frame,
    text="Save",
    font=("Times New Roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=save_task
)
save_button.grid(row=0,column=3,padx=5,pady=5)
load_button=tk.Button(
    button_frame,
    text='Load the task',
    font=("Times New Roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=load_task
)
load_button.grid(row=1,column=1,padx=5,pady=5)
clear_button=tk.Button(
    button_frame,
    text="Clear all tasks",
    font=("Times New Roman",16),
    bg="#FFF0F5",
    fg="#100F51",
    command=clear_all
)
clear_button.grid(row=2,column=0,padx=5,pady=5)

root.bind("<Return>",lambda event: add_task())
task_list.bind("<Double-Button-1>", lambda event:complete_task())
root.resizable(False,False)
root.mainloop()