#1
# word = input("please enter a word: ")
# letter_indexes = {}

# for index, letter in enumerate(word):
#     if letter in letter_indexes:
#         letter_indexes[letter].append(index)
#     else:
#         letter_indexes[letter] = [index]

# print(letter_indexes)
#2
items_purchase = {
  "Water": "1",
  "Bread": "3",
  "TV": "1,000",
  "Fertilizer": "20",
  "Arbuz": "200"
}

wallet = "300"

affordable_items = []

for item, price in items_purchase.items():
    item_price = int(price.replace(",", ""))
    if item_price <= int(wallet):
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print(affordable_items)
else:
    print("Nothing")
 