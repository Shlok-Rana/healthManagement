print('========== Health Management System ==========')

def getdate():
    import datetime
    return datetime.datetime.now()

time = getdate()

def logretrieveData():
    while (1):
        print('Enter 1 for ---> Shlok\n''Enter 2 for ---> Ojash\n''Enter 3 for ---> Prashant')
        user = int(input('Enter client name = '))
        print('\n')

        print('Enter 1 for ---> Exersise\n''Enter 2 for ---> Diet')
        menu = int(input('Enter your choice = '))
        print('\n')

        print('Enter 1 for ---> Log Data\n''Enter 2 for ---> Retrieve Data\n''Enter 3 for ---> Exit')
        choice = int(input('Enter your demand = '))
        print('\n')

        if (choice == 3):
            print('Thanks for visit')
            break

        def forClientExersise():
            if (user == 1 and menu == 1):
                if (choice == 1):
                    f = open('shlokExersise.txt', 'a')
                    exersise = input('Exersise name entry here: ')
                    f.write(str([str(time)]) + ':' + exersise + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('shlokExersise.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')

            elif (user == 2 and menu == 1):
                if (choice == 1):
                    f = open('ojashExersise.txt', 'a')
                    exersise = input('Exersise name entry here: ')
                    f.write(str([str(time)]) + ':' + exersise + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('ojashExersise.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')

            elif (user == 3 and menu == 1):
                if (choice == 1):
                    f = open('prashantExersise.txt', 'a')
                    exersise = input('Exersise name entry here: ')
                    f.write(str([str(time)]) + ':' + exersise + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('prashantExersise.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')

        forClientExersise()

        def forClientdiet():
            if (user == 1 and menu == 2):
                if (choice == 1):
                    f = open('shlokDiet.txt', 'a')
                    diet = input('Diet entry here: ')
                    f.write(str([str(time)]) + ':' + diet + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('shlokDiet.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')

            elif (user == 2 and menu == 2):
                if (choice == 1):
                    f = open('ojashDiet.txt', 'a')
                    diet = input('Diet entry here: ')
                    f.write(str([str(time)]) + ':' + diet + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('ojashDiet.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')

            elif (user == 3 and menu == 2):
                if (choice == 1):
                    f = open('prashantDiet.txt', 'a')
                    diet = input('Diet entry here: ')
                    f.write(str([str(time)]) + ':' + diet + '\n')
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                elif (choice == 2):
                    f = open('prashantDiet.txt', 'rt')
                    print(f.read())
                    f.close()
                    print('Task is successfully done.')
                    print('\n')

                else:
                    print('Error, try again!')
                    print('\n')


        forClientdiet()

logretrieveData()
















