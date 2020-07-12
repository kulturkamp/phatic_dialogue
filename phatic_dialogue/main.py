import os
import pymorphy2
import random

morph = pymorphy2.MorphAnalyzer()

answers = {}
topic_lexemes = {}

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.txt') and 'lexemes' not in filename:
        with open(os.path.join(os.getcwd(), filename)) as f:
            answers[filename.split('.')[0]] = f.read().split('.')

for key in answers:
    for filename in os.listdir(os.getcwd()):
        if filename.endswith('lexemes.txt') and filename.split('_')[0] == key:
            with open(os.path.join(os.getcwd(), filename)) as f:
                topic_lexemes[key] = f.read().split()

# print(answers.keys())

print('greetings, lets chat! (phatically)')

topic = 'default'
prev = ''
subj = []
while True:
    question = input()
    if question == 'end convo':
        print('Bye!')
        break
    question_lexemes = ' '.join([morph.normal_forms(w)[0] for w in question.split()])
    print(type(question_lexemes))
    for lexeme in question_lexemes.split():
        for key in topic_lexemes:
            if lexeme in topic_lexemes[key]:
                subj.append(key)
    topic = random.choice(subj) if subj else 'default'

    if topic == prev and len(subj) > 1:
        other = [t for t in subj if t != topic]
        topic = random.choice(other)

    print(random.choice(answers[topic]))

    prev = topic
    topic = 'default'
    subj.clear()
