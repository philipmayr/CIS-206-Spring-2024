
# Reference: Tic Tac Toe Game - Python Tkinter GUI Tutorial #113
#            https://www.youtube.com/watch?v=xx0qmpuA-vM

# import tkinter lib
from tkinter import *
# import messagebox module
from tkinter import messagebox

# create instance of TK, init. interpreter, and create root window
root = Tk()
# disable resizing of root window (width or height)
root.resizable(False, False)
# set root window title
root.title("Noughts & Crosses")

# set o to mathematical double-struck capital o character (U+1D546)
o = '𝕆'
# set x to mathematical double-struck capital x character (U+1D54F)
x = '𝕏'

# set hex color code value for olive
olive = "#4B7132"
# set hex color code value for amaranth
amaranth = "#71324B"
# set hex color code value for white
white = "#ffffff"

# initialize or reset game board
def init_game():
    # declare 9 global button variabes
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    # declare global clicked and count variables
    global clicked, count

    # init. clicked flag to true for x starts first
    clicked = True
    # init. button click count to 0
    count = 0

    # init. button properties and command func.
    b1 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    # init. button properties and command func.
    b4 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    # init. button properties and command func.
    b7 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # place buttons in grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    # place buttons in grid
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    # place buttons in grid
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def disable_buttons():
    # set button state to disabled for all buttons
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def check_game_state():
    # declare global winner flag
    global winner
    # init. winner flag to false
    winner = False

    # check win combinations for x
    if b1["text"] == x and b2["text"] == x and b3["text"] == x:
        b1.config(bg=amaranth, fg=white)
        b2.config(bg=amaranth, fg=white)
        b3.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b4["text"] == x and b5["text"] == x and b6["text"] == x:
        b4.config(bg=amaranth, fg=white)
        b5.config(bg=amaranth, fg=white)
        b6.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b7["text"] == x and b8["text"] == x and b9["text"] == x:
        b7.config(bg=amaranth, fg=white)
        b8.config(bg=amaranth, fg=white)
        b9.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b1["text"] == x and b4["text"] == x and b7["text"] == x:
        b1.config(bg=amaranth, fg=white)
        b4.config(bg=amaranth, fg=white)
        b7.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b2["text"] == x and b5["text"] == x and b8["text"] == x:
        b2.config(bg=amaranth, fg=white)
        b5.config(bg=amaranth, fg=white)
        b8.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b3["text"] == x and b6["text"] == x and b9["text"] == x:
        b3.config(bg=amaranth, fg=white)
        b6.config(bg=amaranth, fg=white)
        b9.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b1["text"] == x and b5["text"] == x and b9["text"] == x:
        b1.config(bg=amaranth, fg=white)
        b5.config(bg=amaranth, fg=white)
        b9.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    elif b3["text"] == x and b5["text"] == x and b7["text"] == x:
        b3.config(bg=amaranth, fg=white)
        b5.config(bg=amaranth, fg=white)
        b7.config(bg=amaranth, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "X Wins!")
        disable_buttons()
    # check win combinations for o
    elif b1["text"] == o and b2["text"] == o and b3["text"] == o:
        b1.config(bg=olive, fg=white)
        b2.config(bg=olive, fg=white)
        b3.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b4["text"] == o and b5["text"] == o and b6["text"] == o:
        b4.config(bg=olive, fg=white)
        b5.config(bg=olive, fg=white)
        b6.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b7["text"] == o and b8["text"] == o and b9["text"] == o:
        b7.config(bg=olive, fg=white)
        b8.config(bg=olive, fg=white)
        b9.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b1["text"] == o and b4["text"] == o and b7["text"] == o:
        b1.config(bg=olive, fg=white)
        b4.config(bg=olive, fg=white)
        b7.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b2["text"] == o and b5["text"] == o and b8["text"] == o:
        b2.config(bg=olive, fg=white)
        b5.config(bg=olive, fg=white)
        b8.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b3["text"] == o and b6["text"] == o and b9["text"] == o:
        b3.config(bg=olive, fg=white)
        b6.config(bg=olive, fg=white)
        b9.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b1["text"] == o and b5["text"] == o and b9["text"] == o:
        b1.config(bg=olive, fg=white)
        b5.config(bg=olive, fg=white)
        b9.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    elif b3["text"] == o and b5["text"] == o and b7["text"] == o:
        b3.config(bg=olive, fg=white)
        b5.config(bg=olive, fg=white)
        b7.config(bg=olive, fg=white)
        winner = True
        messagebox.showinfo("Noughts & Crosses", "O Wins!")
        disable_buttons()
    # 9 moves but no winner - tied game
    if count == 9 and winner == False:
        messagebox.showinfo("Noughts & Crosses", "Game Tied!")
        disable_buttons()

# func. handles button clicked event
def b_click(b):
    # declare global clicked, count variables
    global clicked, count

    # if button text is empty and turn is x's
    if b["text"] == " " and clicked == True:
        # set button text to x
        b["text"] = x
        # hand turn over to o
        clicked = False
        # add 1 to turn count
        count += 1
        # check if game won
        check_game_state()
    # if button text is empty and turn is o's
    elif b["text"] == " " and clicked == False:
        # set button text to o
        b["text"] = o
        # add 1 to turn count
        clicked += 1
        # check if game won
        check_game_state()
    else:
        # show alert when selected square is already taken
        messagebox.showerror("Noughts & Crosses", "That square is already taken!\nPick another one!")

# instantiate menu bar object and assign to root window menu option
game_menu = Menu(root)
# assign game menu to root menu
root.config(menu=game_menu)

# instantiate menu item object and assign to game menu with tearoff set to false (disallow floating menu)
options_menu = Menu(game_menu, tearoff=False)
# add menu item to game menu
game_menu.add_cascade(label="Game", menu=options_menu)
# add menu item and command to options menu
options_menu.add_command(label="Reset Game", command=init_game)

# init. game
init_game()
# update GUI every time event occurs
root.mainloop()
