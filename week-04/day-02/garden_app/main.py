from tree import Tree
from flower import Flower 

class Garden(object):


    def __init__(self, flowers = None, trees = None):
        if flowers is None:
            self.flowers = []
        else:
            self.flowers = flowers
        if trees is None:
            self.trees = []
        else:
            self.trees = trees

    
    def garden_watering(self, water):
        flowers_need_water = []
        trees_need_water = []
        for i in self.flowers:
            if i.needs_water == True:
                flowers_need_water.append(i)
        for i in self.trees:
            if i.needs_water == True:
                trees_need_water.append(i)
        for i in trees_need_water:
            i.water += water / (len(trees_need_water) + len(flowers_need_water)) * 0.4
        for i in flowers_need_water:
            i.water += water / (len(trees_need_water) + len(flowers_need_water)) * 0.75
        print("Watering with", water)


    def add_flower(self, Flower):
        self.flowers.append(Flower)


    def add_tree(self, Tree):
        self.trees.append(Tree)

tree1 = Tree("blue")
tree2 = Tree("yellow")
flower1 = Flower("black")
flower2 = Flower("pink")
tree1.status()
tree2.status()
flower1.status()
flower2.status()

garden = Garden()

garden.add_flower(flower1)
garden.add_flower(flower2)
garden.add_tree(tree1)
garden.add_tree(tree2)

garden.garden_watering(40)

tree1.status()
tree2.status()
flower1.status()
flower2.status()

garden.garden_watering(70)

tree1.status()
tree2.status()
flower1.status()
flower2.status()
