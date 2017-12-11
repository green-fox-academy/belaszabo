class PostIt(object):
    def __init__(self, background_color, text, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color
    
idea = PostIt("orange", "Idea 1", "blue")
line = PostIt("pink", "Awesome", "black")
nice = PostIt("yellow", "Superb!", "green")

print(idea.text)
print(line.background_color)
print(nice.text_color)