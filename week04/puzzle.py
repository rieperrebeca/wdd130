
keep_playing = "yes"

while keep_playing == "yes":
    secret = "brazil"
    guess_count = 0
    guess = -1

    while guess != secret:
        guess = input("what is your guess? ").lower()
        guess_count = guess_count + 1 #guess count

        if guess == secret:
            print("Congratulations! you got it!")
        else:
            hint = ""
            for i in range(len(secret)):
                if i < len(guess) and guess[i] == secret[i]:
                    if guess[i] == secret[i]:
                        hint += secret[i] + " "
                    else:
                        hint += "_ "
                else:
                    hint += "_ "
            print("Hint:", hint)
            print("Try again.")
            print("")

    print(f"you took {guess_count} guesses") #guess count result

    keep_playing = input("would you like to play again yes/no?")

