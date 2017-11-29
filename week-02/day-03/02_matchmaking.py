girls = ["Eve", "Ashley", "Bözsi", "Kat", "Jane"]
boys = ["Joe", "Fred", "Béla", "Todd", "Neef", "Jeff"]
order = []
for i in range(0,len(girls)):
    order.append(girls[i])
    order.append(boys[i])
if len(boys) > len(girls):
    order.append(boys[-1])
print(order)