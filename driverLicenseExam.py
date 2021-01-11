
CORRECT_ANSWERS =['a', 'c', 'a', 'a', 'd', 'b', 'c', 'a', 'c', 'b', 'a', 'd', 'c', 'a', 'd', 'c', 'b', 'b', 'd', 'a']

def main():
    student_answers=get_answers()
    answer_checker(student_answers)
      



def get_answers(): #user inputs answer for each question
    print('enter the answer for each question:')
    answers=[]
    for i in range (len(CORRECT_ANSWERS)):
        print(i+1,': ', sep='', end='')
        answer=input()
        answer=answer.lower()#very likely the user will enter uppercase
        while answer !='a' and answer !='b' and answer !='c' and answer !='d':
            answer=input('please enter a value between a and d: ')#input validation
            answer=answer.lower()
        answers.append(answer)#makes a list of the student's answers
    return answers 


def answer_checker(student_answers2):
    score=0
    wrong_answers=[]

    for i in range (len(student_answers2)):
        if student_answers2[i]==CORRECT_ANSWERS[i]:#if student's answer matches answer key, she gets a point for it 
            score+=1

        else:
            wrong_answers.append(i+1) #if it's wrong the question number gets added to a list
            

    if score>=15:
        passed=('passed')
    else:
        passed=('failed')
    total_correct=(len(student_answers2))-len(wrong_answers)
    total_incorrect=len(wrong_answers)

    print('You',passed)
    print('total correct:',total_correct)
    print('total incorrect:',total_incorrect)

    if total_incorrect>0:
        print('here\'s the questions you got wrong:', wrong_answers)



main()
