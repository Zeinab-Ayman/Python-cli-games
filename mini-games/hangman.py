from random import *

def draw_hangman(wrong_attempts):
    print("\n")
    print("  +---+")
    print("  |   |")
    print(f"  { 'O' if wrong_attempts >= 1 else ' ' }   |")
    print(
        f" { '/' if wrong_attempts >= 3 else ' ' }"
        f"{ '|' if wrong_attempts >= 2 else ' ' }"
        f"{ '\\' if wrong_attempts >= 4 else ' ' }  |"
    )
    print(
        f" { '/' if wrong_attempts >= 5 else ' ' } "
        f"{ '\\' if wrong_attempts >= 6 else ' ' }  |"
    )
    print("  =========")
    print("\n")


def play_hangman():
    wordBank = [
        "computer", "engineering", "programming", "hardware", "software",
        "embedded", "systems", "pointer", "compiler", "variable",
        "function", "algorithm", "database", "network", "robotics",
        "circuit", "controller", "memory", "processor", "automation"
    ]

    secretWord = choice(wordBank)
    guessedWord = ["_"]*len(secretWord)
    maxTries = 6
    wrongattempts = 0
    guessedLetters = set()

    while maxTries > 0 :
        
        draw_hangman(wrongattempts)
        print("Word: ", guessedWord)
        print(f"Remaining Tries: {maxTries}")

        if "_" not in guessedWord:
            print("\n(✿◠‿◠) Congratulations! You guessed the word correctly!\n")
            return
        
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter (a-z).")
            continue

        if guess in guessedLetters:
            print("You already guessed that letter!")
            continue
        
        guessedLetters.add(guess)

        if guess in secretWord:
            print(f"\nGood job! '{guess}' is in the word.")
            for i, letter in enumerate(secretWord):
                if letter == guess:
                    guessedWord[i] = guess
        else:
            print(f"\nWrong! '{guess}' is not in the word.")
            wrongattempts  += 1
            maxTries -= 1

    draw_hangman(wrongattempts)
    print(f"Game Over! The word was: {secretWord}\n")


if __name__ == "__main__":
    play_hangman()