agree_age = 18
#Ask user name
name = input("Hello what is your name?")
print("Hello. " + name)

#Ask user age
age = input("Hello please enter your age")
a = int(age)
print("You are." + a)

if a > agree_age:
    print("You can get driver lince")
elif a == 18 and a > 18:
    print("You can get driver lince")    
else: 
    print("Next year guy!")    
