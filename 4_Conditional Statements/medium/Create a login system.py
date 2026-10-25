# Create a login system
username = input('Enter UserName : ')
password = input('Enter Password : ')

credentials = 'admin', '1234'

if (username, password) == credentials:
    print('Login successful')
else:
    print('Login Failed')