# Practice activity that shows how to move a integer to the end of a list.

list = [1, 0, 2, 0, 4, 6]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)

# This will move it to the item to the beginning.  Only works for first item!!!

new_list = [1, 0, 2, 0, 4, 6]

location = 0

for item in new_list:
    if item == 0:
        new_list.remove(item)
        new_list.insert(location, item)
        location = location + 1

print(new_list)