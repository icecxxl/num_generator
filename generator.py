import random

def num_generator(min_0, max_0):
    # function to generate a random number within the given range
    return random.randint(min_0, max_0)

def user_guess():
    #function to retrieve user's guess
    while True:
        try:
            guess =int(input("Enter Your Guess: "))
            return guess
        except ValueError:
            print("Invalid Input. Please enter a valid integer")

def play_game():
    #main function that executes the game
    print("Welcome To The Generator")
    min_0 = int(input("Enter a minimum number: "))
    max_0 = int(input("Enter a maximum number: "))

    #now to generate the secret/random number
    secret_num = num_generator(min_0, max_0)
    print(" have generated a random number between {min} and {max}.")

    attempts = 0

    while True:
        guess = user_guess()
        attempts += 1

        if guess == secret_num:
            print("Congrats! You guessed the {secret_num} in {attempts} attempts!")

        elif guess<secret_num:
            print("Below Number, Try Again!")
        else:
            print("Above Number, Try Again!")

if __name__ == "__main__":
    play_game()
