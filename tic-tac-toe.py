# A tic-tac-toe game in python 3.6
# developer: glatkobrasno
# version: 1.0
# see project at: https://github.com/glatkobrasno/python-tic-tac-toe-game
# contact developer via E-mail: renato.brasnic@gmail.com

import turtle # importing graphic module
import random # importing module for random numbers
coin=random.randint(0,1) # simulating a coin toss
boardx=[] # a list of x coordinats
boardy=[] # a list of y coordinats
turn=0 # defining turn counter

for i in range(21): # filling coordinate lists with 21 indexes of 0
    boardx.append(0)
    boardy.append(0)


if coin==0: # determining who goes first
    print ("X goes first")
    turn=0
else:
    print ("O goes first")
    turn=1
spacex,spacey=int(input("input x coordinate:")), int(input("input y coordinate:")) # waiting for coordinate input
