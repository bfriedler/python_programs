#here is the original recipe printed
print('Cookies')
print('1.5 cups sugar')
print('1 cup butter')
print('2.75 cups flour')

#here the program asks how many cookies you want to make  and converts it into an integer
amt_of_cookies= int(input('\nThis recipe makes 48 cookies. How many cookies would you like to make? '))

#here the program converts the ingredient amounts into floated numbers so it can do math with them
sugar=float(1.5)
butter=float(1)
flour=float(2.75)

#then it divides the amount of cookies you want to make by 48 which gives you the percent of the recipe that you want to make
percent_of_recipe=amt_of_cookies/48

#then it multiplies each ingredient by that percent which gives you how much of each ingredient you need
sugar=sugar*percent_of_recipe
butter=butter*percent_of_recipe
flour=flour*percent_of_recipe

#then it prints the amount of each ingredient you need
print("\nOkay, here's what you'll need:")
print ('sugar ',format(sugar,'5.2f'),'cups')#the 5.2f makes it line up the decimals by making them all have 5 places and the .2 rounds it to 2 decimal places
print ('butter',format(butter,'5.2f'),'cups')
print ('flour ',format(flour,'5.2f'),'cups')
