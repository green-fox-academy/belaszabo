from tkinter import *

class CanvasMap(object):
    def __init__(self):
        pass

class Tile(object):
    def __init__(self):
        pass

    def draw_floor_tile(self, x, y):
        root = Tk()
        canvas = Canvas(root, width = 720, height = 720)
        canvas.pack()
        
        self.x = x
        self.y = y

        tile = PhotoImage(file = "floor.png")
        canvas.create_image(self.x, self.y, anchor = NW, image = tile)

        root.mainloop()

image = Tile()
image.draw_floor_tile(0, 0)

