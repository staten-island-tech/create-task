import random
import math

operations = ['a', 's', 'm', 'd'] # addition, subtraction, mulitplication, division, respectively
numbers = [4, 5, 6, 9, 10, 12, 13, 14, 18, 20, 23, 45]

def getUnitsDigit(num):
    return math.floor(num % 10)

def askQuestion():
    print(" ") # spacing/looks purposes
    randomNum1 = random.choice(numbers)
    randomNum2 = random.choice(numbers)
    num1 = max([randomNum1, randomNum2])
    num2 = min([randomNum1, randomNum2])
    # i want num1 to be greater than or equal to num2, for simplicity
    
    operation = random.choice(operations)
    if operation == 'a':
        response = int(input(f"What is the units digit of {num1} + {num2}? - "))
        if response == getUnitsDigit(num1+num2):
            return True
        else: 
            return False
        
    elif operation == 's':
        response = int(input(f"What is the units digit of {num1} - {num2}? - "))
        if response == getUnitsDigit(num1-num2):
            return True
        else: 
            return False
    elif operation == 'm':
        response = int(input(f"What is the units digit of {num1} x {num2}? - "))
        if response == getUnitsDigit(num1*num2):
            return True
        else: 
            return False
    else:
        response = int(input(f"What is the units digit of {num1} / {num2}? - "))
        if response == getUnitsDigit(num1/num2):
            return True
        else: 
            return False

def game(questions):
    questionsCorrect = 0
    print("For the following questions, respond with the units digit of the result.")
    for i in range(questions):
        if(askQuestion() == True):
            questionsCorrect += 1
            print("You got that correct!")
        else: 
            print("Sorry, you got that incorrect.")
            
    print(" ") # spacing/looks purposes
    print(f"You got {questionsCorrect} questions correct!")
    print(f"That's a score of {round((questionsCorrect/questions)* 100)}%!") 
    
game(int(input("How many questions do you want to be asked? - ")))