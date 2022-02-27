import random
import string

player1 = ["rock", "paper", "scissors"]
player2 = ["rock", "paper", "scissors"]




def play(games):
    for i in range(games):
        p1_move = random.choice(player1)
        p2_move = random.choice(player2)
        print(p1_move)
        print(p2_move)

        if p1_move == p2_move:
            print ("draw")
        else:
            if (p1_move == "rock" and p2_move == "paper") or (p1_move == "scissors" and p2_move == "rock") or (p1_move == "paper" and p2_move == "scissors"):
                print ("Player2 wins")
            else:
                print("Player1 wins")
            
play(10)    