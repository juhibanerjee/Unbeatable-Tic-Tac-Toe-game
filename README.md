# Tic Tac Toe Game - Microsoft Mars Colonization Program 2020

## Inroduction
The main aim of the following project was to create an unbeatable Tic Tac Toe Game using Minimax algorithm and powered by AI.  

The following shows the [Tic Tac Toe game](https://tictactoe-juhi.herokuapp.com/index.html) (browser based web application) deployed using Heroku.


## Running the Application
### Web Application in Javascript
The web application has been written in Javascript. The game is designed for both 1 player and for 2 players. For the 1 player game, there are 3 difficulty levels (easy, medium and hard) and is powered by AI (via *Minimax Algorithm*).

This web application has been tested on - 
* Safari Version 13.1.2 (15609.3.5.1.3)
* Chrome Version 84.0.4147.89
* Firefox Version 78.0.2
* Microsoft Edge Version 44.18362.449.0
* Internet Explorer Version 11.959.18362.0

The following web page is designed for desktop view and has not been made responsive to mobile views yet.


### Backend Application in Python
The backend code for the following game is present in Python. This code works on the console and is not deployed. 


## Technical Details
* function evaluate (state) : The following function finds the score of the given move and returns it. 

* function gameOver(state, player) : The following function stores all the winning possibilities and returns true if any player has won.

* function gameOverAll(state) : This function calls the gameOver(state,player) function to see who has won - human/player1 or computer/player2.

* function emptyCells(state) : It stores the number of empty cells present after each move and returns it in the form of a list.

* function validMove(x,y) : Function to check whether any move given is a valid move or not. If board[x][y] is blank, then it returns true, else false.


