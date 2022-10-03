# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:15:34 2022

@author: sp7012
"""
from random import randint
#create a list of play options
t = ["Rock", "Paper", "Scissors"]
BrL=0
BrW=0
#assign a random play to the computer
computer = t[randint(0,2)]


while (BrW <= 2 and BrL<=2):
    computer = t[randint(0,2)]
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print( computer, "covers", player)
            BrL+=1
        else:
            print(player, "smashes", computer)
            BrW+=1

    elif player == "Paper":
        if computer == "Scissors":
            print(computer, "cut", player)
            BrL+=1
        else:
            print( player, "covers", computer)
            BrW+=1
    elif player == "Scissors":
        if computer == "Rock":
            print( computer, "smashes", player)
            BrL+=1
        else:
            print(player, "cut", computer)
            BrW+=1
    else:
        print("That's not a valid play. Check your spelling!")
  
if BrW == 3:
 print("You Win, Congratulations")        
elif BrL==3:
 print("You lose Maybe next time")          
        
        
        
