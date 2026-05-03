# Import random ensures that the word chosen for the game is chosen at random using the random function
import random

    # A word bank for all the words that can be guessed within the game
word_bank = ['python', 'college', 'panda', 'pizza']

def start_game():
    global attempts
    word = random.choice(word_bank)
    guessedWord = ['_'] * len(word)
    attempts = 10
    guessed_letters = []
    print("Starting your game!")

    while attempts > 0:
        print('\nCurrent word: ' + ' '.join(guessedWord))
        guess = input('Guess a letter: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Invalid input! Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print("You've already tried that letter! Please try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print('Great guess!')
        else:
            attempts -= 1
            print('Wrong guess! Attempts left: ' + str(attempts))

        if '_' not in guessedWord:
            print('\nCongratualtions!! You guessed the word: ' + word)
            break

    if attempts == 0 and '_' in guessedWord:
        print('\nYou\'ve run out of attempts! The word was: ' + word)

    
        
