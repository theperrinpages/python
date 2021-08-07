# This is a python script on guessing from a range of 0 to 9
import random
from time import sleep
import os

magic_number = random.randint(0, 9)
sleep(0.3)
print("You will have 3 chance to make the correct guess!\n ")


def user_in():
    sleep(0.6)
    x: int = int(input("Enter a number from 0 to 9 > "))
    return x


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


for a in range(3):
    if user_in() != magic_number:
        if a == 2:
            clear()
            sleep(0.7)
            print("\n\tYou have used all of your chances!\nGood luck next time!")
            break
        else:
            clear()
            sleep(0.5)
            print("You failed!", len(range(3)) - 1 - a, "tries left")
        continue

    else:
        clear()
        sleep(0.9)
        print("Success! Wohoo! :)")
        break

print(f"The computer generated random number was {magic_number}")
