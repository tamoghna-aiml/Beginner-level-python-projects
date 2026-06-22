from random import randint

lower_number: int = int(input(f"Enter the lowest possible number: "))
upper_number: int = int(input(f"Enter the highest possible number: "))
random_number: int = randint(lower_number, upper_number)
tries: int = int(input(f"Enter the number of tries: "))
print(f"Guess a number between {lower_number} and {upper_number}.")

count: int = 1
while True:
    try:
        user_guess: int = int(input(f"Guess({tries} tries remaining): "))
    except ValueError:
        print(f"Please enter a valid number!")
        continue

    if tries == 1:
        print(f"Sorry, You are out of tries!. Better luck next time!")
        break
    elif user_guess < random_number:
        print(f"{user_guess} is too low!")
        count += 1
        tries -= 1
    elif user_guess > random_number:
        print(f"{user_guess} is too high!")
        count += 1
        tries -= 1
    elif user_guess == random_number:
        print(f"You guessed the number!. {user_guess} is correct!. You took {count} tries!")
        break
