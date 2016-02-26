from fractions import Fraction  
while True:
    list_quadratic = list(input('>'))
#form F(x) = ax^c

#Magnitude
    position = list_quadratic.index('x')

    try:
        if list_quadratic[0] == 'x':
            a = 1
        else:
            a = Fraction(list_quadratic[position - 1])
    except:
        print('Error occured')
    
    magnitude = a
    
#power
    if '^' in list_quadratic:
        c = Fraction(list_quadratic[position + 2])
        
    else:
        c = 1
           
    power = c
     
#derivative
    new_power = power - 1
    new_magnitude = magnitude * power
    
    if new_power == 0:
        derivative = '{}'.format(new_magnitude)
        print(derivative)
    
    else:
        derivative = '{}x^{}'.format(new_magnitude, new_power)
        print(derivative)