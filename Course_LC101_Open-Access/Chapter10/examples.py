vocabulary = ["iteration", "selection", "control"]
numbers = [17, 123]
empty = []
mixed_list = ["hello", 2.0, 5*2, [10, 20]]

print(numbers)
print(mixed_list)
new_list = [ numbers, vocabulary ]
print(new_list)

#--------------------------------------

numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9 - 8])
print(numbers[-2])

#--------------------------------------

nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)
item = innerlist[1]
print(item)

print(nested[3][1])

#-------------------------------------

alist =  ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]))

#-------------------------------------

fruit = ["apple", "orange", "banana", "cherry"]

print("apple" in fruit)
print("pear" in fruit)

#-----------------------------------------

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

#---------------------------------------

a = ['one', 'two', 'three']
del a[1]
print(a)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

#----------------------------------------

fruit = ["banana", "apple", "cherry"]
print(fruit)

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

#------------------------------------------

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = ['x', 'y']
print(alist)

#------------------------------------------

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []
print(alist)

#-------------------------------------------

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop()
print(lastitem)
print(mylist)

#----------------------------------------

mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist = mylist.sort()   # error
print(mylist)

#----------------------------------------

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits:     # by item
    print(afruit)

#----------------------------------------

fruits = ["apple", "orange", "banana", "cherry"]

for position in range(len(fruits)):     # by index
    print(fruits[position])

#--------------------------------------------

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print(numbers)

#--------------------------------------------

fruit = ["apple", "orange", "banana", "cherry"]
print([1, 2] + [3, 4])
print(fruit + [6, 7, 8, 9])

print([0] * 4)
print([1, 2, ["hello", "goodbye"]] * 2)

#----------------------------------------------

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

print(a == b)

#----------------------------------------------

a = [81, 82, 83]
b = a
print(a is b)

#--------------------------------------------

orig_list = [45, 76, 34, 55]
print(orig_list * 3)

#------------------------------------------

orig_list = [45, 76, 34, 55]
print(orig_list * 3)

new_list = [orig_list] * 3

print(new_list)

#----------------------------------------

orig_list = [45, 76, 34, 55]

new_list = [orig_list] * 3

print(new_list)

orig_list[1] = 99

print(new_list)

#----------------------------------------

orig_list = [45, 76, 34, 55]

new_list = [orig_list] * 3

another_list = orig_list * 3

print(new_list)

print(another_list)

orig_list[1] = 99

print(new_list) # Note the change

print(another_list) # Note the lack of change

#------------------------------------------

def double_stuff(alist):
    """ Overwrite each element in alist with double its value. """
    for position in range(len(alist)):
        alist[position] = 2 * alist[position]

def main():
    things = [2, 5, 9]
    print(things)
    double_stuff(things)
    print(things)

if __name__ == "__main__":
    main()

#----------------------------------------------

def double_stuff(alist):
    """ Return a new list in which contains doubles of the elements in alist. """
    new_list = []
    for value in alist:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

def main():
    things = [2, 5, 9]
    print(things)
    things = double_stuff(things)
    print(things)

if __name__ == "__main__":
    main()

#-----------------------------------------

my_list = [1,2,3,4,5]
your_list = [item ** 2 for item in my_list]
print(your_list)

#-----------------------------------------

song = "The rain in Spain..."
words = song.split()
print(words)

#--------------------------------------------

song = "The rain in Spain..."
words = song.split('ai')
print(words)

#---------------------------------------------

words = ["red", "blue", "green"]
glue = ';'
s = glue.join(words)
print(s)
print(words)

print("***".join(words))
print("".join(words))

#---------------------------------------------

xs = list("Crunchy Frog")
print(xs)

