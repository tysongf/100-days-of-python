class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def get_question(self):
        return self.question_list[self.question_number]

    def next_question(self):
        self.question_number += 1
        if len(self.question_list) == self.question_number:
            self.question_number = 0
            return False
        else:
            return True

