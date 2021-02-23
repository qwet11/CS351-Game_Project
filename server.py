# Function to print Tic Tac Toe
def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Function to check if any player has won
def check_win(player_pos, cur_player):
 
    # All possible winning combinations
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 
# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Function for a single game of Tic Tac Toe
def single_game(cur_player):
 
    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
     
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
     
    # Game Loop for a single game of Tic Tac Toe
    while True:
        print_tic_tac_toe(values)
         
        # Try exception block for MOVE input
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue
 
        # Sanity check for MOVE inout
        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue
 
        # Check if the box is not occupied already
        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue
 
        # Update game information
 
        # Updating grid status 
        values[move-1] = cur_player
 
        # Updating player positions
        player_pos[cur_player].append(move)
 
        # Function call for checking win
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Player ", cur_player, " has won the game!!")     
            print("\n")
            return cur_player
 
        # Function call for checking draw game
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'
 
        # Switch player moves
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
from socket import *

# Server IP Address and Port
HOST = "18.219.39.168"
PORT = 1200
BUFFER_SIZE = 1024

# Setting up our socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen(2)

while True:
    try:
        # Establish connection with client 1
        print("Waiting for player 1...")
        connectionSocket1, connectionAddress1 = serverSocket.accept()
        print("Player 1 connected successful!\n")
        
        # Establish connection with client 2
        print("Waiting for player 2...")
        connectionSocket2, connectionAddress2 = serverSocket.accept()
        print("Player 2 connected successfully!\n")
        
        # Get players names
        player1 = connectionSocket1.recv(BUFFER_SIZE).decode()
        player2 = connectionSocket2.recv(BUFFER_SIZE).decode()
        
        # Stores the current player
        cur_player = player1
        
        # Stores the choice of players 
        player_choice = {"X" : "", "O" : ""}
        
        # Stores the options 
        options = ["X", "O"]
        
        # Stores the scoreboard
        score_board = {player1 : 0, player2: 0}
        
        # Send current scoreboard
        """
        connectionSocket1.sendall(print_scoreboard(score_board).encode())
        connectionSocket2.sendall(print_scoreboard(score_board).encode())
        """
        
        # Game Loop for a series of Tic Tac Toe
        # The loop runs until the players quit 
        while True:
     
            # Player choice Menu
            if (cur_player == player1):
                currentState = "Turn to choose for" + cur_player + "\n"
                                "Enter 1 for X \n" +
                                "Enter 2 for O \n" +
                                "Enter 3 to Quit \n"
                                
                # Try exception for CHOICE input
                while True:
                    connectionSocket1.sendall(currentState.encode())
                    choice = int(connectionSocket1.recv(BUFFER_SIZE).decode())
                    if choice >= 1 and choice <= 3:
                        break
                    else 
                        # ERROR MESSAGE
         
                # Conditions for player choice  
                if choice == 1:
                    player_choice['X'] = cur_player
                    if cur_player == player1:
                        player_choice['O'] = player2
                    else:
                        player_choice['O'] = player1
         
                elif choice == 2:
                    player_choice['O'] = cur_player
                    if cur_player == player1:
                        player_choice['X'] = player2
                    else:
                        player_choice['X'] = player1
                 
                elif choice == 3:
                    # TBD                    
                    """
                    print("Final Scores")
                    print_scoreboard(score_board)
                    break  
                    """
         
                # Stores the winner in a single game of Tic Tac Toe
                winner = single_game(options[choice-1])
                 
                # Edits the scoreboard according to the winner
                if winner != 'D' :
                    player_won = player_choice[winner]
                    score_board[player_won] = score_board[player_won] + 1
         
                connectionSocket1.sendall(print_scoreboard(score_board).encode())
                connectionSocket2.sendall(print_scoreboard(score_board).encode())
                # Switch player who chooses X or O
                if cur_player == player1:
                    cur_player = player2
                else:
                    cur_player = player1
            else:
                currentState = "Turn to choose for" + cur_player + "\n"
                                "Enter 1 for X \n" +
                                "Enter 2 for O \n" +
                                "Enter 3 to Quit \n"
                                
                # Try exception for CHOICE input
                while True:
                    connectionSocket2.sendall(currentState.encode())
                    choice = int(connectionSocket2.recv(BUFFER_SIZE).decode())
                    if choice >= 1 and choice <= 3:
                        break
                    else 
                        # ERROR MESSAGE
         
                # Conditions for player choice  
                if choice == 1:
                    player_choice['X'] = cur_player
                    if cur_player == player1:
                        player_choice['O'] = player2
                    else:
                        player_choice['O'] = player1
         
                elif choice == 2:
                    player_choice['O'] = cur_player
                    if cur_player == player1:
                        player_choice['X'] = player2
                    else:
                        player_choice['X'] = player1
                 
                elif choice == 3:
                    # TBD                    
                    """
                    print("Final Scores")
                    print_scoreboard(score_board)
                    break  
                    """
         
                # Stores the winner in a single game of Tic Tac Toe
                winner = single_game(options[choice-1])
                 
                # Edits the scoreboard according to the winner
                if winner != 'D' :
                    player_won = player_choice[winner]
                    score_board[player_won] = score_board[player_won] + 1
         
                connectionSocket1.sendall(print_scoreboard(score_board).encode())
                connectionSocket2.sendall(print_scoreboard(score_board).encode())
                # Switch player who chooses X or O
                if cur_player == player1:
                    cur_player = player2
                else:
                    cur_player = player1
    except Exception:
        print("Error!")
        print(Exception + "\n")
    finally:
        # Close connection with client
        connectionSocket.close()
        print("Connection successfully terminated!\n")
        

