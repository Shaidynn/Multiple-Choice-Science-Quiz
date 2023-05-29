import random

questions = [
    'What is the formula for Work?: ',
    'What is the formula for Energy?: ',
    'What is stored energy and energy in motion called?: ',
    'What is the formula for pressure?: ',
    'What is light?: ',
    'What is Ohm\'s law used to calculate?: ',
    'What is the SI unit of electric current?: ',
    'What is the law of conservation of energy?: ',
    'What is the unit of power?: ',
    'What is the formula for speed?: ',
    'What is the unit of frequency?: ',
    'What is the formula for density?: ',
    'What is the SI unit of temperature?: ',
    'What is the law of reflection?: ',
    'What is the formula for gravitational force?: '
]

options = [
    ['A. W = FD', 'B. W = F/D', 'C. W = F/A', 'D. W = D/F'],
    ['A. E = M^2C', 'B. E = MC^2', 'C. E = MC', 'D. E = CM'],
    ['A. Stored, Potential', 'B. Motion, Kinetic', 'C. Stored, Motion', 'D. Potential, Kinetic'],
    ['A. P = F/A', 'B. P = A/F', 'C. P = F x A', 'D. P = F - A'],
    ['A. Radiant Energy', 'B. Heat', 'C. Warm Energy', 'D. Essence of Life'],
    ['A. Resistance', 'B. Voltage', 'C. Current', 'D. Power'],
    ['A. Ampere', 'B. Watt', 'C. Joule', 'D. Volt'],
    ['A. Energy cannot be created or destroyed', 'B. Energy can be destroyed but not created',
     'C. Energy can be created but not destroyed', 'D. Energy is always conserved'],
    ['A. Joule', 'B. Watt', 'C. Newton', 'D. Ampere'],
    ['A. S = d/t', 'B. S = t/d', 'C. S = (d/t)^2', 'D. S = d + t'],
    ['A. Hertz', 'B. Watt', 'C. Ampere', 'D. Volt'],
    ['A. D = m/V', 'B. D = V/m', 'C. D = m x V', 'D. D = m + V'],
    ['A. Celsius', 'B. Kelvin', 'C. Fahrenheit', 'D. Rankine'],
    ['A. Light travels in straight lines', 'B. The angle of incidence equals the angle of reflection',
     'C. Light can pass through opaque objects', 'D. Light has a constant speed'],
    ['A. F = (G x m1 x m2) / r^2', 'B. F = G x (m1 x m2) / r', 'C. F = (m1 x m2) / (G x r^2)', 'D. F = G x m1 x m2']
]

answers = ['A', 'B', 'D', 'A', 'A', 'C', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'B', 'A']
guesses = []
score = 0

randomized_questions = list(enumerate(questions))
random.shuffle(randomized_questions)

print('Welcome to the Quiz!\n')

for question_num, question in randomized_questions:
    print('---------------')
    print(question)
    randomized_options = random.sample(options[question_num], len(options[question_num]))
    for option in randomized_options:
        print(option)

    while True:
        guess = input('Enter your answer (A, B, C, D): ').upper()
        if guess not in ['A', 'B', 'C', 'D']:
            print('Invalid input. Please enter A, B, C, or D.')
        else:
            break

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print(f'The correct answer is {answers[question_num]}')

print('---------------')
print('       RESULTS      ')
print('---------------')

print('Questions: ')
for idx, question in randomized_questions:
    print(f'{idx + 1}. {question}')

print('\nYour Answers: ')
for idx, guess in randomized_questions:
    print(f'{idx + 1}. {guesses[idx]}')

print('\nCorrect Answers: ')
for idx, answer in randomized_questions:
    print(f'{idx + 1}. {answers[idx]}')

score_percentage = (score / len(questions)) * 100
print(f'\nYour score is: {score_percentage}%')

