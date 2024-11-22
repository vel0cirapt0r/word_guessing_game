import random
from nltk.corpus import words


def word_guessing_game():
    print("Welcome to the Word Guessing Game!\nYou'll have to guess the secret word.")
    print("Let's get started!")

    # Ensure nltk's word list is loaded
    word_list = words.words()
    word = random.choice(word_list).lower()

    # Uncomment this for debugging or testing
    print(f"(DEBUG) The secret word is: {word}")

    print("Guess the characters!")
    guesses = ''
    turns = 2 * len(word)
    print(f"You have {turns} available wrong answers.")

    while turns > 0:
        failed = 0
        print("\nCurrent progress: ", end="")

        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n\nCongratulations! You guessed the word.")
            print(f"The word is: {word}")
            break

        print(f"\n\nYou have {turns} guesses remaining.")
        guess = input("Guess a character: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guesses:
                print("You already guessed that letter.")
            else:
                guesses += guess
                if guess not in word:
                    turns -= 1
                    print("Wrong guess!")
                    if turns == 0:
                        print(f"\nYou lose! The correct word was: {word}")
        else:
            print("Invalid input. Please enter a single alphabet character.")

    # Ask the user if they want to play again
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay in ['yes', 'y']:
        word_guessing_game()
    else:
        print("Thank you for playing! Goodbye.")


# Start the game
if __name__ == "__main__":
    import nltk
    nltk.download('words', quiet=True)
    word_guessing_game()