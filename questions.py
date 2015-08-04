from hashlib import md5

class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer.strip()

    def check(self, answer):
        hexed = md5(answer.lower().strip()).hexdigest()
        return self.answer == hexed

