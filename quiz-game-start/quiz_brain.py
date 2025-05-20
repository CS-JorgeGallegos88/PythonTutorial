class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.player_score = 0
        self.highest_score = len(question_list)

    def show_score(self):
        print(f"Your score is {self.player_score} out of {self.highest_score}")

    def is_questionary_complete(self):
        return self.question_number == len(self.question_list)

    def next_question(self):
        """Retrieves the question from list at specific index"""
        question = self.question_list[self.question_number]
        self.question_number += 1
        right_answer = question.answer.lower()
        player_answer = input(f"Q{self.question_number}: {question.text} (True/False)?:").lower()
        self.check_answer(player_answer, right_answer)

    def check_answer(self, p_answer, r_answer):
        if p_answer == r_answer:
            print("You got it right!")
            self.player_score += 1
        else:
            print("You got it wrong")

        print(f"Correct answer was: {r_answer}")