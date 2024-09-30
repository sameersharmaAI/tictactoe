# Tic-Tac-Toe Game (Player vs Player) on Streamlit

## Overview
This is a simple Player vs Player Tic-Tac-Toe game built using Streamlit. The game allows two players to take turns, playing as "X" and "O" on a 3x3 grid. The game automatically detects wins or draws and provides the option to restart the game.

## Core Features
- **Player vs Player:** Two players can compete locally on the same machine.
- **Turn-based system:** The game alternates between Player X and Player O.
- **Win/Draw Detection:** The game automatically checks for a winner or a draw after each move.
- **Restart Option:** A button is provided to reset the game and start fresh.

## How to Run the Game
1. Clone the repository:
    ```bash
    git clone https://github.com/sameersharmaAI/tictactoe.git
    ```
2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. Open the browser and go to `http://localhost:8501` to play the game.

## Requirements
- Python 3.x
- Streamlit

You can install Streamlit by running:
```bash
pip install streamlit
