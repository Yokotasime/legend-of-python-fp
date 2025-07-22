
# Write code below 💖

my_list = {'Bananas', 'Oranges', 'Blood oranges', 'Pineapple'}

bf_list = {'Papaya', 'Mango', 'Guava', 'Xuxu', 'Pineapple', 'Bananas', 'Oranges'}

union_result = my_list.union(bf_list)
intersection_result = my_list.intersection(bf_list)

print(union_result)
print(intersection_result)

# Another option wti the same result

my_fruits = {'apple', 'banana', 'kiwi'}
friend_fruits = {'banana', 'orange', 'grape'}

# Uncomment to check if a fruit is <in> both list
# print('apple' in fruits)  # Output: True
# set3 = {'apple', 'orange'}
# print(set3.issubset(fruits))  # Output: True

union_result = my_fruits | friend_fruits
intersection_result = my_fruits & friend_fruits
difference_result = my_fruits - friend_fruits

print('Union:', union_result)
print('Intersection:', intersection_result)
print('My Fruits - Friend\'s Fruits:', difference_result)
