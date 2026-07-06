import random
choice=['rock','paper','scissor']
while True:
    user=input("Enter your choice:")
    if user not in choice:
        print("Invalid choice!")
        continue
    computer=random.choice(choice)
    print("Computer chose:",computer)
    if user==computer:
        print("It's a Tie")
    elif(user=="rock" and computer=="scissor") or \
        (user=="paper" and computer=="rock") or \
        (user=="scissor" and computer=="paper"):
        print("You win!")
    else:
        print("Computer wins!")
    play_again=input("Do you want to play again? (y/n): ")
    if play_again=="n":
        print("Thanks for playing")
        break
    elif play_again !="y":
        print("Invalid input! Exiting the game.")
        break