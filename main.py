import tkinter as tk
from tkinter import messagebox

def check_winner(board, player):
    return (board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player)

def on_click(btn, pos):
    global counter, player
    if btn["text"] == " ":
        btn["text"] = player
        board[pos] = player
        counter += 1
        if counter >= 5:
            if check_winner(board, player):
                messagebox.showinfo("Гру закінчено", f"Гравець {player} переміг!")
                reset_game()
                # root.destroy()
                return
        if counter == 9:
            messagebox.showinfo("Гру закінчено", "Перемогла дружба!")
            reset_game()
            # root.destroy()
            return
        player = "X" if player == "O" else "O"
        label.config(text=f"{player} черга")
        if counter >= 3:
            if check_winner(board, player):
                messagebox.showinfo("Гру закінчено", f"Гравець {player} переміг!")
                reset_game()
                # root.destroy()
                return

def reset_game():
    global counter, player, buttons, board
    counter = 0
    player = "X"
    label.config(text=f"{player} черга")
    board = [" "] * 9
    for btn in buttons:
        btn["text"] = " "

counter = 0
player = "X"
board = [" "] * 9
root = tk.Tk()
root.title("Хрестики нулики")
label = tk.Label(root, text=f"{player} черга", font=("Arial", 16))
label.grid(row=0, column=0, columnspan=3)

buttons = []
for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text=" ", font=("Arial", 16), width=5, height=2)
        btn.grid(row=i+1, column=j, padx=5, pady=5)
        btn.config(command=lambda btn=btn, pos=i*3+j: on_click(btn, pos))
        buttons.append(btn)

root.mainloop()
