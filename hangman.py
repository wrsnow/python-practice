secret_word = "batman"
player_guesses = []
game_status = "running"
correctLetters = 0


def checkLetter(user_guess):
    global correctLetters
    correctLetters = 0
    player_guesses.append(user_guess.lower())
    for letter in secret_word:
        exists = False
        if letter in (player_guesses):
            exists = True
            correctLetters += 1
        if exists:
            print(letter.upper(), end="")
        else:
            print("-", end="")


def lineDividers(symbol, times):
    print(symbol*times)
    print("")


def play():
    print('''
		  HANGMAN

		  -------
		  |
		  |
		  |
		  |
		  |
		  |
		  |
		  |------------------

		  Pick a letter to start playing.

		  ''')
    global correctLetters
    while (game_status != "end" and correctLetters != len(secret_word)):
        print(f"Letter used: {player_guesses}\n")
        user_guess = input("Pick a letter: ")
        print("\n")
        lineDividers("/", 20)
        checkLetter(user_guess)
        print("\n")
        lineDividers("/", 20)


play()
