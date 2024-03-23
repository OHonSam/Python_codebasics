item1 = "bread"
item2 = "pasta"
item3 = "fruits"

# similar with array in C++
items = ["bread","pasta", "fruits", "veggies"]

print(items)
print(items[0])

items[0] = 'chips'
print(items[-2])

# from to
print(items[0:3])

# append new elements 
items.append("butter")

# insert in whatever position you want in the list
# .insert(index, new item)
items.insert(2, "HelloKitty")
print(items[0:3])


# append two lists
food = ["bread", "pasta", "fruits"]
bathroom = ["shampoo", "soap"]
items = food + bathroom
print(items)

# len([list]) -> output the number of items in that list
print(len(items))

# [item] in [list]
# check if an item is in the list
print("shampoo" in items)