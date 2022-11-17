import random

l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
             'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '/', ']', '^']

numberLow_letter = int(input("How many lower letters would you like in your password?\n"))
numberUP_letter = int(input("how many upper letters would you like in your password\n"))
numbers_pass = int(input("how many number would you like in your password\n"))
symbols_pass = int(input("how many symbols would you like in your password\n"))

password_list = []

for char in (1, numberLow_letter + 1):
    password_list.append(random.choice(l_letters))

for char in (1, numberUP_letter + 1):
    password_list.append(random.choice(u_letters))

for char in range(1, numbers_pass + 1):
    password_list.append(random.choice(numbers))

for char in range(1, symbols_pass + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

randomPwd = "".join(password_list)
print(f"Your password is: {randomPwd}")


