num = int(input('Please enter a number between 10 and 20: '))
while num <10 or num >20:
    if num <10:
        print('Too low')
    else:
        print('Too high')
    num = int(input('Try again: '))
print('Thank you')
