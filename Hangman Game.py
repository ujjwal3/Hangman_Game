import random

def logo():
    return print(
        "____\n"
        "|    |\n"
        "|    O\n"
        "|   /|\\\n"
        "|   / \\"
    )

print("Welcome to Hangman!")

word_list = ["tree", "book", "key", "coma"]
bot_select = random.choice(word_list)
word_display = ["_" for _ in bot_select]

max_attempts = 6
attempts = 0
guessed_letters = []

while attempts < max_attempts:
    print(" ".join(word_display) + f" (Length: {len(bot_select)})")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in bot_select:
        print(f"Correct! The letter '{guess}' is in the word.")
        for i in range(len(bot_select)):
            if bot_select[i] == guess:
                word_display[i] = guess
    else:
        print(f"Incorrect! The letter '{guess}' is not in the word.")
        attempts += 1
        logo()

    if "_" not in word_display:
        print(f"Congratulations! You guessed the word '{bot_select}' correctly!")
        break

if "_" in word_display:
    print(f"Sorry, you ran out of attempts. The word was '{bot_select}'.")
