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
# размер на игралното поле в клетки
s_x = s_y = 9
# размер на стъпката между линиите, линиите ще са +1 на брой
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
# Коригираме размера на полето - за всякъв брой клетки
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y

# Добавяме област за командване на играта
menu_x = 250

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
canvas = Canvas(tk, width=size_canvas_x + menu_x, height=size_canvas_x, bd=0 ,highlightthickness=0)
# 1. На прозореца създаваме правоъгълник с бял цвят
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
# 2. Опаковаме канваса и обновяваме tk(tk - това е обектът, който описва нашата игра)
canvas.pack()
tk.update()

# Създаваме клетките на полето
def draw_table():
    for i in range(0, s_x + 1):
        # creates line from x1,y1 to x2,y2
        canvas.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(0, step_y * i, size_canvas_x, step_y * i)


def button_show_enemy():
    pass

def button_begin_again():
    pass

b0 = Button(tk, text="Покажи корабите на противника", command = button_show_enemy)
b0.place(x = size_canvas_x + 20, y = 30)

b1 = Button(tk, text="Започни отначало!", command = button_begin_again)
b1.place(x = size_canvas_x + 20, y = 70)

draw_table()

def add_to_all(event):
    _type = 0  # ЛБМ
    if event.num == 3:
        _type = 1  # ДБМ
    # print(_type)
    # за да получим координатите на мишката само по полето, а не глобално по екрана
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    # print(mouse_x, mouse_y)
    # преобразуваме в номер на клетка по х и у
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    print(ip_x, ip_y, "_type ", _type)

# Искаме да проследим натискането на бутон на мишката
canvas.bind_all("<Button-1>", add_to_all)  # Ляв бутон ЛБМ
canvas.bind_all("<Button-3>", add_to_all)  # Десен бутон ДБМ

# Създаваме цикъла на работa на играта
while app_running:
    tk.update_idletasks()
    tk.update()
    # Поставяме малко забавяне на играта тук
    time.sleep(0.005)



