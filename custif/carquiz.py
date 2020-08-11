#!/usr/bin/env python3

def carGame():

    print('\n'*2)
    print("Welcome to the unBeatableCarGame, the questions get harder each level and if you get them all right, Danny will be seriously impressed. So let's try and impress Danny!")
    print('\n'*2)

    score = 0
    answer1 = input("Here's the first question, which ford vehicle paved the way for automotive technoglogy? \na) Mustang \nb) Model T \nc) Focus")

    if answer1 == "b":
        score = score + 1
    
    print('\n'*2)
    answer2 = input("Second question, how many cylinders does a Honda S2000 have? \na) 6  \nb) 4 \nc) 8")
    if answer2 == "b":
        score = score + 1

    print('\n'*2)
    answer3 = input("They're only going to get harder... here's hash tag three, what system uses exhaust gases to pull more air into an engine? \na) naturally aspirated \nb) supercharger \nc) turbocharger")
    
    if answer3 == "c":
        score = score + 1;

    print('\n'*2)
    answer4 = input("Let's hope you get some of these right - #4, what infamous 8 cylinder chevrolet engine is known for its high horsepower/torque cabilities, efficiency, and small form factor? \na) LS1 \nb) 2JZ \nc) K20")

    if answer4 == "a":
        score = score + 1;
    
    print('\n'*2)
    answer5 = input("Last one... make it count! which of these tires are best suitable for track/racing conditions? \na) Michelin Pilot Super Sport \nb) Pirelli P-Zero \nc) Toyo R888")

    if answer5 == "c":
        score = score + 1;

    print('\n'*2)
    print(f"You've earned {score} out of 5 questions!")

    print('\n')
    if score <= 2:
        print("you noob. bye.")
    elif score <= 4:
        print("you not noob but you not pro. same same but different. bye.")
    else: 
        print("brosif. im impressed. bye.")
    print('\n'*2)
 
carGame()
