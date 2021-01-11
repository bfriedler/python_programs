#This program calculaes the shipping charges of packages 
weight = float(input('what is the weight of your package, in pounds? '))

if weight <=2:
    rate= (1.5)
    
elif  weight<=6:
    rate=(3)
    
elif  weight<=10:
    rate=(4)

else:
    rate=(4.75)

shipping_charge=(weight*rate)

print('shipping charge: $',format (shipping_charge,'.2f'),sep='')
