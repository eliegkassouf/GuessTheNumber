# Created by Elie Kassouf
# Wednesday January 22nd, 2020
# Guessing game with a little validation

import random

# Declaring so we know it's in the scope
amountOfGamesToPlay = 0
amountOfGamesPlayed = 0

def printGamesPlayed(gamesPlayed):
    print("\n\nGame #: " + str(gamesPlayed+1))
    return


def startTheGame():

    # Avoiding the notorious UnboundLocalError
    # This wouldn't happen in Java ;)
    global amountOfGamesToPlay
    global amountOfGamesPlayed


    # Set a random number
    randomNumberToGuess = random.randint(1, 25)
    guessesAttempted = 0

    printGamesPlayed(amountOfGamesPlayed)

    # While loop to loop through the number of games the user wants to play
    while amountOfGamesPlayed < amountOfGamesToPlay:

        try:
            usersGuessInput = int(input("Enter an integer from 1 to 25: "))

            if usersGuessInput >= 1 and usersGuessInput <= 25:

                if usersGuessInput < randomNumberToGuess:
                    print("\nGuess is low!")
                    guessesAttempted += 1
                elif usersGuessInput > randomNumberToGuess:
                    print("\nGuess is high!")
                    guessesAttempted += 1
                else:
                    print("\nYay, You guessed the number!\nAttempts made: " + str(guessesAttempted+1))
                    randomNumberToGuess = random.randint(1, 25)
                    guessesAttempted = 0
                    amountOfGamesPlayed += 1

                    if amountOfGamesPlayed < amountOfGamesToPlay:
                        printGamesPlayed(amountOfGamesPlayed)

            else:
                print("Not a valid input!\n")
                guessesAttempted += 1

        except:
            print("Please enter a valid integer!\n")
            guessesAttempted += 1


    return


def askTheUserHowManyGamesTheyWantToPlay():

    # Avoiding the notorious UnboundLocalError
    global amountOfGamesToPlay

    # Ask the user how many games they want to play
    userAmountOfGamesToPlayInput = input("How many games would you like to play?")

    # Check if the user inputed a proper INT (number)
    try:

        # Assign the input
        amountOfGamesToPlay = int(userAmountOfGamesToPlayInput)
    except:

        # Alert the user that the value supplied is not good
        print("Please enter a valid integer!\n")

    if amountOfGamesToPlay > 0:
        startTheGame()
    else:
        askTheUserHowManyGamesTheyWantToPlay()

    return


# Self explanatory -> Start the initial process
askTheUserHowManyGamesTheyWantToPlay()
