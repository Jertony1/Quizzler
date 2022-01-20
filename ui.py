from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.question_canvas.create_text(150, 125,
                                                              width=280,
                                                              text="",
                                                              font=("Arial", 20, "italic")
                                                              )
        self.question_canvas.grid(row=1, columnspan=2, padx=20, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz."
                                                                     f" {self.quiz.score}/{self.quiz.question_number}")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, func=self.next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")