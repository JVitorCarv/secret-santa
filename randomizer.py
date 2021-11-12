import random

list_santa = []
list_chosen = []

#Appends all names to list_santa
inserting_names = True
while inserting_names == True:
    name = input('Insert names and type "end" when you finish all your names: ')
    if name.upper() != 'END':
        list_santa.append(name)
    else:
        inserting_names = False

#Appends all list_santa names to list_chosen
for name in list_santa:
    list_chosen.append(name)

random.shuffle(list_chosen)

print(list_santa)
print(list_chosen)
