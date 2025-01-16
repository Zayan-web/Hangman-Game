import random

words = ["one", "two", "three","four","five","six","retarted"]
computer_choice = random.choice(words)
print("The number of letters your word has is " + str(len(computer_choice)))

wrong_guess_count = 0
max_wrong_guesses = 5
guessed_letters = []

while wrong_guess_count < max_wrong_guesses:
    user_guess = input("Enter a letter: ").lower()  # Use .lower() to handle case insensitivity

    # Check if the guess is a valid letter and hasn't been guessed before
    if user_guess in guessed_letters:
        print("You've already guessed that letter.")
    elif user_guess in computer_choice:
        print("This letter is in the word, keep going.")
        guessed_letters.append(user_guess)
    else:
        print("Sorry, this letter is not in the word.")
        wrong_guess_count += 1
        guessed_letters.append(user_guess)

    # Display the current progress of the word
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in computer_choice])
    print("Current word: " + display_word)

    # Check if the user has guessed the entire word
    if all(letter in guessed_letters for letter in computer_choice):
        print("Congratulations! You've guessed the word.")
        break

if wrong_guess_count == max_wrong_guesses:
    print("You have failed to beat this game.and we know your Ip haha your retarted")

