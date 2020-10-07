again = 'y'
count = 0
while again == 'y':
    name = input('Enter a name of somebody you want to invite to your party: ')
    print(name, 'has now been invited')
    count = count + 1
    again = input('Do you want to invite somebody else? (Please enter y/n): ')
print('You have', count, 'people coming to your party')
