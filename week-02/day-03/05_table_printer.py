# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
    { "name": "vodka", "in_stock": 1, "needs_cooling": True },
    { "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
    { "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
    { "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
    { "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
    { "name": "sugar", "in_stock": 0, "needs_cooling": False },
    { "name": "lime juice", "in_stock": 0, "needs_cooling": True },
    { "name": "soda", "in_stock": 0, "needs_cooling": True }
]
def header():
    return "+--------------------+---------------+----------+\n| Ingredient         | Needs cooling | In stock |\n+--------------------+---------------+----------+"

def needs_cooling(i):
    if ingredients[i]["needs_cooling"] == True:
        return "Yes"
    else:
        return "No"

def in_stock(i):
    if ingredients[i]["in_stock"] != 0:
        return str(ingredients[i]["in_stock"])
    else:
        return "-"

def footer():
    return "+--------------------+---------------+----------+"

def table():
    for i in range(0, len(ingredients)):
        print("| " + ingredients[i]["name"] + " "*(19-len(ingredients[i]["name"])) + "| " + needs_cooling(i) + " "*(14-len(needs_cooling(i))) + "| " + in_stock(i) + " "*8 + "|")

print(header())
table()
print(footer())
