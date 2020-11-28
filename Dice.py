import random
def main():
    player1 = 0
    player2 = 0
    player1wins = 0
    player2wins = 0
    rounds = 1
    while rounds != 6:
        print("Round " + str(rounds))
        player1  =dice_roll()
        player2 = dice_roll()
        print("player 1 roll :" + str(player1))
        print("player 2 roll :" + str(player2))

        if player1 ==player2:
            print("Draw")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("player 1 wins")
        else:
            player2wins = player2wins + 1
            print("player 2 wins")

        rounds = rounds + 1
    if player1wins == player2wins:
        print("the match is draw" )
    elif player1wins > player2wins:
        print("Player1 wins finally : "  + str(player1wins))
    else:
        print("player2 wins finally : " + str(player2wins))

def dice_roll():
    diceroll = random.randint(1,6)
    return  diceroll
main()
