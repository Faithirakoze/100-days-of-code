from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


data = pandas.read_csv("data/french_words.csv")
words_dict = {row.French: row.English for (index, row) in data.iterrows()}

def next_card():
    global words_dict
    french_words_list = list(words_dict.keys())
    random_fr_word = random.choice(french_words_list)
    print(random_fr_word)

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_fr_word)

def flip_card():
    english_words_list = list(words_dict.values())
    random_en_word = random.choice(english_words_list)
    print(random_en_word)

    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=random_en_word)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=my_image)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.grid(row=0, column=0, columnspan=2)


button1_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=button1_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

button2_image = PhotoImage(file="images/right.png")
right_button = Button(image=button2_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()



window.mainloop()