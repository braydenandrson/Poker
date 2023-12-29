# Brayden Anderson
# 12/28/2023

# This program will be a poker assistant that will help you make decisions based on the cards you have

class player():
    card1 = ""
    card2 = ""
    money = 0
    folded = False

class game():
    numPlayers = 0
    myCards = []
    communityCards = []
    turn = 1
    flop, turn, river = False, False, False
 

# Game info:
game = game()
player1 = player()

def handProbability():
    pass

def welcome():
    print("\n***************************************************************************************************")
    print("\nHello from your personal poker assistant!\n")
    print("A few things to note before we started:\n")
    print("\t- this program current will tell you the probabilty of getting a certain hand\n")
    print("\t- this program will tell you your chances of winning based on the cards presented\n")
    print("\t- this program does NOT read players and their tendencies... that is up to you\n")
    print("-----------------------------------------------------------------------------------------------\n")

    game.numPlayers = input("How many players are in the game? ")
    player1.card1 = input("\nWhat is your first card? ")
    game.myCards.append(player1.card1)
    player1.card2 = input("\nWhat is your second card? ")
    game.myCards.append(player1.card2)

    print("\n-----------------------------------------------------------------------------------------------\n")
    print("\nSo this is what we know so far:\n")
    print("\t- there are " + game.numPlayers + " players in the game\n")
    print("\t- your first card is a " + player1.card1 + "\n")
    print("\t- your second card is a " + player1.card2 + "\n")
    print("This means that the current possibilities for specific hand combinations are... \n")

    handProbability()

    print("Let the game commence!\n")
    print("-----------------------------------------------------------------------------------------------\n")

def engine():
    while not game.flop:
        next = input("Did the flop come out? (y/n) ")

        if next == "y": game.flop = True

    game.communityCards.append(input("\nWhat is the first card? "))
    game.communityCards.append(input("\nWhat is the second card? "))
    game.communityCards.append(input("\nWhat is the third card? "))

    print("\n-----------------------------------------------------------------------------------------------\n")
    print("This means that the current possibilities for specific hand combinations are... \n")

    handProbability()

    print("-----------------------------------------------------------------------------------------------\n")

    while not game.turn:
        next = input("Did the turn come out? (y/n) ")

        if next == "y": game.turn = True

    game.communityCards.append(input("\nWhat is the fourth card? "))

    print("\n-----------------------------------------------------------------------------------------------\n")
    print("This means that the current possibilities for specific hand combinations are... \n")

    handProbability()

    print("-----------------------------------------------------------------------------------------------\n")

    while not game.river:
        next = input("Did the river come out? (y/n) ")

        if next == "y": game.river = True

    game.communityCards.append(input("\nWhat is the fifth card? "))

    print("\n-----------------------------------------------------------------------------------------------\n")

    print("This means that the current possibilities for specific hand combinations are... \n")

    handProbability()

    print("-----------------------------------------------------------------------------------------------\n")

def end():
    print("\nThank you for using me, and I hope you found me useful!\n")
    print("***************************************************************************************************\n")

def main():
    welcome()
    engine()
    end()

if __name__ == "__main__":
    main()