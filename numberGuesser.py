import random

rangeInput = input("Type a number: ")

if rangeInput.isdigit():
    rangeInput = int(rangeInput)

    if rangeInput <= 0:
        print("Enter a number greater than 0")
        quit()
    else:
        randNum = random.randint(0, rangeInput)
else:
    print("Enter a number next time.")
    quit()

guessNum = 0

while True:
    guessNum += 1
    userInput = input("Guess a number within your range (previously typed): ")
    if userInput.isdigit(): #isdigit() function checks if the string is a digit or not/ but it does not consider negative numbers
        userInput = int(userInput)
    else:
        print("Type a number next time.")
        continue

    if userInput == randNum:
        print("You got it right!")
        break
    else: #the code here can be optimized using an elif statement
        if userInput < randNum:
            print("You are below the number.")
        else:
            print("You are above the number.")

print("You got in in", guessNum, "guesses!")