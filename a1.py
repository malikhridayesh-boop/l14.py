import random
playing = True
number = random.randint(0,9)
print("Welcome to the guessing game!")
print("I have selected a number between 0 and 9. Can you guess it?")
while playing:
    guess = input("Enter your guess: ")
    if number == int(guess):
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Sorry, that's not the correct number. Try again!")