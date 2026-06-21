# Class - 9

## Today's Topic
- Mini Project – Number guessing game

## Relevant Notes with code examples in English

### Mini Project: Number Guessing Game
In this game, the program selects a secret random number, and the player tries to guess it. The program gives feedback (too high, too low) for each guess until they guess correctly or run out of attempts.

```python
import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input("Take a guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")
        break
else:
    print(f"Game over! The secret number was {secret_number}.")
```
