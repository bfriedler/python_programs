import random

def main():
    computer_choice=computer_picker()
    #1=rock
    #2=paper
    #3=scissors
    user_choice=user_picker()
    print('Computer chose',computer_choice)
    determiner(computer_choice, user_choice)
    

def computer_picker():
    number=random.randint(1,3)
    if number==1:
        value='rock'
    elif number==2:
        value='paper'
    else:
        value='scissors'
    return value

def user_picker():
    choice=input('please enter rock, paper, or scissors ')
    while choice != 'rock' and choice !='paper' and choice !='scissors':
        choice = input('please enter a valid choice')
    return choice    

def determiner(computer_choice2, user_choice2):
    if computer_choice2==user_choice2:
        print('let\'s redo this!')
        main()
    elif computer_choice2=='rock':
        if user_choice2=='paper':
            winner='user'
        else:
            winner='computer'
    elif computer_choice2=='paper':
        if user_choice2=='rock':
            winner='computer'
        else:
            winner='user'
    elif computer_choice2=='scissors':
        if user_choice2=='rock':
            winner='user'
        else:
            winner='computer'
    print('winner:',winner)            

main()    
