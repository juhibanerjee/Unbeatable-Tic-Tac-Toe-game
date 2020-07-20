/*Tic Tac Toe Game with 1 player and 2 players*/
var player1turn = true;
var board = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0],
];

var HUMAN_P1 = -1;
var COMP_P2 = +1;
var LEVEL = null;
var PLAYER = null;

/*Function to find the state and returning the score*/
function evalute(state) {
	var score = 0;
	if (gameOver(state, COMP_P2))
		score = +1;
	else if (gameOver(state, HUMAN_P1))
		score = -1;
	else
		score = 0;
	return score;
}

/* Function that stores all the winning possibilities*/
function gameOver(state, player) {
	var win_state = [
		[state[0][0], state[0][1], state[0][2]],
		[state[1][0], state[1][1], state[1][2]],
		[state[2][0], state[2][1], state[2][2]],
		[state[0][0], state[1][0], state[2][0]],
		[state[0][1], state[1][1], state[2][1]],
		[state[0][2], state[1][2], state[2][2]],
		[state[0][0], state[1][1], state[2][2]],
		[state[2][0], state[1][1], state[0][2]],
	];
	for (var i = 0; i < 8; i++) {
		var line = win_state[i];
		var filled = 0;
		for (var j = 0; j < 3; j++) {
			if (line[j] == player)
				filled++;
		}
		if (filled == 3)
			return true;
	}
	return false;
}

/* Function to see whether anybody has won*/
function gameOverAll(state) {
	return gameOver(state, HUMAN_P1) || gameOver(state, COMP_P2);
}

/*Function that returns the empty cells*/
function emptyCells(state) {
	var cells = [];
	for (var x = 0; x < 3; x++) {
		for (var y = 0; y < 3; y++) {
			if (state[x][y] == 0)
				cells.push([x, y]);
		}
	}
	return cells;
}

/* Function to check whether a move is a valid move*/
function validMove(x, y) {
	try {
		if (board[x][y] == 0)
			return true;
		else
			return false;
	}
	catch (e){
		return false;
	}
}

/* Function to set the move only if that move is a valid move */
function setMove(x, y, player) {
	if (validMove(x, y)) {
		board[x][y] = player;
		return true;
	}
	else
		return false;
}

/* The minimax algorithm for 1 player only */
function minimax(state, depth, player) {
	var best;

	if (player == COMP_P2)
		best = [-1, -1, -1000];
	else
		best = [-1, -1, +1000];

	if (depth == 0 || gameOverAll(state)) {
		var score = evalute(state);
		return [-1, -1, score];
	}

	emptyCells(state).forEach(function (cell) {
		var x = cell[0];
		var y = cell[1];
		state[x][y] = player;
		var score = minimax(state, depth - 1, -player);
		state[x][y] = 0;
		score[0] = x;
		score[1] = y;
		if (player == COMP_P2) {
			if (score[2] > best[2])
				best = score;
		}
		else {
			if (score[2] < best[2])
				best = score;
		}
	});

	return best;
}


/*Function to find where AI will place its move by calling the minimax algorithm*/
function aiTurn() {
	var x, y;
	var move;
	var cell;
	switch (LEVEL){
		case "1":
			depth = 1;
			break;
		case "5":
			depth = 5;
			break;
		case "10":
			depth = emptyCells(board).length;
			break;
	}

	if (emptyCells(board).length == 9) {
		x = parseInt(Math.random() * 3);
		y = parseInt(Math.random() * 3);
	}
	else {
		move = minimax(board, depth, COMP_P2);
		x = move[0];
		y = move[1];
	}

	if (setMove(x, y, COMP_P2)) {
		cell = document.getElementById(String(x) + String(y));
		cell.innerHTML = "O";
	}
}

