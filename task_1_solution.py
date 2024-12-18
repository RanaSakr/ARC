import random

# Step 1: Generate a random secret number between 1 and 20
secret_number = random.randint(1, 20)

# Step 2: Allow the user 5 attempts to guess
print("Guess the number between 1 and 20! You have 5 attempts.")

for attempt in range(1, 6):  # 5 attempts (attempt = 1 to 5)
    # Get user's guess
    guess = int(input(f"Attempt {attempt}: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break  # Exit the loop since the guess is correct
    
    # If guess is too low
    if guess < secret_number:
        print("Too low! Try again.")
        continue  # Go to the next iteration
    
    # If guess is too high
    if guess > secret_number:
        print("Too high! Try again.")
        continue  # Go to the next iteration

# If user runs out of attempts
else:  # The 'else' block executes if the loop completes fully
    print(f"Game over! The secret number was {secret_number}.")
