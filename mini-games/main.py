from hangman import play_hangman
from tictactoe import play_tictactoe
from number_guessing import play_number_guessing

print("\n=============Welcome To AMmOooR Games=============")

while True:
    print("\nOur Games")
    print("  1-HangMan")
    print("  2-Tic-Tac-Toe")
    print("  3-NumberGuessing")
    try:
        choice = int(input("Your choice >> "))
    except ValueError:
        print("[x] Invalid Input")
        continue

    match choice:
        case 1:
            print("\n---Welcome to Hangman Game---")
            play_hangman()
        case 2:
            print("\n---Welcome to Tic-Tac-Toe Game---")
            play_tictactoe()
        case 3:
            print("\n---Welcome to Number Guessing Game---")
            play_number_guessing()
        case _:
            print("[x] Wrong Choice! Please choose 1, 2, or 3.")
            continue

    while True :

        print("\nWhat Do You Want To Do?")
        print(" 1- Return To Main Menu")
        print(" 2- Exit")

        try:
            exit_choice = int(input(">> "))
            if exit_choice in range(1,3):
                break
            else:
                print("[!] Please enter 1 or 2.")
        except ValueError:
            print("[!] Invalid Input! Please enter a number.")

    if exit_choice == 2:
        break

print("\n(●'◡'●) Thanks For Your Time, Hope You Enjoyed AMmOooR Games!\n")