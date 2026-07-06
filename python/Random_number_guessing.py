import random
print("=====Number Guessing Game=====")
while True:
    number = random.randint(1, 100)
    chances=0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        chances += 1

        if guess == number:
            print("Congratulations! You guessed it right.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

    print("\n----- Result -----")
    print("Computer selected:", number)
    print("You selected:", guess)
    print("You guessed the number in", chances, "chances.")

    choice = input("\nDo you want to play again? (y/n): ")

    if choice == "n":
        print("Thanks for playing!")
        break