# ======================================
# 🌸 Pink Calculator
# Автор: Ainazik
# Первый проект на Python + Tkinter
# ======================================
import tkinter as tk #подключает библиотеку tkinter и дает ей короткое имя tk 
root=tk.Tk()#создает главное окно программы
root.title("Pink calculator") #создаем название окна
root.geometry("450x550")
              #страиваем размер окна (350 пикселей в ширину и 500 в высоту)
BUTTON_BG = "#F8BBD0"
BUTTON_FG = "#C2185B"
BUTTON_ACTIVE = "#F48FB1"
root.configure(bg="#DF9AB1")
display = tk.Entry(
    root,
    font=("Arial",24),
    justify="right",
    bg="#FFF0F5",
    fg="#8E3257",
    insertbackground="black",

    relief="flat"
)

#данные две строки удалят все содержимое поля ввода
#root.mainloop() #запускает окно и позволяет пользователю взаимодействовать с ним. без этой строки окно сразу закроется
#теперь мы будем создавать кнопки
def calculate():
    print("Кнопка = нажата")
    try:
        expression = display.get()
        if expression =="":
            return
        result=eval(expression)
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")
def add_operation(operator):
    display.insert(tk.END, operator)
def add_number(number):
    display.insert(tk.END, number)
def clear_display():
    display.delete(0,tk.END)
def backspace():
    text=display.get()
    display.delete(0,tk.END)
    display.insert(0,text[:-1])
button1=tk.Button( 
    root,
    text="1", #на кнопке будет написано 1
    font=("Arial",20), #размер и шрифт текста
    width=5,# размер кнопки
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("1")
)
button1.grid(row=1,column=0,padx=5,pady=5)
 #показывает кнопку на экране
#row=1 - первая строка
#column=0 - первый столбец
#pady=5 - отступы между кнопками
button2=tk.Button(
    root,
    text="2",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda:add_number("2")
)
button2.grid(row=1,column=1,padx=5,pady=5)
button3=tk.Button(
    root,
    text="3",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("3")
)
button3.grid(row=1,column=2,padx=5,pady=5)
button4=tk.Button(
    root,
    text="4",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("4")
)
button4.grid(row=2,column=0,padx=5,pady=5)
button5=tk.Button(
    root,
    text="5",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("5")
)
button5.grid(row=2,column=1,padx=5,pady=5)
button6=tk.Button(
    root,
    text="6",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda : add_number("6")
)
button6.grid(row=2,column=2,padx=5,pady=5)

button7=tk.Button(
    root,
    text="7",
    font=("Arial", 20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("7")
)
button7.grid(row=3,column=0,padx=5,pady=5)

button8=tk.Button(
    root,
    text="8",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("8")
)
button8.grid(row=3,column=1,padx=5,pady=5)

button9=tk.Button(
    root,
    text="9",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("9")
)
button9.grid(row=3,column=2,padx=5,pady=5)

button0=tk.Button(
    root,
    text="0",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_number("0")
)
button0.grid(row=4,column=1,padx=5,pady=5)


button_clear=tk.Button(
    root,
    text="C",
    font=("Arial",20),
    width=5,
    height=2,
    bg="#E05684",
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=clear_display
)
button_clear.grid(row=4,column=0,padx=5,pady=5)
#теперь будем создавать кнопки со всеми действиями

button_plus=tk.Button(
    root,
    text="+",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_operation("+")
)
button_plus.grid(row=1,column=3,padx=5,pady=5)
button_minus=tk.Button(
    root,
    text="-",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command= lambda:add_operation("-")
)
button_minus.grid(row=2,column=3,padx=5,pady=5)
button_umnozh=tk.Button(
    root,
    text="*",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_operation("*")
)
button_umnozh.grid(row=3,column=3, padx=5,pady=5)

button_delit=tk.Button(
    root,
    text="/",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda: add_operation ("/")
)
button_delit.grid(row=4,column=2,padx=5,pady=5)

button_dot=tk.Button(
    root,
    text=".",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=lambda:add_number(".")
    
)
button_dot.grid(row=5,column=0,padx=5,pady=5)
button_equal=tk.Button(
    root,
    text="=",
    font=("Arial",20),
    width=5,
    height=2,
    bg="#E05684",
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=calculate
)
button_equal.grid(row=4,column=3,padx=5,pady=5)
root.configure(bg="#D29DB2")

button_back=tk.Button(
    root,
    text="⌫",
    font=("Arial",20),
    width=5,
    height=2,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=BUTTON_ACTIVE,
    activeforeground="white",
    relief="flat",
    command=backspace
)
button_back.grid(row=5, column=1, padx=5, pady=5)


display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=10,
    sticky="we"
)
root.bind("<Escape>", lambda event: clear_display())
root.bind("<Return>", lambda event: calculate())
root.mainloop()