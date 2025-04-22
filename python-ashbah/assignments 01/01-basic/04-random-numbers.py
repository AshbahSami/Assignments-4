import random

num_list = []

while len(num_list) < 10:
    number = random.randint(1, 99)
    num_list.append(number)
    print(number)
