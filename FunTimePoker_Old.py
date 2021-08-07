#!/data/RP/source/noRepo/Project/pokerTest/env/bin/python


from deck_of_cards import deck_of_cards
from os import system, name
from time import sleep
import random
#import numpy as np

def clear():
    #for NT operating systems like Windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#deck_obj = deck_of_cards.DeckOfCards()
#card = deck_obj.give_random_card()
#def deckOfCards():



dialogSleepInterval = 2
#maxShuffle = 3
maxShuffle = random.randint(1,5)
maxHand = 5
#print(maxShuffle)

class Player:
    def __init__(self, name, nickname, age):
        self.name = name
        self.nickname = nickname
        self.age = age

    def playerGreetings(self):
        print("Well HowdyDoo {} aka. {}!\n".format(self.name, self.nickname))
        sleep(dialogSleepInterval)
    
    def playerAgeCheck(self):
        if int(self.age) < 18:
            print("I Am Very Sorry {} Your Are Not Old Enough To Play This Game Of Chance".format(self.nickname))
            sleep(dialogSleepInterval)
            exit(1)
        else:
            newPlayerInfo.playerGreetings()

class Card:
    def __init__(self, suit, val, name):
        self.suit = suit
        self.value = val
        self.name = name
    
    def show(self):
        #print("{} of {}".format(self.value, self.suit))
        print(self.name)

def playerNew():
    clear()
    newPlayerQuestions = {"PlayerName": 'What is Your Name Stranger? ', "PlayerNickname": 'Here In The West, What Name Should Your Rivals Cower From? ', "PlayerAge":  'We Have To Ask, What Is Your Age? '}
    newPlayerInfo = {}

    for key, value in newPlayerQuestions.items():
        answer = input(value)
        newPlayerInfo[key] = answer
        clear()
    newPlayerInfo = Player(newPlayerInfo["PlayerName"], newPlayerInfo["PlayerNickname"], newPlayerInfo["PlayerAge"])
    #return newPlayerInfo
    return newPlayerInfo

def dealingHand(maxHand):
    deck_obj = deck_of_cards.DeckOfCards()
    maxHand = maxHand
    cardsDealt = 0
    cardsInHand = []
    suitInHand = []
    print
    print("Good Luck With This Hand!\n")
    sleep(dialogSleepInterval)
    while cardsDealt < maxHand:
        card = deck_obj.give_random_card()
        #card.suit  # 0=spades, 1=hearts, 2=diamonds, 3=clubs, 4=joker
        #card.rank  # 1=Ace, 11=Jack, 12=Queen, 13=King, 14=B&W Joker, 15=Color Joker
        #card.value # defaults: same as rank
        #card.name  # string representation
        if card.suit == 0:
            suit = '\u2660'
        elif card.suit == 1:
            suit = '\u2665'
        elif card.suit == 2:
            suit = '\u2666'
        elif card.suit == 3:
            suit = '\u2663'
        elif card.suite == 4:
            suit = '\u1F0BF'

        if card.value == 1:
            rank = 'A'
        elif card.value == 11:
            rank = 'J'
        elif card.value == 12:
            rank = 'Q'
        elif card.value == 13:
            rank = 'K'
        else:
            rank = card.value            

        print("{} {}".format (rank, suit))
        #print("{} ({})".format (card.name, card.value))
        sleep(0.5)
        cardsInHand.append(card.value)
        suitInHand.append(card.suit)
        cardsDealt = cardsDealt + 1
        if cardsDealt == maxHand:
            #break
            continue
    #print(cardsInHand)
    print("")
    print(cardsInHand)
    return cardsInHand, suitInHand

def shuffleDeck(maxShuffle):

    shuffle = 'Shuffle...'
    maxShuffle = maxShuffle
    shuffleCount = 0
    while shuffleCount < maxShuffle:
        for i in range(10):
            print(shuffle[i], sep=' ', end=' ', flush=True); sleep(0.1)
        shuffleCount = shuffleCount + 1
        #print(shuffleCount)
        if shuffleCount == maxShuffle:
            continue

