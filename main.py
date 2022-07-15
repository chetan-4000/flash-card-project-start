from tkinter import *
import pandas
import random

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card={}

def next_card():
    global current_card,flip
    window.after_cancel(flip)
    current_card = random.choice((to_learn))
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_image,image=front_card)
    flip = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_image,image=back_card)

def is_correct():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip = window.after(3000,func=flip_card)

canvas =Canvas(width=800,height=586)
back_card = PhotoImage(file="images/card_back.png")
front_card = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400,283,image=front_card)
card_title = canvas.create_text(400,150, text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button =Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,highlightthickness=0,command=is_correct)
right_button.grid(row=1,column=1)


next_card()

window.mainloop()