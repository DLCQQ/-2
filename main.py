from tkinter import *

def move(event):
    key = event.keysym
    if key == "w":
        canvas.move(rect, 0, -10)
        canvas.move(shadow, 0, -10)
    elif key == "a":
        canvas.move(rect, -10, 0)
        canvas.move(shadow, -10, 0)
    elif key == "s":
        canvas.move(rect, 0, 10)
        canvas.move(shadow, 0, 10)
    elif key == "d":
        canvas.move(rect, 10, 0)
        canvas.move(shadow, 10, 0)

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

rect = canvas.create_rectangle(50, 50, 150, 150, fill='blue')
shadow = canvas.create_polygon(50, 150, 150, 150, 130, 170, 30, 170, fill='gray')

canvas.focus_set()
canvas.bind("<Key>", move)

root.mainloop()