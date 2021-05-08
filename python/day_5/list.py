# list/array

## initialise list
list = [1, 2, 99]

## get the length of list
length = len(list)
print(length)

## add element to a list at last
list.append(10)         # .append(element to add)
list.append(20)
print(list)

## add element at particular index
list.insert(1, 99)      # .insert(index, element)
print(list)

## remove element from end
list.pop()
print(list)

## find the index of element 
index_of_99 = list.index(99)
print(index_of_99)

## find number of times an element is present
count_of_99 = list.count(99)    # .count(whose count is needed)
print(count_of_99)

## joining lists (forms new list)
array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
joined = array1 + array2
print(joined)
print(array1)
print(array2)

## merging lists (mutates the original list)
array1.extend(array2)
print(array1)
print(array2)
