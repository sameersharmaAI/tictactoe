import streamlit as st
import numpy as np

# Initialize game board
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

# Initialize turn (1 for player X, -1 for player O)
if 'turn' not in st.session_state:
    st.session_state.turn = 1

# Reset game function
def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.turn = 1
    st.session_state.winner = None

# Check for a winner
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if abs(sum(board[i, :])) == 3:  # Rows
            return board[i, 0]
        if abs(sum(board[:, i])) == 3:  # Columns
            return board[0, i]
    
    if abs(sum([board[i, i] for i in range(3)])) == 3:  # Main diagonal
        return board[0, 0]
    if abs(sum([board[i, 2-i] for i in range(3)])) == 3:  # Anti-diagonal
        return board[0, 2]
    
    return None

# Game logic
st.title("Tic-Tac-Toe (Player vs Player)")

# Render the game board as buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.session_state.board[i, j] == 0:
                if st.button(" ", key=f"{i}-{j}"):
                    st.session_state.board[i, j] = st.session_state.turn
                    st.session_state.turn *= -1
            elif st.session_state.board[i, j] == 1:
                st.button("X", key=f"{i}-{j}", disabled=True)
            elif st.session_state.board[i, j] == -1:
                st.button("O", key=f"{i}-{j}", disabled=True)

# Check for a winner
winner = check_winner(st.session_state.board)

if winner:
    st.success(f"Player {'X' if winner == 1 else 'O'} wins!")
    st.button("Restart Game", on_click=reset_game)
elif not (st.session_state.board == 0).any():  # Check for a draw
    st.info("It's a draw!")
    st.button("Restart Game", on_click=reset_game)
else:
    st.info(f"Player {'X' if st.session_state.turn == 1 else 'O'}'s turn.")

# Button to reset game at any point
st.button("Reset Game", on_click=reset_game)
