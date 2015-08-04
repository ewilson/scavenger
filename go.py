import os

from questions import Question
from hashanswer import DELIM

def list_unsolved_questions():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    correct_answers = 15 - len(questions)
    question_limit = correct_answers + 2
    print '%d ANSWERS FOUND!\n' % correct_answers
    for i, k in enumerate(questions.keys()):
        if i >= question_limit:
            break
        print '%d) %s' % (k, questions[k].question)

def take_guess():
    q_raw = raw_input('\nWhich question? ')
    if q_raw.isdigit() and int(q_raw) in questions:
        q = int(q_raw)
        question = questions[q]
        a = raw_input('Answer? ')
        if question.check(a):
            print 'That is correct!'
            del questions[q]
        else:
            print '"%s" is incorrect for question %d' % (a, q)
    else:
        print 'That number choice is invalid'
    raw_input('Press [Enter] to continue\n')

def go():
    while questions:
        list_unsolved_questions()
        take_guess()
    print 'Congratulations! You have completed the scavenger hunt!'

def load_questions(filename):
    with open(filename) as f:
        qa = f.readlines()
    return {i: Question(*line.split(DELIM)) for (i, line) in enumerate(qa)}

questions = load_questions('qa.txt')

if __name__ == '__main__':
    go()
