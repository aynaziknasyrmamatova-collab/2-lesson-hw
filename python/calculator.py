import tkinter as tk #подключает библиотеку tkinter и дает ей короткое имя tk 
root=tk.Tk()#создает главное окно программы
root.title("My calculator") #создаем название окна
root.geometry("400x600") #настраиваем размер окна (350 пикселей в ширину и 500 в высоту)
display=tk.Entry(
    root,
    font=("Arial",24),#здесь мы пишем как текст будет выравниваться, какой шрифт
    justify="right"
)
display.pack(fill="x", padx=10,pady=10)
#root.mainloop() #запускает окно и позволяет пользователю взаимодействовать с ним. без этой строки окно сразу закроется
#теперь мы будем создавать кнопки
button1=tk.Button( 
    root,
    text="1", #на кнопке будет написано 1
    font=("Arial",20), #размер и шрифт текста
    width=5,# размер кнопки
    height=2
)
button1.pack(pady=10) #показывает кнопку на экране
root.mainloop()