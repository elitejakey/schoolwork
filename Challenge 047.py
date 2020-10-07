num1 = int(input('Please enter a number: '))
total = num1
again = 'y'
while again == 'y':
    num2 = int(input('Please enter another number'))
    total = total + num2
    again = input('Do you want to add another number? (Please enter y/n): ')
print('The total of the two numbers is ',total)
                  
