import random
from faker import Faker

print("Welcome to my word Guessing Game!\nYou'll have to guess the secret word")
print("Let's get started!")

fake = Faker()

word = fake.word()

# print(word)

print("Guess the characters")

guesses = ''
turns = 2 * len(word)
print(f"you have {turns} available wrong answers")

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    if guess.isalpha() and len(guess) == 1:
        guesses += guess

        if guess not in word:

            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print(f"You Loose the correct answer is {word}")
    else:
        print("your guess should be only 'alphabet' letters and 'one' character long")