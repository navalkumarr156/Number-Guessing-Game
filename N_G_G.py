
import random

print("Guess the number!")
secret_num = random.randint(1, 100)
guess_num = None

while guess_num != secret_num:
    guess_num = int(input("Guess the number between 1 to 100: "))
    
    if guess_num < secret_num:
            print("Your guess is low. (Hint: Number is above) Try again!")
    elif guess_num > secret_num:
            print("Your guess is high. (Hint: Number is lower) Try again!")
    else:
        print(f"Correct! The number was {secret_num}.")
    