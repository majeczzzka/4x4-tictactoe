```markdown
# Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

## Overview

This project implements a **4x4 Tic-Tac-Toe** game in Python. The AI opponent uses the **Minimax algorithm with Alpha-Beta pruning** for optimized decision-making. Players can compete against the AI or run automated AI vs AI simulations to analyze performance.

## Features

- ✅ **4x4 Tic-Tac-Toe board**  
- ✅ **Minimax algorithm** with Alpha-Beta pruning for optimal AI decision-making  
- ✅ **Human vs AI** mode  
- ✅ **AI vs AI** simulation mode for performance analysis  
- ✅ **Game state evaluations** including win detection, draw conditions, and move validation  
- ✅ **Automated test cases** to ensure game functionality  

## Installation

Ensure you have **Python 3.6+** installed, then clone the repository:

```bash
# Clone the repository
git clone <repository_url>
cd <repository_folder>

# Run the game
python tic_tac_toe.py
```

## How to Play

```bash
### Human vs AI Mode
1. The game starts with an empty **4x4** board.
2. The **human player (X)** enters a move in the format **row,col** (e.g., `1,2`).
3. The **AI (O)** makes its move based on the **Minimax algorithm**.
4. The game continues until a **win** or a **draw** occurs.

### AI vs AI Simulation
Run AI vs AI games to analyze performance:

python tic_tac_toe.py --simulate

The program will print game results and win statistics.
```

## Code Structure

```bash
| Function | Description |
|----------|------------|
| `print_board(board)` | Displays the current state of the board |
| `check(board)` | Determines if there is a winner or a draw |
| `winningPlayer(board, player)` | Checks if a player has won |
| `boardFull(board)` | Checks if the board is full |
| `strategy(board, depth, alpha, beta, player, max_depth)` | Implements Minimax with Alpha-Beta pruning |
| `makeMove(board, player, mode, max_depth)` | Handles AI and human player moves |
| `game_play()` | Runs the main game loop |
| `run_simulations(num_games)` | Runs multiple AI vs AI simulations |
```

## Running Tests

```bash
# To verify the game logic, run unit tests:
python -m unittest tic_tac_toe.py
```

## Example Simulation Output

```bash
Simulation Results: {'X Wins': 20, 'O Wins': 25, 'Draws': 5}
X Win Rate: 40.00%
O Win Rate: 50.00%
Draw Rate: 10.00%
```

## Future Improvements

```bash
🚀 Expand to a configurable board size
🎨 Implement a GUI version
🧠 Enhance AI difficulty settings
```

