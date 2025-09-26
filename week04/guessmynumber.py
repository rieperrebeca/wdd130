import random   

keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1, 100)
    print(f"the random number was:{secret_number}")
    guess_count = 0
    guess = -1

    while guess != secret_number:
        guess = int(input("what is your guess? "))
        guess_count = guess_count + 1

        if guess < secret_number:
            print("too low")
        elif guess > secret_number:
            print("too high")
        else:
            print("you got it!")

    print(f"you took {guess_count} guesses")

    keep_playing = input("would you like to play again yes/no?")
