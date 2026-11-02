# Create a number guessing game
import random
number = random.randint(1,100)
win = 0
print(number)
def gameplay():
    while True:
        guess = int(input('Enter your guess : '))
        if guess == number:
            print('You Win!!!')
            win = 1
            break
        elif guess > number:
            print('Your guess is greater then the number.')
        else:
            print('Your guess is smaller then the number.')

def replay():
    gameplay()
    while True:
        re_play = input('Do you want to play again? : ').capitalize()
        if re_play == 'Yes':
            gameplay()
        else:
            print('Thanks for playing.')
            break
replay()