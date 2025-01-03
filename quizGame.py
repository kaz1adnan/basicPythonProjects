print("Welcome to USQuizMania")

playDecision = input("Would you like to play? (Y/N): ")

if playDecision.lower() != "y": #converts the data into lowercase, it is done to increase user convenience
    quit() #When quit() function is used or becomes true, no code after that is executed

print("Okay, Let's look at your chances of getting into US unis!")

score = 0
#ques1
question = input("What does DET mean? ")
if question.lower() == "duolingo english test":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

#ques2
question = input("What does IELTS mean? ")
if question.lower() == "international english language testing system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques3
question = input("What does TOEFL mean? ")
if question.lower() == "test of english as a foreign language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques4
question = input("What does SAT mean? ")
if question.lower() == "scholastic assessment test":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques5
question = input("What does ECA mean? ")
if question.lower() == "extra curricular activity":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques6
question = input("What does CSS mean? ")
if question.lower() == "college scholarship service":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score) + " out of 6 questions!") #score is converted into string as only data types of string can be added with a + sign but score was in number data type
if score > 3:
    print("Great! Carry on your US trek! Meet ya at Princeton")
else:
    print("Dude! You lack dedication. These were just basics! Meet ya at SUST")