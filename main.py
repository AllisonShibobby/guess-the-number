from random import randint

def guess(x):
    random_number = randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))
        if guess_number > random_number:
            print("Sorry, guess again. Too high.")
        elif guess_number < random_number:
            print("Sorry, guess again. Too low.")

    print(f"Yay, Congrats! You have guessed the number {random_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = randint(low, high)
        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c) ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay!  The computer have guessed your number, {guess}, correctly!")



if __name__ == "__main__":
    computer_guess(8)