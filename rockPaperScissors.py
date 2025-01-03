import random

aiWins = 0
userWins = 0
options = ["rock", "paper", "scissor"]

while True:
    userInput = input("Rock, Paper or Scissor? ")
    if userInput == "q":
        break
    if userInput not in options: # returns true if userInput is not found in the list
        continue

    aiGuess = options[random.randint(0, 2)]
    print("Computer guesses", aiGuess + ".")

    if userInput == "paper" and aiGuess == "rock": # and returns true if both conditions are true/ it functions like the logical and
        print("You won!")
        userWins += 1

    elif userInput == "rock" and aiGuess == "scissor":
        print("You won!")
        userWins += 1

    elif userInput == "scissor" and aiGuess == "paper":
        print("You won!")
        userWins += 1

    elif userInput == aiGuess:
        print("No one gets a point!")

    else:
        print("You lose!")
        aiWins += 1

print("You win", userWins, "times.")
print("Computer wins", aiWins, "times.")
print("Adios!")