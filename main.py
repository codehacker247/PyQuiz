from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_list = question_data["results"]
for question in question_list:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your Final score is {quiz.score}/{quiz.question_number}")
