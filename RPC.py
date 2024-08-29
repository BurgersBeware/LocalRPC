#import tool for random value selection
import random

#player chooses rock, paper, or scissors
playerChoice = input("Paper? Rock? Scissors? ")

#opponent "ai" chooses rock, paper, or scissors at random
possibleChoices = ['Paper', "Rock", "Scissors"]
opponentChoice = (random.choice(possibleChoices))

#global variables for use in functions
win = 1
tie = False

#win, loss, and tie conditions
if playerChoice == opponentChoice:
    tie = True
    win = 3
if playerChoice == "Rock" and opponentChoice == "Scissors":
    win = 2
if playerChoice == "Rock" and opponentChoice == "Paper":
    win = 1
if playerChoice == "Paper" and opponentChoice == "Scissors":
    win = 1
if playerChoice == "Paper" and opponentChoice == "Rock":
    win = 2
if playerChoice == "Scissors" and opponentChoice == "Paper":
    win = 2
if playerChoice == "Scissors" and opponentChoice == "Rock":
    win = 1

#print results to the terminal
print("-"*35)
print("You chose: ", playerChoice)
print("Your opponent chose: ", opponentChoice)
if win == 2:
    print("Result: Victory")
if tie == True or win == 3:
    print("Result: Tie")
if win == 1:
    print("Result: Loss")
print("-"*35)