def rankOfHand(cardsInHand, suitInHand):
    cardsInHandUnique = set(cardsInHand)
    #cardsInHandSorted = sorted(cardsInHand)
    rankedHand = []
    suitHand = []
    d = {x:suitInHand.count(x) for x in suitInHand}
    #d = sorted(d.items())
    print(cardsInHandUnique)
    print(cardsInHand)    
    for y in cardsInHandUnique:
        if cardsInHand.count(y) >= 4:
            rankedHand.append(4)
        elif cardsInHand.count(y) == 3:
            rankedHand.append(3)
        #IF two of the same cards it's one Pair
        elif cardsInHand.count(y) == 2:
            rankedHand.append(1)
            d = {x:rankedHand.count(x) for x in rankedHand}
            if d[1] == 2:
                rankedHand.append(2)
                valueToBeRemoved = 1
                try:
                    while True:
                        rankedHand.remove(valueToBeRemoved)
                except ValueError:
                    pass        
    ##Evalute Potential of Flush vs Royal Flush
    try:
        for y in cardsInHand:
            #Potential Upward
            if (y + 1) == cardsInHand[1]:
                if (y + 2) == cardsInHand[2]:
                    if (y + 3) == cardsInHand[3]:
                        if (y + 4) == cardsInHand[4]:
                            rankedHand.append(5)

            #Potential Downward
            if (y - 1) == cardsInHand[1]:
                if (y - 2) == cardsInHand[2]:
                    if (y - 3) == cardsInHand[3]:
                        if (y - 4) == cardsInHand[4]:
                            rankedHand.append(5)


        #Potential Royal Flush
            #print(y)
            if y == 1:
                if (y + 12) == cardsInHand[1]:
                    if (y + 11) == cardsInHand[2]:
                        if (y + 10) == cardsInHand[3]:
                            if d[0] == 5:
                                rankedHand.append(55)

    except ValueError:
        pass

    try:
        d = {x:suitInHand.count(x) for x in suitInHand}
        #print(d)
        d = sorted(d.items())
        for key, value in d:
            if value == 5:
                #print(key)
                rankedHand.append(6)

        #print(d)

        #print(d[-1])


    except ValueError:
        pass      
    
    #print(cardsInHand)
    #print(max(cardsInHandUnique))
    #print(cardsInHand)
    #print(suitInHand)     
    #Winning Rank
    rankedHand = sorted(rankedHand)
    print(rankedHand)
    try:
        if rankedHand[-1] == 55:
            print("Winning Hand: ROYAL FLUSH!!!!")
        elif rankedHand[-1] == 5:
            print("Winning Hand: Flush!")
        elif rankedHand[-1] == 4:
            print("Winning Hand: Four of A Kind!")
        elif rankedHand[-1] == 3:
            if rankedHand[-2] == 1:
                print("Winning Hand: Full House!")
        elif rankedHand[-1] == 6:
            print("Winning Hand: Flush!")
        elif rankedHand[-1] == 3:
            print("Winning Hand: Three of A Kind!")
        elif rankedHand[-1] == 2:
            print("Winning Hand: Two Pairs!")            
        elif rankedHand[-1] == 1:
            print("Winning Hand: One Pair!")






        # elif rankedHand[-1] == 0:
        #     print("Winning Hand: High Card")
    except:
        print("Sorry Better Luck Next Time")

    #print(rankedHand)
    #print(d)
    #print(rankedHand)
    
    #print(rankedHand)
    #print("You Have: Two Pair!")

        
    #print(rankOfHand)
    

######################IMPORTANT DO NOT REMOVE
#newPlayerInfo = playerNew()
#newPlayerInfo.playerAgeCheck()


#shuffleDeck(maxShuffle)
#cardsInHand, suitInHand = dealingHand(maxHand)

cardsInHand = [1, 12, 12, 11, 10]
suitInHand = [0, 1, 2, 1, 0]
#cardsInHand = [6, 6, 6, 5, 5]

#rankOfHand = rankOfHand(cardsInHand)
rankOfHand(cardsInHand,suitInHand)

######################IMPORTANT DO NOT REMOVE
