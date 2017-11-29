watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival

# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival
granted = []

def security_check(queue):
    global security_alcohol_loot
    for i in range(0,len(queue)):
        if queue[i]['alcohol'] > 0:
            security_alcohol_loot += queue[i]['alcohol']
            queue[i]['alcohol'] = 0
        if queue[i]['guns'] > 0:
            watchlist.append(queue[i]['name'])
        else:
            granted.append(queue[i]['name'])
security_check(queue)
print(granted)
print(watchlist)