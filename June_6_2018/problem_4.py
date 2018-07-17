### Problem 4

birthdates = {'John' : '10/10/1993',
              'Bob' : '10/10/1993',
              'Sally' : '03/13/2012',
              'Rob' : '11/11/1993',
              'Santa' : '12/25/1342',
              'Greg' : '07/04/1975',
              'United States of America' : '07/04/1776',
              'Laura' : '02/16/1966',
              'Daryl' : '10/02/1965'
              }

def birthday_lister():
    while True:
        intro_message()
        user_input = input('Selection [1]: ')
        user_input = user_input or 3

        try:
            user_input = int(user_input)
            if user_input not in [1,2,3]:
                print('Please enter an acceptable number')
        except ValueError:
            print('Please enter a number')

        if user_input == 1:
            while True:
                print('Enter a name to see birthday')
                print('Or "list" to see all names')
                print('Or "exit" to go back to previous menu')
                user_input = input('Selection: ')
                if user_input == 'list':
                    name_lister()
                elif user_input == 'exit':
                    break
                else:
                    if user_input in birthdates:
                        print('The birthday of',
                              user_input,
                              'is',
                              birthdates.get(user_input))
                    else:
                        print('Name not found, names are case-senstitive')
                user_input = input('Do another search? [Y/n]: ').lower()
                user_input = user_input or 'y'
                if user_input == 'n':
                    break
        
        if user_input == 2:
            while True:
                print('Enter a date to see names')
                print('Date format is 01/31/1970')
                print('Or "exit" to go back to previous menu')
                user_input = input('Selection: ')
                if user_input == 'exit':
                    break
                else:
                    counter = 0
                    for key in birthdates:
                        if birthdates.get(key) == user_input:
                            counter += 1
                            print(user_input, 'is the birthdate of', key)
                        
                    if counter == 0:
                        print('No one in list has that birthday')
                user_input = input('Do another search? [Y/n]: ').lower()
                user_input = user_input or 'y'
                if user_input == 'n':
                    break

        if user_input == 3:
            print('Exiting program')
            return False
    return

def name_lister():
    print('Names of people in the list:')
    for key in birthdates.keys():
        print(key)

def intro_message():
    print('Birthday Selector')
    print('Available options:')
    print('[1]: Find birthday by name')
    print('[2]: Find name by birthday')
    print('[3]: Exit')

birthday_lister()
