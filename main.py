import os
from sys import exit
import random
from art import logo

# Defining Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

def newgame():
    if input("Do you want to play a game of Blackjack? y/n") == "y":
        os.system("clear")
        print(logo)
        global cards
        global user_cards
        global computer_cards
        global user_score
        global computer_score
        user_cards = []
        computer_cards = []
        user_score = 0
        computer_score = 0
        return loop()
    else:
        exit()

def deal_card():
    cardIndex = random.randint(0,12)
    card = cards[cardIndex]
    return card

def calc_score(cards):
    score = 0
    for i in cards:
        score += i
    return score

def blackjack(cards, score, player):
    if score == 21:
        print(f"{player} Got Black Jack!")
        if player.lower() == "user":
            win()
        elif player.lower() == "computer":
            lose()
    elif score > 21:
        if 11 in cards:
            ace = cards.index(11)
            cards[ace] = 1
            score = calc_score(cards)
            blackjack(cards, score, player)
        else:
            if player.lower() == "user":
                lose()
            elif player.lower() == "computer":
                win()

    return cards, score

def win():
    print("\nRevealing Cards..")
    print(f"User Cards: {user_cards}, User Score: {user_score}")
    print(f"Computer Cards: {computer_cards}, Computer Score: {computer_score}\n")
    
    print("Player Wins!")
    return newgame()

def lose():
    print("\nRevealing Cards..")
    print(f"User Cards: {user_cards}, User Score: {user_score}")
    print(f"Computer Cards: {computer_cards}, Computer Score: {computer_score}\n")
    
    print("Computer Wins!")
    return newgame()

def draw():
    print("\nRevealing Cards..")
    print(f"User Cards: {user_cards}, User Score: {user_score}")
    print(f"Computer Cards: {computer_cards}, Computer Score: {computer_score}\n")
    
    print("Its a Draw!")
    return newgame()

def loop():
    # Globalizing Variables
    global cards
    global user_cards
    global computer_cards
    global user_score
    global computer_score

    # Giving User Cards
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    # Giving Computer Cards
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    # Updating Score
    user_score = calc_score(user_cards)
    computer_score = calc_score(computer_cards)

    # Checking for Black Jack
    user_cards, user_score = blackjack(user_cards, user_score, "User")
    computer_cards, computer_score = blackjack(computer_cards, computer_score, "Computer")

    # Printing User and Computer Cards
    print(f"User Cards: {user_cards}, User Score: {user_score}")
    print(f"Computer Card: [{computer_cards[0]}]")

    # Checking if User Wants New Card
    new_card = input("Do want another card? y/n").lower()
    if new_card == "y":
        user_cards.append(deal_card())
        user_score = calc_score(user_cards)
        user_cards, user_score = blackjack(user_cards, user_score, "User")
        print("\nUser Draws Card..")
        print(f"User Cards: {user_cards}, User Score: {user_score}")
        print(f"Computer Card: [{computer_cards[0]}]")
    elif new_card == "n":
        pass
    else:
        exit("Due to 'Invalid Response', The Game Is Being Terminated..")

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)
        computer_cards, computer_score = blackjack(computer_cards, computer_score, "Computer")
        print("\nComputer Draws Card..")
        print(f"User Cards: {user_cards}, User Score: {user_score}")
        print(f"Computer Card: [{computer_cards[0]}]") 

    # Checking Winner
    if user_score > computer_score:
        win()
    elif user_score < computer_score:
        lose()
    else:
        draw()
    
    return newgame()

newgame()