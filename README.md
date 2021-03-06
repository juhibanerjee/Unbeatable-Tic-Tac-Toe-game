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
The backend code for the following game is present in Python. This code works on the console and is not deployed. The program can be run by
```python src.py```.


## Technical Details
* **function evaluate (state)** : The following function finds the score of the given move and returns it. 

* **function gameOver(state, player)** : The following function stores all the winning possibilities and returns true if any player has won.

* **function gameOverAll(state)** : This function calls the gameOver(state,player) function to see who has won - human/player1 or computer/player2.

* **function emptyCells(state)** : It stores the number of empty cells present after each move and returns it in the form of a list.

* **function validMove(x,y)** : Function to check whether any move given is a valid move or not. If board[x][y] is blank, then it returns true, else false.

* **function setMove(x,y,player)** : If the validMove(x,y) is given by any player then it returns true, else false.

* **function minimax(state,depth,player)** : The Minimax algorithm (used only for 1 player) is similar to backtracking algorithm. It is generally used to find the    optimal solution or the optimal move of a player, assuming that the other player also plays optimally. The algorithm searches recursively  for the best move      that leads the MAX player to win. For each valid move, it plays alternatively (MAX and MIN) until it finds a terminal state.
   ![alt text](https://github.com/juhibanerjee/Unbeatable-Tic-Tac-Toe-game/blob/master/image/minimax.png?raw=true)
   ![alt text](https://github.com/juhibanerjee/Unbeatable-Tic-Tac-Toe-game/blob/master/image/minimax2.png?raw=true)
   
   In the following function both players start with their worst case. If the player is MAX then its score is -1000. If the player is MIN then its score is +1000.    The best move[-1,-1] is for the best row and best column. If the depth=0, then the board does not have any empty cell to play, or if any player wins then +1      will be returned for MAX and -1 for MIN. If it is a draw then it returns 0.The recursion part of the function - 
    * x contains the cell row index and y contains the cell column index
    * state[x][y] receives the MAX or MIN player
    * score = minimax(state, depth-1, -player) : state stores the current state of the board, depth-1 stores the index of the next step and -player keeps on             alternating MAX and MIN.
   The move placed on the board is undo and the row and column are stored. The current score is compared with the best score. For MAX player a bigger score will      be achieved while for MIN player a lower score will be achieved. At last, the best score is returned.

* **function aiTurn()** : This function works only for 1 player as well. The depth variable depends upon the difficulty level chosen by the player. if depth=1 then it is easy, depth=5 then it is medium and when depth=the length of the number of empty cells then it is hard/unbeatable. This function calls the minimax function when AI is to make a move.

* **function clickedCell(cell)** : This function is the main function of the program. If the user chooses '1 player' then first=Human and second=Computer. If the user chooses '2players' then first=Player 1 and second=Player 2. The functions are called accordingly and the game continues till the game gets over.

* **restartBnt(button)** : The function is for asking the user who will start first and to reset the screen for the next game.


## Deploying Website on Heroku
The game has been deployed using Heroku. The steps followed can be found [here](https://blog.teamtreehouse.com/deploy-static-site-heroku).

## References
* https://github.com/Cledersonbc/tic-tac-toe-minimax
* https://blog.teamtreehouse.com/deploy-static-site-heroku
* https://towardsdatascience.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d
