from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = Label(text="Score:",fg = "white",bg = THEME_COLOR)
        self.score.grid(column=1, row=0,padx=20, pady=20)

        #canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0 , bg = "white")
        self.canvas.grid(column=0, row=1,columnspan = 2,padx=20, pady=20)

        #canvas-text
        self.question_text = self.canvas.create_text(150, 125,width = 280, text="test", font=("Arial", 20, "italic"), fill="black")

        # Button - true
        self.true_image = PhotoImage(file="C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 34\\quizzler-app-start\\images\\true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, bg=THEME_COLOR, command= self.true_pressed)
        self.true_button.grid(column=0, row=2,padx=20, pady=20)


        # Button - false
        self.false_image = PhotoImage(file="C:\\Users\\Dell\\PycharmProjects\\pythonProject\\100 days of code\\DAY 34\\quizzler-app-start\\images\\false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, bg=THEME_COLOR, command = self.false_pressed)
        self.false_button.grid(column=1, row=2,padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

