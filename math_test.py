#You can solve these all problems you 
#Solve 1problem you got 1 socore
#If you roung one sums you got (-1)
uplodsoc = 0
#tell the user
your_socore = (0 + uplodsoc)
#Ask the user "what is the output of this code"
a = 250
b = 0
first = a * b

#What is the out put of this code?
#Only numer allowed please type number
answer1 = int(input("fill the answer"))
if  answer1 == first:
    uplodsoc = 1
    print("collect now your socore is" + str(your_socore + uplodsoc))
else:
    print("Noo! try next problem")

#Ask the user 'what is the output of this code'
c = 9 ** 1/2
d = 81 ** 1/2
e = 11 / 3
secound = (c + (d / e))
answer2 = int(input("fill the answer"))
if answer2 >= secound:
    uplodsoc = uplodsoc + 1
    print("collect now your socore is" + str(your_socore + uplodsoc))
else:
    print("Noo! try next problem")

#Ask the user 'what is the output of this code'
f = 0 - (-3)
g = -3 * (-1)
h = 9
third = ((f + g) - h)
answer3 = int(input("fill the answer"))
if answer3 < 0:
    uplodsoc = uplodsoc + 1
    print("collect now your socore is" + str(your_socore + uplodsoc))
else:
    print("Noo! try next problem")
    

#Ask the user 'what is the output of this code'
i = 0 * 0 - 10 +28 
j = i / 2 
fourth = i % j
answer4 = int(input("fill the answer"))
if answer4 == fourth:
    print("100% collect")
    if answer4 <= 0:
        print("too close bro")
    uplodsoc = uplodsoc + 1
    print("collect now your socore is" + str(your_socore + uplodsoc))
elif answer4 > 10:
    print("Noo! try next problem")


