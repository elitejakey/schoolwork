compnum = 50
guess = int(input('Can you guess the number I am thinking of? Please enter a number: '))
count = 1
while guess != compnum:
    if guess<compnum:
        print('Too low')
    else:
        print('Too high')
    count = count+1
    guess = int(input('Have another guess: '))
print('Well done! It took you', count, 'attempts to guess the number')
