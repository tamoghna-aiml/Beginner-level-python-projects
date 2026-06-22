import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError

    rolls: list[int] = []
    for _ in range(amount):
        rolls.append(random.randint(1, 6))

    return rolls

def main():
    while True:
        try:
            print(f"How many dice would you like to roll?")
            user_input: str = input()

            if user_input.lower() == "exit":
                print(f"Thanks for playing. Goodbye!")
                break

            rolls: list[int] = roll_dice(int(user_input))
            print(*rolls, sep=", ")
            print(f"Total: "+ str(sum(rolls)))

        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()