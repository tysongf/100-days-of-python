from data import question_data
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question_bank = []

for q_dict in question_data:
    question_bank.append(Question(q_dict['text'], q_dict['answer']))
