import numpy as np
import funtools as ft
from funtools import save_path

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

desired_width = 320
np.set_printoptions(linewidth=desired_width)


# To generate a tournament draw in excel in your python directory end the number of rounds and the number of teams #
# , if you enter an odd number of teams the program will add an additional team to ensure there is an even number  #
# Example ft.make_my_draw(4, 28) will produce a draw of four rounds between 28 teams using 14 rinks. If you don't   #
# enter any parameters for Example ft.make_my_draw() the program will produce a draw of 4 rounds between 32 teams  #
# using 16 rinks. The final and third input variable creates a standard sequential draw (0) and if 1 is entered    #
# the round robin fixture is randomly shuffled. If you don't enter the third variable it will default to the          #
# standard sequential draw. #


ws = Tk()
ws.title("Lawn Bowls Draw Generator")
ws.geometry("600x600")

windowWidth = ws.winfo_reqwidth()
windowHeight = ws.winfo_reqheight()


positionRight = int(ws.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(ws.winfo_screenheight()/2 - windowHeight/2)
ws.geometry("+{}+{}".format(positionRight, positionDown))
test_text = 0


# ------------------------ progress bar widget ----------------------------------------------------------- #
progress = Progressbar(ws, orient=HORIZONTAL,
                       length=100, mode='indeterminate')


def bar():
    import time
    progress['value'] = 20
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 80
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 50
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    ws.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 20
    ws.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 0

# ------------------------------------------------------------------------------------------ #


def create_draw3():
    create_draw2()
    create_draw()
    return


def create_draw2():
    global test_text
    try:
        isinstance(int(rnds_tf.get()),int) and isinstance(int(teams_tf.get()), int)
        # isinstance(int(teams_tf.get()),int)
        test_text = 1
    except ValueError:
        test_text = 0
        messagebox.showerror("showinfo", "You need to enter whole numbers in both fields")
    return  # print(test_text)


def create_draw():

    if test_text != 0:

        if int(rnds_tf.get()) > 2 and int(teams_tf.get()) > 8:
            test_num = 1
        else:
            test_num = 0
            messagebox.showerror("showinfo", "Rounds must be > 3 and Teams must be > 8")

        if int(rnds_tf.get()) <= int(teams_tf.get()) - 1:
            test_num = 1
        else:
            test_num = 0
            messagebox.showerror("showinfo", "Rounds should be less than teams by at least 1")

        if test_text == 1 and test_num == 1:

            try:
                messagebox.showinfo("showinfo", f'Your draw will be saved to {save_path}\output_data.xlsx')
                bar()
                ft.make_my_draw(int(rnds_tf.get()), int(teams_tf.get()), var1.get(), var2.get(), var3.get())

            except ValueError as error:
                messagebox.showerror("showinfo", error)
                ws.destroy()
    return


teams_lb = Label(ws,text="Enter Number of Teams > 8")
teams_default = StringVar()
teams_tf = Entry(ws, text=teams_default)
teams_default.set(14)
rnds_default = StringVar()
rnds_lb = Label(ws,text="Enter Number of Rounds > 2")
rnds_tf = Entry(ws, text=rnds_default)
rnds_default.set(3)
rand_lb = Label(ws, text="Use random draw?")
var1 = IntVar(value=1)
rand_ch = Checkbutton(ws,variable=var1, onvalue=1, offvalue=0)

count_ends_lb = Label(ws, text='Count ends won in points score?')
var2 = IntVar(value=0)
count_ends_ch = Checkbutton(ws, variable=var2, onvalue=1, offvalue=0)

var3 = IntVar(value=0)
score_frame = LabelFrame(ws, text="Choose your scoring system")
score_frame.pack(pady=10)
Radiobutton(score_frame, text='10 - win, 5 - draw, 0 - loss', variable=var3, value=0).grid(row=1, column=1)
Radiobutton(score_frame, text='10 - win, 4 - draw, 0 - loss', variable=var3, value=1).grid(row=2, column=1)


prog_lb = Label(ws, text="Progress Indicator")
note_lb = Label(ws, text="NOTE - A large number of rnds (> 6) for a large number of teams (> 48) can take a"
                         " long time (>5 min) to resolve. Rnds should never exceed the number of teams - 1."
                         " The output file (Draw) will be saved to your desktop"
                , wraplength=450)
who_lb = Label(ws, text="Brought to you by Jd Johnson")


run_btn = Button(ws, text="Create Draw", command=create_draw3)


teams_lb.place(x=25, y=40, anchor=W)
teams_tf.place(x=270, y=40, anchor=CENTER)
rnds_lb.place(x=25, y=80, anchor=W)
rnds_tf.place(x=270, y=80, anchor=CENTER)
rand_lb.place(x=25, y=120, anchor=W)
rand_ch.place(x=233, y=120, anchor=E)
count_ends_ch.place(x=233, y=160, anchor=E)
count_ends_lb.place(x=25, y=160, anchor=W)
score_frame.place(x=25, y=230, anchor=W)
run_btn.place(x=100, y=300, anchor=E)
prog_lb.place(x=25, y=350, anchor=W)
progress.place(x=260, y=350, anchor=CENTER)
note_lb.place(x=25, y=400, anchor=W)
who_lb.place(x=25, y=460, anchor=W)

ws.mainloop()
