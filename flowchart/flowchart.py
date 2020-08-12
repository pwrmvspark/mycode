#!/usr/bin/env python3

#Engineering Flow Chart

def exit():
    import sys
    sys.exit(0)

def yesItMoves():
    answerYesMoves = input("But should it move?")
    if answerYesMoves.strip().upper() == "YES":
        print("NO PROBLEMO SUCKA")
    elif answerYesMoves.strip().upper() == "NO":
        print("Duct tape, https://www.amazon.com/duct-tape/s?k=duct+tape")
    elif answerYesMoves.strip().upper() == "Q":
        exit()
    else:
        yesItMoves()

def noNotMoves():
    answerNotMoves = input("Should it move?")
    if answerNotMoves.strip().upper() == "YES":
        print("WD-40, https://www.amazon.com/WD-40-Multi-Use-Product-Spray-Smart/dp/B0083V8H0I")
    elif answerNotMoves.strip().upper() == "NO":
        print("NO PROBLEM")
    elif answerNotMoves.strip().upper() == "Q":
        exit()
    else:
        noNotMoves()

def askFirstQuestion():
    answer1 = input("Does it move?")
    if answer1.strip().upper() == "YES":
        yesItMoves()
    elif answer1.strip().upper() == "NO":
        noNotMoves()
    elif answer1.strip().upper() == "Q":
        exit()
    else:
        askFirstQuestion()

def beginFlowChart():
    print('\n')
    print("This engineering flowchart will determine what you should do during times of engineering confusion.")
    print('\n')
    print('Hit the "q" key at anytime to quit')
    print('\n' * 2)

    askFirstQuestion()

def main():
    beginFlowChart()

main()