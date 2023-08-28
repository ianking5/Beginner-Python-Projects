import random

print("Your random password is:")

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
password = ''
for x in range(10):
    password += random.choice(chars)

print(password)