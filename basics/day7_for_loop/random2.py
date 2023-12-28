import random

WORDS = ('python', 'softuni', 'държава', 'софтуер')
MAX_GUESSES = 3
RESPONSE_CONDITION = False

print('Welcome to SoftUni PB Game!')
print('You have to unscramble the word within', MAX_GUESSES, 'guesses.')

word = random.choice(WORDS)
scrambled_word = ''.join(random.sample(word, len(word)))

for guess in range(MAX_GUESSES):
    print('Srambled word:', scrambled_word)
    answer = input('Enter your guess: ')

    if answer == word:
        print("Congratulations! You unscrambled the word!")
        RESPONSE_CONDITION = True
        break
    else:
        print("Sorry, that's not correct")

if not RESPONSE_CONDITION:
    print("Sorry, you ran out of guesses. The word was:", word)
