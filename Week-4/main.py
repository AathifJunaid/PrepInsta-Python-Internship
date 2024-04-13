from question import Question
from syllabus import question_data
from brain import QuizBrain

#question bank of question objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the Quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
