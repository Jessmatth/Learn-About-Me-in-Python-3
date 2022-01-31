#Welcome and introduction
print("Welcome to two truths and a lie.  You will be asked to evaluate three statements about Jess Matthews.  Your task is to identify the statement that is not true.")  
print()
print("You will get 10 questions.  If you answer more than 7 correctly, you win!")
print()

# #Answer Key
answer_key_1 = "C"
answer_key_2 = "B"
answer_key_3 = "A"
answer_key_4 = "C"
answer_key_5 = "C"
answer_key_6 = "B"
answer_key_7 = "A"
answer_key_8 = "B"
answer_key_9 = "C"
answer_key_10 = "C"


# Question dataset
question_1 = """Which of the following is not true: 
A. Jess was in a metal band with her older brother. They released their first recording on a cassette tape  called, Deal with the Madness
B. Jess grew up in a town with a population of 200.  It had a single stop sign and cows out numbered people in the county.
C. Jess has a pet gecko named, Herbert."""



print(question_1)
print()
num_correct = 0

answer_1 = input("Please enter A. B. or C. >")
answer_1 = answer_1.upper()
if answer_1 in answer_key_1: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} point.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} correct answers.")
    print("Let's try again.")

question_2 = """Which of the following is not true:
A. Jess has owned and worn Jynco jeans.
B. Jess played in a band with her cousin called, Strawberry Garbage.
C. Jess graduated from college in 4.5 years with a BA and an MA."""

print(question_2)

answer_2 = input("Please enter A. B. or C. >")
answer_2 = answer_2.upper()
if answer_2 in answer_key_2: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was B.")
    print()
    print(f"You have {num_correct} correct answers.")
    print("Let's try again.")
    print()

question_3 = """Which of the following is not true: 
A. Jess created a website for hamster enthusiasts called, running down that road.
B. Jess studied abroad in the UK where she got to record the voiceover for a Russian Cosmonaut on ITV news.
C. One of Jess' favorite places is Torrey Pines a natural preserve north of San Diego that is home to the rarest pine trees in north america."""

print(question_3)
answer_3 = input("Please enter A. B. or C. >")
answer_3 = answer_3.upper()
if answer_3 in answer_key_3: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was A.")
    print()
    print(f"You have {num_correct} correct answers.")
    print("Let's try again.")
    print()


question_4 = """Which of the following is not true: 
A. Jess began learning to code on sololearn and W3. 
B. Jess' first formal coding class was a 500 level  python for data science course at UC Berkeley. 
C. Jess started COBOL programming as a way to connect with her father."""

print(question_4)
answer_4 = input("Please enter A. B. or C. >")
answer_4 = answer_4.upper()
if answer_4 in answer_key_4: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_5 = """Which of the following is not true: 
A. After college Jess' first job was as a best practices resaercher supporting CIOs and CTOs.
B. Other than working for her family, Jess' first job was a snowboard instructor. 
C. Jess' second job was in consulting at Booze Allen."""

print(question_5)
answer_5 = input("Please enter A. B. or C. >")
answer_5 = answer_5.upper()
if answer_5 in answer_key_5: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_6 = """Which of the following is not true: 
A. Jess lived in Washington DC.
B. Jess owns a Tesla. 
C. Jess has unlimed access to ice cream."""

print(question_6)
answer_6 = input("Please enter A. B. or C. >")
answer_6 = answer_6.upper()
if answer_6 in answer_key_6: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_7 = """Which of the following is not true: 
A. Jess considers herself to be type A.
B. Jess is in an improv troupe. 
C. Jess prefers Sheetz to Wawa."""

print(question_7)
answer_7 = input("Please enter A. B. or C. >")
answer_7 = answer_7.upper()
if answer_7 in answer_key_7: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("Sorry, the correct answer was C.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_8 = """Which of the following is not true: 
A. Jess became interested in technology while watching rockets take off from Cape Canavral with her Grandma.
B. Jess helped Jillian Michaels create the 30 Day Shred workout series. 
C. Jess presented to 120 sales leaders in Sydney."""

print(question_8)
answer_8 = input("Please enter A. B. or C. >")
answer_8 = answer_8.upper()
if answer_8 in answer_key_8: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was B.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_9 = """Which of the following is not true: 
A. Jess has surfed on 6 continents.
B. Jess was an NCAA athlete. 
C. Jess has three patents."""

print(question_9)
answer_9 = input("Please enter A. B. or C. >")
answer_9 = answer_9.upper()
if answer_9 in answer_key_9: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} answers.")
    print("Let's try again.")
    print()

question_10 = """Which of the following is not true: 
A. Jess was married by the major of San Francisco.
B. Jess worked on Wall Street during college. 
C. Jess has no pets."""

print(question_10)
answer_10 = input("Please enter A. B. or C. >")
answer_10 = answer_10.upper()
if answer_10 in answer_key_10: 
    print("You are correct!")
    print()
    print("That is not true.")
    num_correct = num_correct + 1
    print(f"You now have {num_correct} correct answers.")
    print()
else: 
    print("The correct answer was C.")
    print()
    print(f"You have {num_correct} correct answers.")
    print()

if num_correct >= 7: 
    print("Congratulations!  You Win!")
else: 
    print("You needed 7 to win.  Thank you for playing.")