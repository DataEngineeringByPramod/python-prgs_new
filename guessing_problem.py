# guessing problem
number = 18
no_of_guessses = 1
print('you have 9 guesses to win the game')
while no_of_guessses<=9:
    guess_number = int(input('enter a number'))
    if guess_number > 18:
        print('greater then required')
    elif guess_number < 18:
        print('lesser then required')
    else:
        print('WINNER')
        print('no_of_guessses taken by a player :',no_of_guessses)
        break
    print(9-no_of_guessses,'left guesses')
    no_of_guessses = no_of_guessses+1
if no_of_guessses>9:
    print('you lost the game')
