from random import*

def play_number_guessing():
    secretNum = randint(1,100)
    print("\nI have selected a number between 1 and 100. Can you guess it?")
    print("You have 5 attempts to guess the number.")
    attempts = 5

    while attempts > 0:
        
        try:
            guessNum = int(input("\nYour Guess : "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if guessNum > secretNum :
            print(f"Too High.Try Again\nAttempts Left: {attempts-1}")
        elif guessNum < secretNum :
            print(f"Too Low.Try Again\nAttempts Left: {attempts-1}")
        else :
            print("\n(✿◠‿◠) Congratulations! You've guessed the number!\n") 
            break
        
        attempts -= 1

    if attempts == 0 :
        print(f"\nSorry, you've run out of attempts. The number was {secretNum}\n")

if __name__ == "__main__":
    play_number_guessing()