import os

from questions import Question
from hashanswer import DELIM

def display_status():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    status_indicator = ['  ' if n in questions else '##' for n in range(TOTAL_Q)]
    print '|%s|' % '|'.join(status_indicator)
    print '%d of %d ANSWERS FOUND\n' % (TOTAL_Q - len(questions), TOTAL_Q)

def list_unsolved_questions():
    question_limit = TOTAL_Q - len(questions) + 2
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
        display_status()
        list_unsolved_questions()
        take_guess()
    print 'Congratulations! You have completed the scavenger hunt!'

def load_questions(filename):
    with open(filename) as f:
        qa = f.readlines()
    return {i: Question(*line.split(DELIM)) for (i, line) in enumerate(qa)}

questions = load_questions('qa.txt')
TOTAL_Q = len(questions)

if __name__ == '__main__':
    go()
