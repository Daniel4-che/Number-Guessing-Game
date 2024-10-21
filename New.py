import random

print("""Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 10.\nYou have three levels to choose from: \n""")

def selectlevel():
    print("""1.Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances)""")
    userlevel = input("Enter your choice: ")
    return int(userlevel)

def handleguess():
    level = selectlevel()
    leveltext = "Easy" if level == 1 else "Medium" if level == 2 else "Hard" if level == 3 else print ("Wrong level  selected")
    chances = 10 if level == 1 else 5 if level == 2 else 3 
    print(f"Great! You have selected the {leveltext} diffulty level.")
    attempts = 0
    randomnumber = random.randint(1, 100)
    while chances > 0:
        userinput = int(input("Enter your guess: "))
        attempts += 1
        chances -= 1
       
        if userinput == randomnumber:
            print(f"congratulations! You guessed after {attempts} attempts")
            break
        else:
            Winning_number = (randomnumber// 10 + 1) * 10
            print(f"Hint: The winning number is less than {Winning_number}.")
            print(f"You have {chances} chances left.")
    else: print("Game over! You have no chance left")

handleguess()                