#1
# # def display_message():
#     print('i am learning python')

# display_message()
#2
# book=input("please enter book name")
# def favorite_book(book):
    
#     print('my favorite book is',book)
# favorite_book(book)
#3
# def discribe_city(city,country):
#     print(city,"is a city in",country)

# discribe_city('kuiv','ukraine')
#4
# import random
# def compare_numbers(num):
#     random_num=random.randint(1,100)
#     print(random_num)
#     if num==random_num:
#         print("numbers are equal")
#     else:
#         print("numbers are not equal")

# compare_numbers(25)

#5
# def make_shirt(size,text):
#     print("The size of the shirt is", size," and the text is", text)

# make_shirt(45, "i love harry potter")
# def make_shirt(size="large", message="I love Python"):
#     print(f"The size of the shirt is {size} and the text is '{message}'")

# make_shirt()

#6
#magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
#def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)
#def the_great(magicians):
#     for magician in magicians:
#         print('the great',magician)

#the_great(magician_names)
#show_magicians(magician_names)
import random
#7
def get_random_temp():
    random_temp=random.randint(-10, 40)
    # print(random_temp)
    return random_temp
get_random_temp()

def main():
    temperature=get_random_temp()
    print('the temperature is now set to',temperature,'degrees celcium')
    if temperature<0:
        print('that is sooooo cold')
    if 0>temperature>16:
        print('its ok, but better take some jacket')
    if 16>= temperature>23:
        print('its awesome outside')
    else: 
        print('its summer')
main()
