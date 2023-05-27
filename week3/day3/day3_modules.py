# 2
# import random
# def roll_dice(guess):
#     random_number=random.randint(1,100)
#     if guess==random_number:
#         print('u picked right one')
#     else: 
#         print('try again')
        
# user_guess = int(input("Enter a number between 1 and 100: "))
# roll_dice(user_guess)



# 3
# import string
# import random
# def generate_random_string():
#     letters = string.ascii_letters 
#     random_string = ''.join(random.choice(letters) for _ in range(5))
#     return random_string
# random_string = generate_random_string()
# print(random_string)

#4
# from datetime import datetime

# def display_current_date():
#     current_date = datetime.now().date()
#     print(current_date)

# display_current_date()


#5
from datetime import datetime

def time_left_until_january1():
    current_date = datetime.now().date()
    january1 = datetime(current_date.year + 1, 1, 1)  # January 1st of the next year
    time_left = january1 - datetime.now()
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours:02d}:{minutes:02d}:{seconds:02d} hours.")

# Example usage
time_left_until_january1()