from math import inf
import random
EMPTY = 0
X_PLAYER = 1
O_PLAYER = 2


def print_board(board): #function to print the board
    values = {EMPTY: ' ', X_PLAYER: 'X', O_PLAYER: 'O'}
    for i in range(len(board)):
        print('-----------------')
        for j in range(len(board[i])):
            print(f'| {values[board[i][j]]} ', end='')
        print('|')
    print('-----------------')

def check(board): #function to check the board
    if winningPlayer(board, X_PLAYER):
        return 1
    elif winningPlayer(board, O_PLAYER):
        return -1
    elif boardFull(board):
        return 0
    else:
        return None

def terminal_test(board): #function to check if the game is over
    return check(board) is not None

def winningPlayer(board, player): #function to check if a player has won
    conditions = [
    # Rows
    [board[0][0], board[0][1], board[0][2], board[0][3]],
    [board[1][0], board[1][1], board[1][2], board[1][3]],
    [board[2][0], board[2][1], board[2][2], board[2][3]],
    [board[3][0], board[3][1], board[3][2], board[3][3]],
    # Columns
    [board[0][0], board[1][0], board[2][0], board[3][0]],
    [board[0][1], board[1][1], board[2][1], board[3][1]],
    [board[0][2], board[1][2], board[2][2], board[3][2]],
    [board[0][3], board[1][3], board[2][3], board[3][3]],
    # Diagonals
    [board[0][0], board[1][1], board[2][2], board[3][3]],
    [board[0][3], board[1][2], board[2][1], board[3][0]]
]


    if [player, player, player, player] in conditions:
        return True

    return False

def boardFull(board): #function to check if the board is full
    for row in board:
        if EMPTY in row:
            return False
    return True

def blanks(board): #function to check the empty cells in the board
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])
    return blank

def setMove(board, x, y, player): #function to set the move
    board[x][y] = player

def playerMove(board): #function to get the player's move
    e = True
    while e:
        try:
            user_input = input(f"Player 1 enter your move (row,col) between 1 and {len(board)}: ")
            row, col = map(int, user_input.split(','))
            if row < 1 or row > len(board) or col < 1 or col > len(board):
                print(f'Invalid Move! Row and column values should be between 1 and {len(board)}.')
            elif board[row - 1][col - 1] != EMPTY:
                print('Invalid Move! This cell is not empty. Try again.')
            else:
                setMove(board, row - 1, col - 1, X_PLAYER)
                print_board(board)
                e = False
        except (ValueError, IndexError):
            print('Invalid input format. Please enter row,col e.g. 1,2.')
            
def getScore(board): #function to get the score of the game
    result = check(board)
    if result is None:
        return 0
    else:
        return result

def strategy(board, depth, alpha, beta, player, max_depth): #function to implement the strategy
    if terminal_test(board) or depth >= max_depth:
        return [None, None, getScore(board)]
    
    best_move = [None, None]
    if player == X_PLAYER:
        max_eval = float('-inf')
        for cell in blanks(board):
            setMove(board, cell[0], cell[1], player)
            score = strategy(board, depth + 1, alpha, beta, O_PLAYER, max_depth)
            setMove(board, cell[0], cell[1], EMPTY)  # Revert move

            if score[2] > max_eval:
                max_eval = score[2]
                best_move = cell
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        return best_move + [max_eval] if best_move else [None, None, max_eval]
    else:
        min_eval = float('inf')
        for cell in blanks(board):
            setMove(board, cell[0], cell[1], player)
            score = strategy(board, depth + 1, alpha, beta, X_PLAYER, max_depth)
            setMove(board, cell[0], cell[1], EMPTY)  # Revert move

            if score[2] < min_eval:
                min_eval = score[2]
                best_move = cell
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return best_move + [min_eval] if best_move else [None, None, min_eval]


def makeMove(board, player, mode, max_depth): #function to make the move
    if mode == 1:  # Player's turn
        if player == X_PLAYER:
            playerMove(board)
        else:
            result = strategy(board, 0, -inf, inf, O_PLAYER, max_depth)
            if result[0] is not None and result[1] is not None:
                setMove(board, result[0], result[1], O_PLAYER)
            print_board(board)  # Print the board after setting AI's move
    else:  # AI's turn
        if player == X_PLAYER:
            result = strategy(board, 0, -inf, inf, X_PLAYER, max_depth)
            if result[0] is not None and result[1] is not None:
                setMove(board, result[0], result[1], X_PLAYER)
            print_board(board)  # Print the board after setting AI's move
        else:
            print("y")
            result = strategy(board, 0, -inf, inf, O_PLAYER, max_depth)
            print("x")
            if result[0] is not None and result[1] is not None:
                setMove(board, result[0], result[1], O_PLAYER)
            print("c")
            print_board(board)  # Print the board after setting AI's move

