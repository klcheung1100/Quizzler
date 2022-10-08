from tkinter import *
from quiz_brain import  QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        bk_img = PhotoImage(file=r"images/bg.png", height=400)
        self.canvas.create_image(100, 80, image=bk_img)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill="white",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.title_label = Label(text="Computer Quiz", fg="white", bg=THEME_COLOR, font=("Arial", 16, "bold"))
        self.title_label.grid(column=0, row=0)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        tick_image = PhotoImage(file=r"images/true.png")
        self.checkmark_button = Button(image=tick_image, highlightthickness=0, command=self.true_press)
        self.checkmark_button.grid(row=2, column=0)

        cross_image = PhotoImage(file=r"images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.false_press)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="It is the end of the quiz.")
            self.checkmark_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



