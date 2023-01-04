up_d=input("Choose a direction 'Up' or 'Down' :")
if up_d=='Up':
    num=int(input('Maximum number: '))
    for i in range(1,num+1):
        print(i)
elif up_d=='Down':
    num=int(input('A number under 20: '))
    for i in range(20,num-1,-1):
        print(i)
else:
    print('I don\'t understand.')

amount = int(input('How many people do you want to invite?'))
if amount < 10:
    for i in range(amount):
        name = input("What is the person\'s name?")
        print(f'{name} has been invited.')

elif amount >= 10:
    print("Too many people.")