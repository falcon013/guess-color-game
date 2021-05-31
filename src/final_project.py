import os
import subprocess
import random
import time


def clear():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


def main():
    name = input("What is your name? ")
    print("Good Luck ! ", name)

    colors = ['green', 'yellow', 'red', 'white',
              'pink', 'violet', 'blue',
              'black', 'purple', 'gold']
    print(colors)

    time.sleep(5)
    clear()

    color = random.choice(colors)
    print("Guess the color")
    guesses = ''
    turns = 5

    while turns > 0:
        failed = 0
        for col in color:
            if col in guesses:
                print(col)
            else:
                print("_")
                failed += 1

        if failed == 0:
            print("You Win")
            print("The color is: ", color)
            break

        guess = input("guess a char in color: ")
        guesses += guess
        clear()

        if guess not in color:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
            clear()

            if turns == 0:
                print("You Loose")


if __name__ == '__main__':
    main()
