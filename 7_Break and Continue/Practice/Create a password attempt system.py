# Create a password attempt system
password = 'ABC'
attempts = 5
while True:
    Enter_pass = input('Enter the password : ')
    if Enter_pass == password:
        print('It was The correct password.')
        break
    else:
        attempts -= 1
        print(f'You have only {attempts} left.')

    if attempts == 0:
        print('Locking The program...' \
        "You can't enter the right password")
        break
