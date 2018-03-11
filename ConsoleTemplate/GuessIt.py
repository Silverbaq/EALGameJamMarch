high, low = 100, 0

print('Please think of a number between {0} and {1}!'.format(low, high))

guessing = True
while guessing:
    guess = (low + high) // 2
    print('Is your secret number {0}?'.format(guess))
    pointer = input("Enter 'h' to indicate the guess is too high. "
                        "Enter 'l' to indicate the guess is too low. "
                        "Enter 'c' to indicate I guessed correctly.").lower()
    if pointer == 'h' :
        high = guess
    elif pointer == 'l' :
        low = guess
    elif pointer == 'c':
        guessing = False
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was {0}.'.format(guess))