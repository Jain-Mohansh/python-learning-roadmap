# Create a rock-paper-scissors game
import random

user = input('Enter the Choice (Rock, Paper and Scissors) : ')

computer = ['Rock', 'Paper', 'Scissors']
computer =  random.choice(computer)
wins = {'Rock':'Scissors', 'Paper' : 'Rock', 'Scissors' : 'Paper'}
match (user,computer):
    case _ if user == computer:
        print("It's a draw!!!")
