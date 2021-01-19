from tkinter import *


class Box(object):
    def __init__(self):
        self.testBoxX = 0
        self.testBoxY = 0
        self.heroImage = PhotoImage(file=r'hero-down.png')
        fullMap = PhotoImage(file=r'full-map.png')
        canvas.create_image(0, 0, image=fullMap, anchor="nw")
        canvas.image = fullMap

    def draw(self, canvas):
        canvas.create_image(self.testBoxX, self.testBoxY, image=self.heroImage, anchor="nw")


root = Tk()
canvas = Canvas(root, width=900, height=900)
# Wall positions list
wallPositions = [(0, 360), (90, 180), (90, 360), (90, 450), (90, 540), (90, 720)
    , (180, 180), (180, 360), (180, 720)
    , (270, 0), (270, 90), (270, 180), (270, 360), (270, 450), (270, 540), (270, 720), (270, 810)
    , (450, 90), (450, 180), (450, 270), (450, 360), (450, 540), (450, 630), (450, 810)
    , (540, 360), (540, 540), (540, 630), (540, 810)
    , (630, 90), (630, 180), (630, 360)
    , (720, 90), (720, 180), (720, 360), (720, 540), (720, 630), (720, 720)]
box = Box()


def up_key_pressed(e):
    box.testBoxY = box.testBoxY - 90
    if validMove():
        box.heroImage = PhotoImage(file=r'hero-up.png')
        box.draw(canvas)
    else:
        box.testBoxY = box.testBoxY + 90
        box.heroImage = PhotoImage(file=r'hero-up.png')
        box.draw(canvas)


def down_key_pressed(e):
    box.testBoxY = box.testBoxY + 90
    if validMove():
        box.heroImage = PhotoImage(file=r'hero-down.png')
        box.draw(canvas)
    else:
        box.testBoxY = box.testBoxY - 90
        box.heroImage = PhotoImage(file=r'hero-down.png')
        box.draw(canvas)


def left_key_pressed(e):
    box.testBoxX = box.testBoxX - 90
    if validMove():
        box.heroImage = PhotoImage(file=r'hero-left.png')
        box.draw(canvas)
    else:
        box.testBoxX = box.testBoxX + 90
        box.heroImage = PhotoImage(file=r'hero-left.png')
        box.draw(canvas)


def right_key_pressed(e):
    box.testBoxX = box.testBoxX + 90
    if validMove():
        box.heroImage = PhotoImage(file=r'hero-right.png')
        box.draw(canvas)
    else:
        box.testBoxX = box.testBoxX - 90
        box.heroImage = PhotoImage(file=r'hero-right.png')
        box.draw(canvas)


def validMove():
    print
    if box.testBoxX < 0 or box.testBoxX > 810 or box.testBoxY < 0 or box.testBoxY > 810:
        return False
    else:
        if (box.testBoxX, box.testBoxY) in wallPositions:
            return False
        else:
            return True


canvas.bind("<Up>", up_key_pressed)
canvas.bind("<Down>", down_key_pressed)
canvas.bind("<Right>", right_key_pressed)
canvas.bind("<Left>", left_key_pressed)

canvas.pack()
box.draw(canvas)
canvas.focus_set()
root.mainloop()

