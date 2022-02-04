from tkinter import *
# За да имаме изскачащ прозорец с въпроса искаме ли да затворим приложението
from tkinter import messagebox
import time

# Създаваме нов обект от тип Tk
tk = Tk()
# Дали приложението ни е стартирано или не
app_running = True

# Създаваме прозореца на нашето приложение:
# 1. Задаваме размерите му
size_canvas_x = 600
size_canvas_y = 600

def on_closing():
    # Тук ще променяме app_running, затова ще кажем че тя е глобална
    # ако не е глобална - промяната и ще се вижда само вътре в тази функция!
    global  app_running
    if messagebox.askokcancel("Изход от играта", "Искате ли да излезетеот играта?"):
        app_running = False
        tk.destroy()

# 2. В момента на затварянето на прозореца на нашето tk - ще стартира функцията on_closing
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Игра Морска Битка")

# 3. Забраняваме преоразмеряването на прозореца
tk.resizable(0, 0)

# 4. Задаваме атрибут - прозорецът на нашата игра да е винаги най-отгоре
tk.wm_attributes("-topmost", 1)

# Вече можем да създадем прозореца(canvas) на играта:
canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_x, bd=0 ,highlightthickness=0)
# 1. На прозореца създаваме правоъгълник с бял цвят
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
# 2. Опаковаме канваса и обновяваме tk(tk - това е обектът, който описва нашата игра)
canvas.pack()
tk.update()


# Създаваме цикъла на работa на играта
while app_running:
    tk.update_idletasks()
    tk.update()
    # Поставяме малко забавяне на играта тук
    time.sleep(0.005)



