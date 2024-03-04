print('Bible Quiz Game')
ready = input('Are you ready to play the Quiz? (yes/no): ').lower()

if ready == 'yes':
    score = 0
    total_questions = 5

    q1 = input('Question 1: How many books are in the New Testament? ')
    if q1.lower() == '27':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    q2 = input('Question 2: How many books are in the Old Testament? ')
    if q2.lower() == '39':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

        q3 = input('Question 3: Is there ten commandments in the bible? ')
    if q3.lower() == 'yes':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

        q4 = input('Question 3: Was Adam the first person that God created? ')
    if q4.lower() == 'yes':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

        q5 = input('Question 3: Is there 7 people that God trusted? ')
    if q5.lower() == 'yes':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    print(f'Your score is {score} out of {total_questions}.')
    if score >= total_questions / 5:
        print('Well done, you passed the quiz!')
    else:
        print('You did not pass the quiz. Better luck next time!')
