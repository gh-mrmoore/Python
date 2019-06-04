inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

key_list = list(inventory.keys())
print(key_list)

#----------------------------------

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Got key", k)

#-----------------------------------------

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

#---------------------------------------------

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

#---------------------------------------------

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))

#----------------------------------------------

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

#-----------------------------------------------

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

#---------------------------------------------

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])
print(julia[2:6])

print(len(julia))

julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)

#---------------------------------------------

def circle_info(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return (c, a)

print(circle_info(10))

#---------------------------------------------

(name, surname, birth_year, movie, movie_year, profession, birth_place) = julia

temp = a
a = b
b = temp

(a, b) = (b, a)

#-----------------------------------------------

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

#------------------------------------------------

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix.get((0,3)))

print(matrix.get((1, 3), 0))

# Create the sparse matrix using a dictionary
for i in range(5):
    for j in range(5):
        print(matrix.get((i, j), 0), "", end = '')
    print()

#--------------------------------------------

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]
index = 1
for competitor in tennis_champs:
    print(index, competitor)
    index += 1

#--------------------------------

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

for idx, item in enumerate(tennis_champs):
      print(idx, item)

#-----------------------------------------

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

for index, competitor in enumerate(tennis_champs, 1):
      print(index, competitor)

#-------------------------------------------

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

champs_dictionary = dict(enumerate(tennis_champs, 1))

print(champs_dictionary)

#-------------------------------------------

tennis_champs = ["Serena Williams", "Simona Halep", "Caroline Wozniacki",
    "Angelique Kerber", "Elina Svitolina"]

champs_tuples = list(enumerate(tennis_champs, 1))

print(champs_tuples)

#--------------------------------------------

