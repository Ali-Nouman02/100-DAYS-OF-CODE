from tkinter import *
import pandas as pd
import random
import csv

BACKGROUND_COLOR = "#B1DDC6"
french_word = ""
random_int = 0
data_words_to_learn = {}
# ---------------------------- Button functions------------------------------- #

#intial dataset- file name = french_words.csv
df = pd.read_csv('C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\french_words.csv')
data = df.to_dict(orient="records")

def generate_french_word(button):
    global french_word
    global random_int
    global data_words_to_learn
    #this is the first french word that is displayed
    if button == "start":
        random_int = random.randint(0, len(df) - 1)
        french_word = data[random_int]["French"]
        canvas.itemconfig(canvas_word, text=french_word, fill="black")
        canvas.itemconfig(canvas_image, image=french_img)
        canvas.itemconfig(canvas_title, text="French", fill="black")
        window.after(3000, switch_canvas, random_int, data)

    elif button != "start":
        try:
            #this is the code for word_to_learn.csv
            df_words_to_learn = pd.read_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\words_to_learn.csv")
            data_words_to_learn = df_words_to_learn.to_dict(orient="records")

            random_int = random.randint(0, len(df_words_to_learn)-1)
            french_word = data_words_to_learn[random_int]["French"]
            canvas.itemconfig(canvas_word, text=french_word, fill="black")
            canvas.itemconfig(canvas_image, image=french_img)
            canvas.itemconfig(canvas_title, text="French", fill="black")

            # Schedule to switch to English after 3 seconds
            window.after(3000, switch_canvas, random_int,data_words_to_learn)
        except FileNotFoundError:
            if button == "tick":
                for i, row in df.iterrows():
                    if row["French"] == french_word:
                        df.drop(index=i, inplace=True)
                df.to_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\words_to_learn.csv", index=False)
            elif button == "cross":
                df.to_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\words_to_learn.csv", index = False)


            #in the first run the words_to_learn will not exist so it will use this instead
            random_int = random.randint(0, len(df)-1)
            french_word = data[random_int]["French"]
            canvas.itemconfig(canvas_word, text=french_word, fill="black")
            canvas.itemconfig(canvas_image, image=french_img)
            canvas.itemconfig(canvas_title, text="French", fill="black")

            window.after(3000, switch_canvas, random_int,data)
        else:
            #if it was tick remove that word from the dataframe else nothing
            if button == "tick":
                for i, row in df_words_to_learn.iterrows():
                    if row["French"] == french_word:
                        df_words_to_learn.drop(index=i, inplace=True)
                df_words_to_learn.to_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\words_to_learn.csv", index=False)
            elif button == "cross":
                df_words_to_learn.to_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\data\\words_to_learn.csv", index = False)


def switch_canvas(random_int,dict):
    if dict == data:
        english_word = data[random_int]["English"]
        canvas.itemconfig(canvas_word, text=english_word, fill="white")
        canvas.itemconfig(canvas_image, image=eng_img)
        canvas.itemconfig(canvas_title, text="English", fill="white")
    elif dict == data_words_to_learn:
        english_word = data_words_to_learn[random_int]["English"]
        canvas.itemconfig(canvas_word, text=english_word, fill="white")
        canvas.itemconfig(canvas_image, image=eng_img)
        canvas.itemconfig(canvas_title, text="English", fill="white")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashly")
window.config(padx = 50, pady= 50,bg = BACKGROUND_COLOR)


#canvas
canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg =BACKGROUND_COLOR)
french_img = PhotoImage(file = "C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\images\\card_front.png")
eng_img = PhotoImage(file = "C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\images\\card_back.png")
canvas_image = canvas.create_image( 400, 263,image = french_img)
canvas.grid(column = 0, row = 0, columnspan = 2)


# Centered text on canvas
canvas_title = canvas.create_text(400, 150, text="French", font=("Arial", 60, "italic"), fill="black")
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"), fill="black")


#Button - CROSS
cross_image = PhotoImage(file="C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\images\\wrong.png")
button_cross = Button (image=cross_image, highlightthickness=0, bg = BACKGROUND_COLOR, command = lambda: generate_french_word("cross"))
button_cross.grid(column= 0, row = 1 )


#Button - TICK
right_image = PhotoImage(file="C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 31\\flash-card-project-start\\images\\right.png")
button_cross = Button (image= right_image, highlightthickness=0, bg = BACKGROUND_COLOR , command = lambda: generate_french_word("tick"))
button_cross.grid(column= 1, row = 1 )


generate_french_word("start")


window.mainloop()