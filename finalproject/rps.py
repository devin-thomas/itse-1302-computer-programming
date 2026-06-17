#Devin Thomas
#ITSE 1302-003
#July 11, 2023

#This is a Rock, Paper, Scissors [RPS] simulator.
#The user will play against the computer.

import random as r

#We define the global set of answer choices 0, 1, 2
rps = ["rock", "paper", "scissors"]

#We get our choice from the user, convert it to lowercase and pass back to the main function
#Recursion is used to prevent invalid input
def userinput():
    user = input("Choose rock, paper or scissors:").lower()
    if user in rps:
        return user
    else:
        return userinput()
    
#We get a random selection for the CPU input
def cpu_choice():
    cpu = rps[r.randint(0,2)]
    return cpu
 
#rock beats scissors, scissors beat paper and paper beats rock    
def find_winner(user, cpu):
    
    if user == "rock":
        if (cpu == "rock"):
            return 3
        elif (cpu == "paper"):
            return 2
        elif (cpu == "scissors"):
            return 1
    elif (user == "paper"):
        if (cpu == "rock"):
            return 1
        elif (cpu == "paper"):
            return 3
        elif (cpu == "scissors"):
            return 2
    elif (user == "scissors"):
        if (cpu == "rock"):
            return 2
        elif (cpu == "paper"):
            return 1
        elif (cpu == "scissors"):
            return 3
    
    return winner

#Print the results
def show_winner(user, cpu, winner):
    print("You chose", user+ ", and the CPU chose", cpu+".")
    if (winner == 1):
        print("You win!")
    elif (winner == 2):
        print("CPU Wins!")
    elif (winner == 3):
        print("it's a tie!")
    return
    
#main() calls the other functions in order
def main():
    user = userinput()
    cpu = cpu_choice()
    winner = find_winner(user, cpu)
    show_winner(user, cpu, winner)
    
    
    
main()