#!./env/bin/python

#Importing:
#os -  used in clear() function
#time - used for dialogSleep
#random - used to randomize the amount of shuffles
#treys is the main component for this game, as it contains deck, card and the evaluator
from os import system, name
from time import sleep
import random
from treys import Card, Evaluator, Deck

##Messages
suiteMessage = ' -- \u2660 \u2665 \u2666 \u2663 \n\n' #Unicode for card suits

welcomeMessage="Welcome To " #Part of Welcome message
byeMessage="\n\nBye!\n\n"

##Value Based Variables
dialogSleepInterval = 2 #How long dialogs will pause for
maxHand = 5 #Used to determine max amount of cards in hand.
ageLimit = 18

def scriptName():
    scriptName=__file__.strip('.py /') #Gets the current script name, usefull when printing the name of your script and the name might change
    return scriptName

def clear():
    #Clear screen based on operating system
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def runningPrint(message, speed):
    #Used as the Main printing mechanism for the running text
    for i in range(len(message)):
        print(message[i], sep=' ', end=' ', flush=True); sleep(speed)


class Player:
    #I am not very comfortable using classes yet, but i did try this out.
    #Player information will be read into this class and be referenced by playerGreetings and Player Age Check
    def __init__(self, name, nickname, age):
        self.name = name
        self.nickname = nickname
        self.age = age

    def playerGreetings(self):
        greetingsMessage = "\nWell HowdyDoo {} aka. {}!\n\n".format(self.name, self.nickname)
        runningPrint(greetingsMessage, 0.1)
        sleep(dialogSleepInterval)
    
    def playerAgeCheck(self):
        #Not really planned on using the age for anything but did include it in my list of questions, so decided to make it do an age check since poker is "gambling"
        if int(self.age) < ageLimit:
            underAgemessage = ("I Am Very Sorry {} You Are Not Old Enough To Play This Game Of Chance".format(self.nickname))
            runningPrint(underAgemessage, 0.1)
            sleep(dialogSleepInterval)
            runningPrint(byeMessage, 0.6)
            exit(1)
        else:
            newPlayerInfo.playerGreetings()


def playerNew():
    #List of Questions that gets asked in a for loop (so more can be added if required)
    newPlayerQuestions = {"PlayerName": 'What is Your Name Stranger? ', "PlayerNickname": ' Here In The West, What Name Should Your Rivals Cower From? ', "PlayerAge":  ' We Have To Ask, What Is Your Age? '}
    newPlayerInfo = {}
    #Iterates through the list and print the questions out and reads the answer into a dictionary
    for key, value in newPlayerQuestions.items():
        for i in range(len(value)):
            print(value[i], sep=' ', end=' ', flush=True); sleep(0.1) 
        answer = input()
        newPlayerInfo[key] = answer
    newPlayerInfo = Player(newPlayerInfo["PlayerName"], newPlayerInfo["PlayerNickname"], newPlayerInfo["PlayerAge"])
    return newPlayerInfo


def dealingHand(maxHand):
    #Sets the deck variable from the treys modulem then sets required variables and draws board + player hand
    deck = Deck()
    goodLuckMessage = '\n\nGood Luck With This Hand!\n\n'
    runningPrint(goodLuckMessage, 0.1)
        
    sleep(dialogSleepInterval)

    board = deck.draw(maxHand - 2)
    player1_hand = deck.draw(2)

    for i in range(5 * maxHand):
        print(Card.print_pretty_cards(board + player1_hand)[i], sep=' ', end=' ', flush=True); sleep(0.1)
    return board, player1_hand


def evaluteHand(board, player1_hand):
    #Evalutes the platers hand and prints out the winning hand (best score)
    evaluator = Evaluator()
    p1_score = evaluator.evaluate(board, player1_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    sleep(dialogSleepInterval)
    winningHandMessage = "\n\nWinning Hand is!\n"
    runningPrint(winningHandMessage, 0.1)

    sleep(dialogSleepInterval)
    winningRankHandMessage = "\n {}!".format(evaluator.class_to_string(p1_class))
    runningPrint(winningRankHandMessage, 0.1)
    retryMessage = '\n\nWould You Like To Try Again? (y/n): '
    runningPrint(retryMessage, 0.1)
    while "The Answer Is Invalid":
        reply = str(input()).lower().strip()
        if reply[0] == 'y':
            clear()
            shuffleDeck()
            board, player1_hand = dealingHand(maxHand)
            evaluteHand(board, player1_hand)
        if reply[0] == 'n':
            runningPrint(byeMessage, 0.6)
            exit()


def shuffleDeck():
    #Simulates a deck suffeling, randomized the shuffle printout between 2 and 5 times
    maxShuffle = random.randint(2,5)
    shuffle = 'Shuffle...'
    #maxShuffle = maxShuffle
    shuffleCount = 0
    while shuffleCount < maxShuffle:
        for i in range(10):
            print(shuffle[i], sep=' ', end=' ', flush=True); sleep(0.1)
        shuffleCount = shuffleCount + 1
        #print(shuffleCount)
        if shuffleCount == maxShuffle:
            continue

#clears Screen for neatness
clear()
#prints Intro messages
runningPrint(welcomeMessage, 0.1)
runningPrint(scriptName(), 0.1)
runningPrint(suiteMessage, 0.1)

#start of script player onboarding, player age check (since its gambling) and shuffle of deck
newPlayerInfo = playerNew()
newPlayerInfo.playerAgeCheck()
shuffleDeck()

#Dealing of hand and evaluation phase
board, player1_hand = dealingHand(maxHand)
evaluteHand(board, player1_hand)