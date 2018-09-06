import random


number = random.randint(0,100)
guess = int(input("Guess the number, from one to 100!: "))
guess = int(guess)
turns = 1


while guess != number:
    if guess > number:
        guess = int(input("too high, guess again!: "))
        turns = turns + 1
    elif guess < number:
        guess = int(input("too low, guess again!: "))
        turns = turns + 1

print("good job! the number was %s and you guessed it in %s tries!" %(number,turns))
