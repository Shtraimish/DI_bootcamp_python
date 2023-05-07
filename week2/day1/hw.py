#1
print("hello world \n"*4)
#2
number=99**3*8
print(number)
#4
computer_brand="lenovo"
print("I have a computer", computer_brand, "computer")
#5   seems like str length max is short so i decided to make it in a few parts))
my_name="Vladimir"
my_age=32
shoe_size=42
info_sentance1 =f'I have literally no idea how to collect all the information like'
info_sentance2=f'my name, wich is {my_name}, my well known age because i have'
info_sentance3=f'a birthday today and now i am{my_age} years old, and my shoe size wich nobody is interested about but it is {shoe_size}'
print(info_sentance1,info_sentance2,info_sentance3)
#6
a=int(input("input A"))
b=int(input("input B"))
if(a>b):print("hello world")
#7
even_odd=int(input("please enter a number"))
if(even_odd%2==0):print("ur number is even")
else:print("ur number is odd")
#8
ur_name=str(input("what is ur name"))
if(my_name==ur_name):
    print("heeeey, dude we both have the same name")
else: ("u r not my bro, sorry", ur_name)
#9
height_inch=2.54*int(input("please enter ur height in inches"))
if(height_inch>=145):
    print("u r high enough to ride")
else:print("u r too short, go cath a bus")
