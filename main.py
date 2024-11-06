import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Fetch questions from a specific course table
def fetch_questions(course_code):
    cursor.execute(f"SELECT question_text, option_a, option_b, option_c, option_d, correct_answer FROM {course_code}")
    return cursor.fetchall()

# Check if the selected answer is correct
def check_answer(selected_option):
    global current_question_index, score
    correct_answer = questions[current_question_index][5]  # correct_answer is the 6th element in each question tuple
    if selected_option == correct_answer:
        score += 1
    current_question_index += 1
    load_next_question()

# Load the next question or finish quiz if no questions remain
def load_next_question():
    if current_question_index < len(questions):
        question_label.config(text=questions[current_question_index][0])  # Display question text
        option_buttons[0].config(text=questions[current_question_index][1], command=lambda: check_answer(questions[current_question_index][1]))
        option_buttons[1].config(text=questions[current_question_index][2], command=lambda: check_answer(questions[current_question_index][2]))
        option_buttons[2].config(text=questions[current_question_index][3], command=lambda: check_answer(questions[current_question_index][3]))
        option_buttons[3].config(text=questions[current_question_index][4], command=lambda: check_answer(questions[current_question_index][4]))
    else:
        messagebox.showinfo("Quiz Complete", f"Your score: {score}/{len(questions)}")
        root.destroy()

# Start the quiz for the selected course
def start_quiz():
    global questions, current_question_index, score
    course_code = course_var.get()
    questions = fetch_questions(course_code)
    random.shuffle(questions)  # Shuffle questions for variety
    current_question_index = 0
    score = 0
    load_next_question()

# Initialize GUI window
root = tk.Tk()
root.title("Quiz Bowl")

# Course selection dropdown
course_var = tk.StringVar(root)
course_var.set("Select Course")
course_options = ["DS3850", "DS3860", "DS3620", "DS4125", "BIOL3920"]
course_menu = tk.OptionMenu(root, course_var, *course_options)
course_menu.pack(pady=20)

# Start quiz button
start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

# Question label
question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Arial", 14))
question_label.pack(pady=20)

# Option buttons
option_buttons = [
    tk.Button(root, text="", wraplength=300, font=("Arial", 12), width=30),
    tk.Button(root, text="", wraplength=300, font=("Arial", 12), width=30),
    tk.Button(root, text="", wraplength=300, font=("Arial", 12), width=30),
    tk.Button(root, text="", wraplength=300, font=("Arial", 12), width=30),
]

for button in option_buttons:
    button.pack(pady=5)

# Main event loop
root.mainloop()

# Close the database connection
conn.close()

