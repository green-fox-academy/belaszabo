import random

range_start, range_end = input('Please enter the range of the guesses: ').split()
range_start, range_end = int(range_start), int(range_end)
lives = 5
number = random.randrange(range_start, range_end, 1)
first_guess = 'I have a number between '+str(range_start)+'-'+str(range_end)+'. You have 5 lives. What\'s your guess? '
guess = input(first_guess)
while int(guess) != number and lives > 0:
    if int(guess) > number:
        lives -= 1
        print ('Too high. You have '+str(lives)+' left.')
        guess = input()
    if int(guess) < number:
        lives -= 1
        print ('Too low. You have '+str(lives)+' left.')
        guess = input()
if lives == 0:
    print ('You lost, try again.')
else:
    print ('Congratulations. You won!')