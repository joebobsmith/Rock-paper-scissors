import os
import subprocess
from subprocess import run
from subprocess import check_output
import random
from random import choice
from random import choices

Choice_List = ["rock", "paper", "scissors"]
computer_choice = random.choice(Choice_List)
Op_1 = ("rock")
Op_2 = ("paper")
Op_3 = ("scissors")
str_1 = str(input("rock, paper, or scissors?:"))
print("______________________")
if str_1 == "rock":
    print("You chose: rock")
if str_1 == "paper":
    print("You chose: paper")    
if str_1 == "scissors":
    print("You chose: scissors")
print("Computer chose:", computer_choice)
print("______________________")

if computer_choice == str_1: 
    print("Tie. Try again.")
    
if computer_choice == Op_1 and str_1 == Op_2:
    print("You Win!!!")

if computer_choice == Op_2 and str_1 == Op_3:
    print("You Win!!!")

if computer_choice == Op_1 and str_1 == Op_3:
    print("You Lose :(")
    

if computer_choice == Op_3 and str_1 == Op_1:
    print("You Win!!!")

if computer_choice == Op_2 and str_1 == Op_1:
    print("You Lose :(")
    

if computer_choice == Op_3 and str_1 == Op_2:
    print("You Lose :(")
    