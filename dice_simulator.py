from tkinter import *
import random
import os
os.chdir(r"Dice Faces")
faces = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]


def generate():
    face = PhotoImage(file=random.choice(faces))
    l1 = Label(root, image=face)
    l1.image = face
    l1.place(relx=0.385, rely=0.3)


root = Tk()
root.title("Dice Simulator")
root.geometry('400x400')
Label(text="Dice Simulator", font="comicsans 19", padx=10, pady=10).place(relx=0.3, rely=0.2)
Button(root, text="Generate", command=generate).place(relx=0.45, rely=0.6)
root.mainloop()
