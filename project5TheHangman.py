import random

# Word list
words = ['python', 'kotlin', 'java', 'javascript', 'ruby', 'swift']
chosen_word = random.choice(words)

# Display: initialize with underscores
word_display = ['_' for _ in chosen_word]
attempts = 8
guessed_letters = set()

print("Welcome to Hangman!")

# Game loop
while attempts > 0 and '_' in word_display:
    print("\nWord: " + ' '.join(word_display))
    print(f"Attempts left: {attempts}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        print("Good guess!")
    else:
        print("That letter does not appear in the word.")
        attempts -= 1

# Conclusion
if '_' not in word_display:
    print("\nYou guessed the word:", chosen_word)
    print("You survived!")
else:
    print("\nYou ran out of attempts. The word was:", chosen_word)
    print("You lost.")
