import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

st.title("🎮 Tic Tac Toe")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "current_player" not in st.session_state:
    st.session_state.current_player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

# Winning combinations
winning_combos = [
    [0,1,2], [3,4,5], [6,7,8],  # rows
    [0,3,6], [1,4,7], [2,5,8],  # cols
    [0,4,8], [2,4,6]            # diagonals
]

def check_winner():
    board = st.session_state.board
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def make_move(i):
    if st.session_state.board[i] == "" and not st.session_state.winner:
        st.session_state.board[i] = st.session_state.current_player
        st.session_state.winner = check_winner()
        if not st.session_state.winner:
            st.session_state.current_player = (
                "O" if st.session_state.current_player == "X" else "X"
            )

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

# Display board
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        st.button(
            st.session_state.board[i] if st.session_state.board[i] else " ",
            key=i,
            on_click=make_move,
            args=(i,),
            use_container_width=True
        )

# Game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.warning("It's a draw!")
    else:
        st.success(f"Player {st.session_state.winner} wins! 🎉")
else:
    st.info(f"Current turn: {st.session_state.current_player}")

# Reset button
st.button("🔄 Reset Game", on_click=reset_game)