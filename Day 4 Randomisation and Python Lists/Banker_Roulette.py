#Who will pay the bill
import random

print("Welcome to the banker roulette")
name_string = input("Give me everyone name,separated by a comma")
name = name_string.split(",")

randomint = random.randint(0,len(name)-1)

print(f"{name[randomint]} will pay the bill")
