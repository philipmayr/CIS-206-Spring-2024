# Reference: Tic Tac Toe Game - Python Tkinter GUI Tutorial #113
#            https://www.youtube.com/watch?v=xx0qmpuA-vM

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Noughts & Crosses")

x = '𝕏'
o = '𝕆'
amaranth = "#71324B"
olive = "#4B7132"
white = "#ffffff"
clicked = True
count = 0

def disable_buttons():
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
    global winner
    winner = False

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

 
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = x
        clicked = False
        count += 1
        check_game_state()
    elif b["text"] == " " and clicked == False:
        b["text"] = o
        clicked += 1
        check_game_state()
    else:
        messagebox.showerror("Noughts & Crosses", "That square is already taken!\nPick another one!")


b1 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 24), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()
