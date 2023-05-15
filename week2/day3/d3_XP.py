#1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict=dict(zip(keys,values))
# print(dict)

#2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# family_price=0
# for name,age in family.items():
#     if age<3:
#         ticket_price=0
#     if 3<age<=12:
#         ticket_price=10
#     else:
#         ticket_price=15
#     print(f"{name} has to pay ${ticket_price}")
#     family_price+=ticket_price
# print(f"total cost is ${family_price}")

#3
# brand = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ['men', 'women', 'children', 'home'],
#     'international_competitors': ['Gap', 'H&M', 'Benetton'],
#     'number_stores': 7000,
#     'major_color': {
#         'France': ['blue'],
#         'Spain': ['red'],
#         'US': ['pink', 'green']
#     }
# }
# brand['number_stores']=2
# print(brand['number_stores'])
# print("the clients od store are",brand['type_of_clothes'])
# brand['country_creation']='Spain'
# print("country of creation is", brand['country_creation'])
# del brand['creation_date']
# print("the major colors in US are:",brand['major_color']['US'])
# print(len(brand))
# keys = brand.keys()
# print(keys)

# more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
#     }
# brand.update(more_on_zara)
# print(brand)

#4

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
for index, name in enumerate(users):
    disney_users_A[name]=index
print(disney_users_A)

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_B = {}
for index, name in enumerate(users):
    disney_users_B[index]=name
print(disney_users_B)

disney_users_C=dict(enumerate(sorted(users)))
print(disney_users_C)

disney_users_A_i = {}
for index,name in enumerate(users):
    if 'i' in name:
        disney_users_A_i[name]=index   
print(disney_users_A_i)

