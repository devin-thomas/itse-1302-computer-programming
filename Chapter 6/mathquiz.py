#Devin Thomas
#ITSE 1302-003
#July 1, 2023

# Explain the purpose of the program
def intro():
    print("Welcome to the Math Quiz!")

# We need the random module in order to select random integers for the math quiz
def make_quiz():
    import random
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    print(f"{num1}\n+\n{num2}")
    print("Solve the addition problem above.")
    return num1 + num2

# The comparison is intended to prevent 
def answer(right_answer):
    # Try except is used to prevent value errors in the event of string input
    # We accept a float argument to prevent further errors
    try:
        user_answer = float(input("Enter your answer: "))
        if user_answer > right_answer or user_answer < right_answer:
            return False
        else:
            return True
    except ValueError:
        return False

def right():
    print("Congratulations! Your answer is correct.")

def wrong(right_answer):
    print(f"Sorry, your answer is incorrect. The correct answer is {right_answer}.")

def main():
    intro()
    right_answer = make_quiz()
    if answer(right_answer):
        right()
    else:
        wrong(right_answer)

main()
