#!/usr/bin/env python3

#Engineering Flow Chart

def yesItMoves():
    answerYesMoves = input("But should it move?")
    if answerYesMoves.strip().upper() == "YES":
        print("NO PROBLEMO SUCKA")
    elif answerYesMoves.strip().upper() == "NO":
        print("Duct tape")
    else:
        yesItMoves()

def noNotMoves():
    answerNotMoves = input("Should it move?")
    if answerNotMoves.strip().upper() == "YES":
        print("WD-40")
    elif answerNotMoves.strip().upper() == "NO":
        print("NO PROBLEM")
    else:
        noNotMoves()

def askFirstQuestion():
    answer1 = input("Does it move?")
    if answer1.strip().upper() == "YES":
        yesItMoves()
    elif answer1.strip().upper() == "NO":
        noNotMoves()
    else:
        askFirstQuestion()

def beginFlowChart():
    print('\n' * 2)
    print("This engineering flowchart will determine what you should do during times of engineering confusion.")
    print('\n' * 2)
    askFirstQuestion()

def main():
    beginFlowChart()

main()