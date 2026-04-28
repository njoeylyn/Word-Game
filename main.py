from word_game import *

def main():
    while True:
        print('\n-------Welcome to the word game!-------')
        print('Please select an option below to begin:')
        print('1. New Game')
        print('2. Add word')
        print('3. View word bank')
        print('4. Quit')

        choice = input('Please pick a number 1-4: ')

        if choice == '1':
            start_game()
    
        elif choice == '2':
            print('\nNote: We recommend doing this if you are playing with a friend!')
            while True:
                new_word = input('\nPlease provide a word you would like to add: ')

                if not new_word.isalpha():
                    print('Please print a valid word that only contains letters.')
                    continue
                elif len(new_word) <= 2:
                    print('Please input a word at least three letters in length.')
                    continue
                else:
                    word_bank.append(new_word)
                    print(f'"{new_word}" has been added to the word bank!')
                    break
        elif choice == '3':
            print(f'The current words in the word bank are: {word_bank}')

        elif choice == '4':
            print('\nThank you for playing!')
            break

        else:
            print('Invalid choice, please enter a number 1 through 4.')
            continue

if __name__ == '__main__':
    main()