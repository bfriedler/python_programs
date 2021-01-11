#this is the second homework assignment
original_price=float(input("How much did your food cost? $"))
tip=original_price*.18
sales_tax=original_price*.07
total_price=original_price+tip+sales_tax
print('food price:$',format (original_price, '6.2f'),sep='')
print('tip:       $',format (tip,'6.2f'),sep='')
print('sales tax: $', format (sales_tax, '6.2f'),sep='')
print('total bill:$',format (total_price, '6.2f'),sep='')



