#-------------------------------------------------------------------------------
# Name:        Auction
# Purpose:
#
# Author:      bettanyd
#
# Created:     11/04/2014
# Copyright:   (c) bettanyd 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

reserve= 0
name= 0
bid= 0
reserve= input("What is the reserve?")
print ("Auction has started")
print ("Highest bid so far is $0.00")
while name != "F":
    name= input("What is your name?")
    if name == "F":
        if winnerb > reserve:
            print ("The reserve was met" ,winnern,"has won the auction")
        elif bid < reserve:
            print ("The reserve was not met, sorry",winnern,"you do not win")
    bid= input("What is your bid?")
    if bid > reserve:
        winnern = name
        winnerb = bid
        print ("Highest bid so far is $",bid,)
    elif bid < reserve:
        print ("Sorry",name,"please place a higher bid")

