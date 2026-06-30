"""
25
Guess the number: 5
Too low
Guess the number: 50
Too high
Guess the number: 25
You guessed it in 3 attempts!
"""
import random #pseudorandom number

number = random.randint(1, 70) #including 1 and 70

attempts = 0
attempts_left = 5
hasWon = False

while attempts_left > 0:
    attempts_left -= 1 # attempts_left = attempts_left - 1
    attempts += 1      # attempts = attempts + 1
    guess = int(input("Guess the number: "))
    if guess == number:
        print("You guessed it correctly!")
        hasWon = True
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

    print(f"You have {attempts_left} attempts left.")

if hasWon:
    print(f"Congratulations! You guessed it in {attempts} attempt(s)!")
else:
    print(f"You ran out of attempts! The number was {number}. Better luck next time!")



    