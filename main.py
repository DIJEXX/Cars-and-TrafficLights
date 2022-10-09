from tkinter import *
import time

tk = Tk()
tk.title("WannaCry Decrypt0r 1.0")          #Заголовок программы
tk.iconbitmap(r'Images\Malware.ico')        #Иконка программы
tk.geometry("640x480")
bg = PhotoImage(file="Images\Road.png")     #Фон
canvas = Canvas(tk, width=640, height=480)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

Car1_obj = PhotoImage(file="Images\Car1.png")
id_img = canvas.create_image(0, 210, anchor=NW, image=Car1_obj)
Car2_obj = PhotoImage(file="Images\Car2.png")
id_img = canvas.create_image(00, 230, anchor=NW, image=Car2_obj)
Rocket_obj = PhotoImage(file="Images\Rocket.png")
id_img = canvas.create_image(0, 300, anchor=NW, image=Rocket_obj)
TrafficLights_obj = PhotoImage(file="Images\Green.png")
id_img = canvas.create_image(600, 140, anchor=NW, image=TrafficLights_obj)

for i in range(1, 640):
    canvas.move(2, 4, 0)            #Айди объекта canvas, скорость перемещения X, Y
    canvas.move(3, 2, 0)
    canvas.move(4, 8, 0)
    tk.update()
    time.sleep(0.0001)                #Частота обновления для плавности

tk.mainloop()
