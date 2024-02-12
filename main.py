
import random

words = ["amused","peaceful","fang","death","development","ignorant", "pastoral", "first", "natural", "channel", "skin", "volleyball","switch","power","action","painful","messy","wobble","surround","cure","scissors","crib","group"]

while True:
    word = random.choice(words)
    word_char_list = []
    correct_guessed: list[str] = []

    # We are going to break the characters of the word into a list, and then have a second list of underscores that get replaced by letters as they get guessed.
    for char in word:
        word_char_list.append(char)
        correct_guessed.append("_")

    print("""Let's play Hangman!
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========""")


    print(*correct_guessed)

    wrong_guesses = 0
    wrong_guess_list = []
    while True:
        guess = str(input("Guess a letter: "))
        # check for invalid input
        while not guess.isalpha() or len(guess) != 1:
            print("Sorry, your guess must be a letter. Please try again")
            guess = str(input("Guess a letter: "))
        if guess.isalpha() and len(guess) == 1:
            char_index = 0
            if guess.lower() in word_char_list:
                for char in word_char_list:
                    if char == guess.lower():
                        correct_guessed[char_index] = char
                    char_index += 1
            else:
                wrong_guesses += 1
                wrong_guess_list.append(guess.lower())
        if wrong_guesses == 0:
            print("""
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========""")
        elif wrong_guesses == 1:
            print("""
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========""")
        elif wrong_guesses == 2:
            print("""
              +---+
              |   |
              O   |
              |   |
                  |
                  |
           =========""")
        elif wrong_guesses == 3:
            print("""
              +---+
              |   |
              O   |
              |   |
             /    |
                  |
            =========""")
        elif wrong_guesses == 4:
            print("""
              +---+
              |   |
              O   |
              |   |
             / \\  |
                  |
            =========""")
        elif wrong_guesses == 5:
            print("""
              +---+
              |   |
              O   |
             /|   |
             / \\  |
                  |
            =========""")
        elif wrong_guesses == 6:
            print("""
              +---+
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            =========
            Game Over
            The word was""", word.upper())
            break
        if wrong_guesses != 0:
            print("Wrong guesses:",*wrong_guess_list)
        print(*correct_guessed)
        if "_" not in correct_guessed:
            print("You Win!")
            break
    play_again = input("Play Again? Y/N: ")
    if play_again.lower() != "y":
        print("Goodbye!")
        break