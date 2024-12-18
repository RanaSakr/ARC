import random

secret_number = random.randint(1, 20)
print("Guess the number between 1 and 20! You have 5 attempts.")
for attempt in range(1,6):
    try:
        guess = int(input(f"Attempt {attempt}: "))
        if guess < secret_number:
            print("Too low! Try again.")
            continue
        elif guess > secret_number:
            print("Too high! Try again.")
            continue
        else:
            print("Congratulations! You guessed it!")
            break
    except ValueError:
        print("Please enter a valid number.")
else:
    print(f"Game over! The secret number was {secret_number}.")

