import random

answer = random.randint(1, 1000)
tries = 0
min_guess = 1
max_guess = 1000

while tries < 10:
    guess = int(input(f'Guess the number between {min_guess}-{max_guess}: '))
    tries += 1
    if guess == answer:
        print(f'You win with {tries} tries!')
        break
    elif guess < answer:
        if guess >= min_guess:
            min_guess = guess + 1
        print('Too low!')
    else:
        if guess <= max_guess:
            max_guess = guess - 1
        print('Too high!')
    print(f'The number is between {min_guess} and {max_guess}!')
else:
    print(f'You lose! The answer was {answer}')