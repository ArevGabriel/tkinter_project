import tkinter as tk
from tkinter import messagebox

class QuizApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Quiz Site")
        self.geometry("400x300")

        self.questions = [
            {
                'question':'How can you pay for stay at a hotel?',
                'options':['Cash','Credit card','Debit card','In another way'],
                'correct_answer':'Credit card'
            },
            {
                'question':'Did you find the hotel amenities satisfactory?',
                'options':['Yes, completely satisfied','Yes, somewhat satisfied',
                           'No, somewhat dissatisfied',' No, completely dissatisfied'],
                'correct_answer':'Yes, completely satisfied'
            },
            {
                'question':'How are your requests typically handled by hotel staff?',
                'options':['Promptly and courteously','According to availability',
                           'Within hotel policies','All of the above'],
                'correct_answer':'All of the above'
            },
            {
                'question':'How would you rate the cleanliness of your room?',
                'options':['Very Clean','Clean','Somewhat Clean','Not Clean'],
                'correct_answer':'Very Clean'
            },
            {
                'question':'How would you rate the friendliness of the hotel staff?',
                'options':['Very Friendly','Friendly','Neutral','Unfriendly'],
                'correct_answer':'Friendly'
            },
            {
                'question':'How likely are you to recommend this hotel to others?',
                'options':['Very Likely','Likely','Neutral','Unlikely'],
                'correct_answer':'Very Likely'
            },
            {
                'question':'How would you rate the value for money at this hotel?',
                'options':['Excellent value','Good value','Average value','Poor value'],
                'correct_answer':'Excellent value'
            },
            {
                'question':'How satisfied were you overall with your stay at our hotel?',
                'options':['Very Satisfied','Satisfied','Neutral','Dissatisfied'],
                'correct_answer':'Very Satisfied'
            }   
        ]

        self.current_question_index = 0
        self.score = 0
        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self, text="", wraplength=400, justify="center", pady=20)
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", width=30, command=lambda idx=i: self.answer_question(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(self, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)

    def answer_question(self, option_idx):
        selected_option = self.questions[self.current_question_index]["options"][option_idx]
        correct_answer = self.questions[self.current_question_index]["correct_answer"]

        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
            self.next_button.config(state=tk.DISABLED) 
        else:
            messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(self.questions)}!")
            self.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()