/* The main function*/
function clickedCell(cell) {
	console.log(cell)
	var button = document.getElementById("btn-restart");
	button.disabled = true;
	var conditionToContinue = gameOverAll(board) == false && emptyCells(board).length > 0;

	if (PLAYER == "1player") {
		var first = "Human";
		var second = "Computer";
		if (conditionToContinue == true) {
			var x = cell.id.split("")[0];
			var y = cell.id.split("")[1];
			var move = setMove(x, y, HUMAN_P1);
			if (move == true) {
				cell.innerHTML = "X";
				if (conditionToContinue)
					aiTurn();
			}
		}
	}
	else{
		var first = "Player 1";
		var second = "Player 2";
		if (conditionToContinue == true) {
			var move1;
			var x1 = cell.id.split("")[0];
			var y1 = cell.id.split("")[1];
			if(player1turn == true){
				move1 = setMove(x1, y1, HUMAN_P1);
				if (move1 == true){
					cell.innerHTML = "X";
					player1turn = !player1turn;
				}
			}
			else{
				move1 = setMove(x1, y1, COMP_P2);
				if (move1 == true){
					cell.innerHTML = "O";
					player1turn = !player1turn;
				}
			}
		}
	}

	/*Game over check for computer if 1 player and p2 for 2 players*/
	if (gameOver(board, COMP_P2)) {
		var lines;
		var cell;
		var msg;

		if (board[0][0] == 1 && board[0][1] == 1 && board[0][2] == 1)
			lines = [[0, 0], [0, 1], [0, 2]];
		else if (board[1][0] == 1 && board[1][1] == 1 && board[1][2] == 1)
			lines = [[1, 0], [1, 1], [1, 2]];
		else if (board[2][0] == 1 && board[2][1] == 1 && board[2][2] == 1)
			lines = [[2, 0], [2, 1], [2, 2]];
		else if (board[0][0] == 1 && board[1][0] == 1 && board[2][0] == 1)
			lines = [[0, 0], [1, 0], [2, 0]];
		else if (board[0][1] == 1 && board[1][1] == 1 && board[2][1] == 1)
			lines = [[0, 1], [1, 1], [2, 1]];
		else if (board[0][2] == 1 && board[1][2] == 1 && board[2][2] == 1)
			lines = [[0, 2], [1, 2], [2, 2]];
		else if (board[0][0] == 1 && board[1][1] == 1 && board[2][2] == 1)
			lines = [[0, 0], [1, 1], [2, 2]];
		else if (board[2][0] == 1 && board[1][1] == 1 && board[0][2] == 1)
			lines = [[2, 0], [1, 1], [0, 2]];

		for (var i = 0; i < lines.length; i++) {
			cell = document.getElementById(String(lines[i][0]) + String(lines[i][1]));
			cell.style.color = "red";
		}

		msg = document.getElementById("message");
		msg.innerHTML =  second + " wins!";
	}
	/*Game over check for human if 1 player and p1 for 2 players*/
	if (gameOver(board, HUMAN_P1)) {
		var lines;
		var cell;
		var msg;

		if (board[0][0] == -1 && board[0][1] == -1 && board[0][2] == -1)
			lines = [[0, 0], [0, 1], [0, 2]];
		else if (board[1][0] == -1 && board[1][1] == -1 && board[1][2] == -1)
			lines = [[1, 0], [1, 1], [1, 2]];
		else if (board[2][0] == -1 && board[2][1] == -1 && board[2][2] == -1)
			lines = [[2, 0], [2, 1], [2, 2]];
		else if (board[0][0] == -1 && board[1][0] == -1 && board[2][0] == -1)
			lines = [[0, 0], [1, 0], [2, 0]];
		else if (board[0][1] == -1 && board[1][1] == -1 && board[2][1] == -1)
			lines = [[0, 1], [1, 1], [2, 1]];
		else if (board[0][2] == -1 && board[1][2] == -1 && board[2][2] == -1)
			lines = [[0, 2], [1, 2], [2, 2]];
		else if (board[0][0] == -1 && board[1][1] == -1 && board[2][2] == -1)
			lines = [[0, 0], [1, 1], [2, 2]];
		else if (board[2][0] == -1 && board[1][1] == -1 && board[0][2] == -1)
			lines = [[2, 0], [1, 1], [0, 2]];

		for (var i = 0; i < lines.length; i++) {
			cell = document.getElementById(String(lines[i][0]) + String(lines[i][1]));
			cell.style.color = "green";
		}

		msg = document.getElementById("message");
		msg.innerHTML = first + " wins!";
	}
	if (emptyCells(board).length == 0 && !gameOverAll(board)) {
		var msg = document.getElementById("message");
		msg.innerHTML = "It's a draw!";
	}
	if (gameOverAll(board) == true || emptyCells(board).length == 0) {
		button.value = "Restart";
		button.disabled = false;
	}
}

/* Function to restart the game*/
function restartBnt(button) {
	if (button.value == "Computer starts") {
		aiTurn();
		button.disabled = true;
	}
	if (button.value == "Player 2 starts") {
		player1turn = false;
		button.disabled = true;
	}
	else if (button.value == "Restart") {
		var htmlBoard;
		var msg;
		for (var x = 0; x < 3; x++) {
			for (var y = 0; y < 3; y++) {
				board[x][y] = 0;
				htmlBoard = document.getElementById(String(x) + String(y));
				htmlBoard.style.color = "#444";
				htmlBoard.innerHTML = "";
			}
		}
		msg = document.getElementById("message");
		msg.innerHTML = "";
		msg1 = document.getElementById("player_msg");
		msg1.innerHTML =  "";
		$(".players").attr("disabled", false).removeClass("active-player");
		$(".diff-level").attr("disabled", false).removeClass("active");
		$("#diff-buttons").hide();
		$("#tab-tic-tac-toe").hide();
		$("#btn-restart").hide();
		player1turn = true;
	}
}
/*If the difficulty level buttons are clicked*/
$(".diff-level").click(function(){
	LEVEL = $(this).attr("id").split("-")[1];
	$(".diff-level").attr("disabled", true).removeClass("active");
	$(this).addClass("active");
	$("#tab-tic-tac-toe").show();
	document.getElementById("btn-restart").value = "Computer starts";
	$("#btn-restart").show();
	msg = document.getElementById("player_msg");
	msg.innerHTML =  "Human: X"+"<br \n>"+"Computer: O";

})

$("#2players").click(function(){
	$("#diff-buttons").hide();
	$("#tab-tic-tac-toe").show();
	document.getElementById("btn-restart").value = "Player 2 starts";
	$("#btn-restart").show();
	msg = document.getElementById("player_msg");
	msg.innerHTML =  "Player 1: X"+"<br \n>"+"Player 2: O";
})

$("#1player").click(function(){
	$("#diff-buttons").show();
})

$(".players").click(function(){
	PLAYER = $(this).attr("id");
	$(".players").attr("disabled", true).removeClass("active-player");
	$(this).addClass("active-player");
})

$("#diff-buttons").hide();
$("#tab-tic-tac-toe").hide();
$("#btn-restart").hide();
