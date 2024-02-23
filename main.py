import tkinter as tk
from tkinter import messagebox

def button_click(btn):
    global turn, player
    if turn:
        btn.config(text="X", state='disabled')
        turn = 0
        player.config(text="Jogador O")
    else:
        btn.config(text="O", state='disabled')
        turn = 1
        player.config(text="Jogador X")
    check_winner()

def check_winner():
    for i in range(3):
        if buttons[i*3]['text'] == buttons[i*3+1]['text'] == buttons[i*3+2]['text'] != '':
            winner_found(buttons[i*3]['text'])
            return

    for i in range(3):
        if buttons[i]['text'] == buttons[i+3]['text'] == buttons[i+6]['text'] != '':
            winner_found(buttons[i]['text'])
            return

    if buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text'] != '':
        winner_found(buttons[0]['text'])
        return
    if buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text'] != '':
        winner_found(buttons[2]['text'])
        return

    if all(button['text'] != '' for button in buttons):
        messagebox.showinfo("Jogo da Velha", "Empate!")
        reset_game()

def winner_found(winner):
    messagebox.showinfo("Jogo da Velha", f"Player {winner} venceu!")
    reset_game()

def reset_game():
    global turn
    for button in buttons:
        button.config(text="", state='normal')
        turn = 1
        player.config(text="Jogador X")

root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("300x400")

turn = 1
buttons = []
x_start, y_start = 10, 10
button_width, button_height = 10, 5
rows, cols = 3, 3

for i in range(rows):
    for j in range(cols):
        button = tk.Button(root, width=button_width, height=button_height)
        button.place(x=x_start + j * 100, y=y_start + i * 100)
        buttons.append(button)

        button.config(command=lambda current_button=button: button_click(current_button))

player = tk.Label(root, text="Jogador: X")
player.place(x=10, y=350)

reset = tk.Button(root, text="Reset", command=reset_game)
reset.place(x=250, y=350)

root.mainloop()
