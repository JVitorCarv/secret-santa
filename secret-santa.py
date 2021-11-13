import random

list_santa = []
list_chosen = []

print('='*12 + '\nSECRET SANTA\n' + '='*12)
print('\nWelcome! Use this CLI for generating your secret santa list!')
print('Disclaimer: this program does not save your generated list\n')
print('First, insert names and type "END" when you finish all your names\n')

#Appends all names to list_santa
inserting_names = True
while inserting_names == True:
    name = input('Insert name or "END": ')
    if name.upper() == 'END':
        inserting_names = False
    elif name.upper() in list_santa:
        print('This name has already been informed\nPlease try another one\n')
    else:
        list_santa.append(name.upper())

if len(list_santa) == 1:
    print('\nYou have to inform more than one name\nPlease run the program again')
    exit()
elif len(list_santa) == 0:
    exit()

#Appends all list_santa names to list_chosen
for name in list_santa:
    list_chosen.append(name)
    
print('\nGenerating the list and sorting people...\n')

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

#Interactive menu for displaying the secret santas
while True:
    print('Do you want to see all the santas or search for a specific person?')
    option = input('\nall - see all the santas\nspec - specific santa\nend - exit the program\n\nType here: ')

    if option.upper() == 'ALL':
        print('='*20)
        for i in range(len(list_santa)):
            print(f'{list_santa[i]} got {list_chosen[i]}!')
        print('='*20)
    
    elif option.upper() == 'SPEC':
        while True:
            print('\ngoback - go back to the previous menu\nend - exit the program')
            name = input('\nInsert the name of the specific santa: ')
            name = name.upper()
            
            if name == 'GOBACK':
                break
            elif name == 'END':
                exit()
            else:
                try:
                    print('='*45)
                    print(f'{name} got {list_chosen[list_santa.index(name)]}!')
                    print('='*45)
                except:
                    print(f'Could not find "{name}", please try again')
                    print('='*45)
    elif option.upper() == 'END':
        print('Thank you for using this program! Merry Christmas! :)')
        break
    else: 
        print(f'"{option}" => command unknown :(\nPlease try again\n\n')
