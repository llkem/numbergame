import random


number = 3 #random.randint(0,100)
guess = int(input("Guess the number, from one to 100!: "))
turns = 1


while guess != int(number):
    if int(guess) > int(number):
        guess = input("too high, guess again!: ")
        turns = turns + 1
    elif int(guess) < int(number):
        guess = input("too low, guess again!: ")
        turns = turns + 1
    else:
        print("good job! the number was %s and you guessed it in %s tries!" %(number,turns))