def game_play(): #function to play the game
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    initial_depth = 3
    current_player = X_PLAYER
    while not (boardFull(board) or winningPlayer(board, X_PLAYER) or winningPlayer(board, O_PLAYER)):
        max_depth = 2
        makeMove(board, current_player, 1 if current_player == X_PLAYER else 2, max_depth)
        current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER

    if winningPlayer(board, X_PLAYER):
        print("Player 1 wins.")
    elif winningPlayer(board, O_PLAYER):
        print("AI wins.")
    else:
        print("It's a draw.")


print("=================================================")
print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
print("=================================================")
#game_play()

#test cases
def test_initial_board_empty(): #function to test if the board is empty
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    for row in board:
        assert all(cell == EMPTY for cell in row), "Error: Board should be initialized with all cells empty."

def test_invalid_moves(): #function to test invalid moves
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    setMove(board, 0, 0, X_PLAYER)  # Set X in the top-left corner
    try:
        setMove(board, 0, 0, O_PLAYER)  # Try setting O in the same spot
        assert False, "Error: Should not allow placing a move where a cell is already occupied."
    except:
        pass  # Expected to fail

def test_player_win(): #function to test if the player has won
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    for i in range(4):
        setMove(board, 0, i, X_PLAYER)
    assert winningPlayer(board, X_PLAYER), "Error: X should be winning."

def test_draw_condition(): #function to test the draw condition
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    draw_setup = [
        [X_PLAYER, O_PLAYER, X_PLAYER, O_PLAYER],
        [O_PLAYER, X_PLAYER, O_PLAYER, X_PLAYER],
        [O_PLAYER, X_PLAYER, O_PLAYER, X_PLAYER],
        [X_PLAYER, O_PLAYER, X_PLAYER, O_PLAYER]
    ]
    
    for i in range(board_size):
        for j in range(board_size):
            board[i][j] = draw_setup[i][j]
    

    # Ensure the board is full and no player has won
    assert boardFull(board), "Error: The board should be full."
    assert not winningPlayer(board, X_PLAYER), "Error: X should not be winning."
    assert not winningPlayer(board, O_PLAYER), "Error: O should not be winning."
    assert check(board) == 0, "Error: The game should be a draw."


def test_ai_move(): #function to test the AI move
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    setMove(board, 0, 0, X_PLAYER)
    setMove(board, 0, 1, X_PLAYER)
    setMove(board, 0, 2, X_PLAYER)
    makeMove(board, O_PLAYER, 2, 3)  # AI should block X at (0, 3)
    assert board[0][3] == O_PLAYER, "Error: AI should have placed O at (0, 2) to block X."

# Running the tests
if __name__ == "__main__":
    test_initial_board_empty()
    test_invalid_moves()
    test_player_win()
    test_draw_condition()
    test_ai_move()
    print("All tests passed!")

def randomHumanMove(board, player):
    print("Player 1 enter your move (row,col) between 1 and 4: ")
    empty_cells = blanks(board)
    if empty_cells:
        x, y = random.choice(empty_cells)
        setMove(board, x, y, player)  # Player is X_PLAYER, making random moves

def game_play_simulation():
    # Initializing a 4x4 board
    board_size = 4
    board = [[EMPTY] * board_size for _ in range(board_size)]
    current_player = X_PLAYER  # Starting player, can toggle to O_PLAYER if AI should start

    while not (boardFull(board) or winningPlayer(board, X_PLAYER) or winningPlayer(board, O_PLAYER)):
        if current_player == X_PLAYER:
            # Simulated human's move, random for X_PLAYER
            randomHumanMove(board, current_player)
        else:
            # AI's move using strategic function, for O_PLAYER
            result = strategy(board, 0, -inf, inf, current_player, 4)  
            if result[0] is not None and result[1] is not None:
                setMove(board, result[0], result[1], current_player)

        print_board(board)
        current_player = O_PLAYER if current_player == X_PLAYER else X_PLAYER  # Toggle players

    return check(board)

# Run multiple simulations
def run_simulations(num_games):
    results = {"X Wins": 0, "O Wins": 0, "Draws": 0}
    for _ in range(num_games):
        result = game_play_simulation()  # Ensure this function is correctly handling 4x4
        if result == 1:
            results["X Wins"] += 1
        elif result == -1:
            results["O Wins"] += 1
        else:
            results["Draws"] += 1

    total_games = sum(results.values())
    x_win_rate = (results['X Wins'] / total_games) * 100
    o_win_rate = (results['O Wins'] / total_games) * 100
    draw_rate = (results['Draws'] / total_games) * 100

    print(f"Simulation Results: {results}")
    print(f"X Win Rate: {x_win_rate:.2f}%")
    print(f"O Win Rate: {o_win_rate:.2f}%")
    print(f"Draw Rate: {draw_rate:.2f}%")

    return results

# Example of running 100 game simulations
if __name__ == "__main__":  
    simulation_results = run_simulations(50)
    print("Simulation Results: ", simulation_results)





