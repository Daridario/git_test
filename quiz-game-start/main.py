from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

cheat = input("Do you want to cheat? 'y' or 'n'? :) ")
if cheat == 'y':
    print("All right then.. here are the questions and answers.")
    for question in question_bank: # Cheats ON
        print(f"Question: {question.text} Answer: {question.answer}")

quiz = QuizBrain(question_bank)
quiz.next_question()
