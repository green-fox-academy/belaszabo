accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def bank(lists):
    for i in lists:
        print(i['client_name'], i['balance'])

bank(accounts)

def transfer(from_acc, to_acc, amount):
    a = 0
    for i in range(0,len(accounts)):
        if accounts[i]['account_number'] == from_acc:
            a += 1
            reg1 = i
        else:
            a += 0
        if accounts[i]['account_number'] == to_acc:
            a += 1
            reg2 = i
        else:
            a += 0
    if a != 2:
        print("404 - account not found")
    else:
        accounts[reg1]['balance'] -= amount
        accounts[reg2]['balance'] += amount
    
transfer(11234543, 43546731, 100)
print(accounts)