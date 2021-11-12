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

#Function that verifies if a santa is the same person as the one who'll be gifted
def verifier(santa, chosen):
    for i in range(len(santa)):
        if santa[i] == chosen[i]:
            return False
    return True

#Generates a new random list_chosen while verification process is false
is_valid = False
while is_valid == False:
    random.shuffle(list_chosen)
    is_valid = verifier(list_santa, list_chosen)
