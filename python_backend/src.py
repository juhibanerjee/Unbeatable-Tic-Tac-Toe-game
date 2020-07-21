#importing the player1 and player2 programs
import player2
import player1

# Taking input in the console - 1 for 'player1' and 2 for 'player2'
n = (int(input("Press '1' for one player. Press '2' for two players: ")))
if(n == 2):
    player2.main() #main function of player2 is called
elif(n==1):
    player1.main() #main function of player1 is called