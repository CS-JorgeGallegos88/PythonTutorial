from Days_1_10.studentScores import highest_score
from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_model = QuestionModel(question["text"], question["answer"].lower())
    question_bank.append(question_model)

quiz_brain = QuizBrain(question_bank)
print(quiz_brain.is_questionary_complete())

while not quiz_brain.is_questionary_complete():
    quiz_brain.next_question()

quiz_brain.show_score()