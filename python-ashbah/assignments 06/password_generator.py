import random

print("Password Generator\n**********************")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()<>?:'

number = int(input("Amount of password generate: "))

length = int(input("Input your passwsord length: "))

print("\nhere are your passwords:")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
