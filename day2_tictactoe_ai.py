import tkinter as tk
import random

# ---------------- COLORS (PASTEL THEME) ----------------
BG_COLOR = "#f7f7fb"
CELL_COLOR = "#e3f2fd"
HUMAN_COLOR = "#ffd6e0"
AI_COLOR = "#d0f0c0"
WIN_COLOR = "#b5ead7"
TEXT_COLOR = "#444"

# ---------------- GAME VARIABLES ----------------
board = [""] * 9
human = "X"
ai = "O"
current_player = "X"
game_over = False

human_score = 0
ai_score = 0

win_combos = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# ---------------- MINIMAX ----------------
def check_winner(b):
    for combo in win_combos:
        a,b1,c = combo
        if b[a] == b[b1] == b[c] and b[a] != "":
            return b[a]
    return None

def is_draw(b):
    return "" not in b

def minimax(b, is_max):
    winner = check_winner(b)

    if winner == ai:
        return 1
    elif winner == human:
        return -1
    elif is_draw(b):
        return 0

    if is_max:
        best = -1000
        for i in range(9):
            if b[i] == "":
                b[i] = ai
                score = minimax(b, False)
                b[i] = ""
                best = max(best, score)
        return best
    else:
        best = 1000
        for i in range(9):
            if b[i] == "":
                b[i] = human
                score = minimax(b, True)
                b[i] = ""
                best = min(best, score)
        return best

def best_move():
    best_score = -1000
    move = None

    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------------- UI FUNCTIONS ----------------
def on_click(i):
    global current_player, game_over

    if board[i] != "" or game_over:
        return

    if current_player == human:
        board[i] = human
        buttons[i]["text"] = human
        buttons[i]["bg"] = HUMAN_COLOR
        current_player = ai
        update()

        if not game_over:
            root.after(300, ai_turn)

def ai_turn():
    global current_player

    move = best_move()
    if move is not None:
        board[move] = ai
        buttons[move]["text"] = ai
        buttons[move]["bg"] = AI_COLOR
        current_player = human
        update()

def update():
    global game_over, human_score, ai_score

    winner = check_winner(board)

    if winner:
        game_over = True
        highlight_winner(winner)

        if winner == human:
            status_label.config(text="You Win!")
            human_score += 1
        else:
            status_label.config(text="AI Wins!")
            ai_score += 1

        update_score()
        return

    if is_draw(board):
        game_over = True
        status_label.config(text="Draw!")
        return

    status_label.config(
        text="Your Turn" if current_player == human else "AI Thinking..."
    )

def highlight_winner(player):
    for combo in win_combos:
        a,b,c = combo
        if board[a] == board[b] == board[c] == player:
            buttons[a].config(bg=WIN_COLOR)
            buttons[b].config(bg=WIN_COLOR)
            buttons[c].config(bg=WIN_COLOR)

def restart():
    global board, game_over, current_player

    board = [""] * 9
    game_over = False
    current_player = "X"

    for btn in buttons:
        btn.config(text="", bg=CELL_COLOR)

    status_label.config(text="Your Turn" if human == "X" else "AI Thinking...")

    if human != "X":
        root.after(300, ai_turn)

def update_score():
    score_label.config(text=f"You: {human_score} | AI: {ai_score}")

def set_player(choice):
    global human, ai
    human = choice
    ai = "O" if choice == "X" else "X"
    restart()

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Tic Tac Toe AI")
root.configure(bg=BG_COLOR)

status_label = tk.Label(root, text="Choose X or O", font=("Arial", 14), bg=BG_COLOR, fg=TEXT_COLOR)
status_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                    bg=CELL_COLOR, fg=TEXT_COLOR,
                    command=lambda i=i: on_click(i))
    btn.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
    buttons.append(btn)

tk.Button(root, text="Play as X", bg="#dcedc1", command=lambda: set_player("X")).grid(row=4, column=0, pady=10)
tk.Button(root, text="Play as O", bg="#c7ceea", command=lambda: set_player("O")).grid(row=4, column=2)

tk.Button(root, text="Restart", bg="#ffe0ac", command=restart).grid(row=5, column=0, columnspan=3, pady=5)

score_label = tk.Label(root, text="You: 0 | AI: 0", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR)
score_label.grid(row=6, column=0, columnspan=3, pady=10)

root.mainloop()
