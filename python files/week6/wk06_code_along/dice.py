import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root=tk.Tk()
    frm_main=Frame(root)
    frm_main.master.title("Dice")
    frm_main.pack(padx=3,pady=3,fill=tk.BOTH,expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm):
    lbl_sides=Label(frm,text="Enter the number of sides on the dice?:")
    lbl_sides.grid(row=0,column=0)
    entry_box1=IntEntry(frm,width=2,lower_bound=2, upper_bound=20)
    entry_box1.grid(row=0, column=1)
    lbl_sides=Label(frm,text="Enter the number of dice to roll (1-10): ")
    lbl_sides.grid(row=1,column=0)
    entry_box2=IntEntry(frm,width=2,lower_bound=1,upper_bound=10)
    entry_box2.grid(row=1,column=1)
    btn_roll=Button(frm,text="Roll it!")
    btn_roll.grid(row=2,column=0)
    lbl_roll=Label(frm,text="")
    lbl_roll.grid(row=3,column=0)

    def roll_dice(sides,count):
        sum=0
        roll_text=""
        for roll in range(count):
            die_roll=random.randint(1,sides)
            sum +=die_roll
            roll_text+=f"{die_roll}"
        roll_text+=f" Total: {sum}"
        return roll_text

    
    def roll_action():
        try:
            sides=entry_box1.get()
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of sides!")
        try:
            count=entry_box2.get()
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of dice!")
        lbltext=roll_dice(sides,count)
        lbl_roll.config(text=lbltext)

    btn_roll.config(command=roll_action)



if __name__ == "__main__":
    main()