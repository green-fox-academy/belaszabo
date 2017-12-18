from tkinter import *

class CanvasMap(object):
    def __init__(self):
        pass

class Tile(object):
    def __init__(self):
        pass

    def draw_floor_tile(self):
        root = Tk()
        canvas = Canvas(root, width = 720, height = 720)
        
        tile = PhotoImage(file = "floor.png")
        label = Label(root, image = tile)
        label.pack()

        root.mainloop()

image = Tile()
image.draw_floor_tile()

