print('Welcome to your new job!')
print('Your salary will start at 1 penny, and double every day')

days_worked=int(input('how many days do you plan to work? '))

while days_worked<=0:
    days_worked=int(input('please enter a valid amount of days: '))


print()
print('Day \t Salary')
print('----------------')

daily_salary=.005#start at .05 times 2 will be 1-the salary of the first day
total_salary=0
                    
for days in range (1,days_worked+1):
    daily_salary=daily_salary*2#each day salary doubles

    print(days, '\t $', format(daily_salary, ',.2f'),sep='')
    
    total_salary=total_salary+daily_salary

print()    
print('total salary: $'+format(total_salary, ',.2f'))
