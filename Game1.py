#This will be a game where there's two players and a random number generator from 1 to 100. The player that has the closest number wins.
import random

while True:
    #Ask for their inputs

    player1 = int(input("Player 1, Say a number from 1 to 100: "))
    player2 = int(input("Player 2, Say a number from 1 to 100: "))

    #check if they're valid

    if player1 <= 0 or player1 > 100:
        print("Player 1's amount is wrong!")
    if player2 <= 0 or player2 > 100:
        print("Player 2's amount is wrong!")

    while player1 > 0 and player2 > 0 and player1 <= 100 and player2 <= 100:
        amount = random.randint(1, 100)

        #Check the distance between the input and the random number generator.

        P1Distance = abs(player1 - amount)
        P2Distance = abs(player2 - amount)

        #Compare the distance between the players and the random number generator.

        if P1Distance < P2Distance:
            print("Player 1 wins! The amount is ", amount)
        if P1Distance > P2Distance:
            print("Player 2 wins! The amount is ", amount)
        if P1Distance == P2Distance:
            print("It's a tie! The amount is", amount)

        #ask if they want to play again.
        PlayAgain = str(input("Want to play again? Y/N: "))
        PA_low = PlayAgain[0].lower()
        if PA_low == "y":
            player1 = 0
            player2 = 0
        if PA_low == "n":
            exit()
