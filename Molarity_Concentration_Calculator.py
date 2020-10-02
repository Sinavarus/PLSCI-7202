# This is a script for PLSCI 7202
# Barituziga Banuna


# This script is a calculator for molarity and concentration
# of chemicals commonly used in the lab

# This is a dictionary of the chemicals and their molecular weights (g/mol)
ChemMW = {'POPC':100, 'DOPC_PEG_5k':50, 'NaCl': 11, 'D_Mannitol':10, 'CaCl2':70, 'HEPES': 45, 'Formaldehyde': 100, 'DTT': 111, 'NaOH': 120}
chems = []

#Prints the list of chemicals
def ChemList():
    print("Here are the chemicals in the database:")
    print('')
    for i in ChemMW:
        print(i)
    print('')

#Update the list of chemicals
def UpdateChemList():
    print('')
    newChem_name = input('What is the name of the new chemical? ')
    newChem_MW = input('What is the MW in g per mole? ')
    if newChem_MW.isnumeric():
        ChemMW[newChem_name] = newChem_MW
        print('Added to database')   
    else:
        #Error message
        print('Incorrect MW input')
        UpdateChemList()
    print('')
        

#Makes your selection
def ChemSelect():
    global chems
    chem = ''
    chksize = len(ChemMW)

    ChemList()
    while chem != 'END':
        chem = input("Which chemical? If that is all enter 'END' ")
        print('')
        found = False
        #Searches chemical database to see if chemical exist
        for i in ChemMW:
            if chem == i:
                chems.append(chem)
                print('confirmed')
                found = True
        if not found and chem != 'END':
            #Error message
            print('That chemical was not found.')
            #Redirects user to update database
            update = input('Do you want to add it? (Y or N) ')
            if update == 'Y':
                UpdateChemList()

#This performs the calculation
def MassCalc():
    ChemSelect()
    global chems
    print('')
    if chems == []:
        #Error message
        print('No selection, exiting...')
    else:
        volume = input('What is the desired total volume in L? ')
        if volume.isnumeric() == False:
            print('Incorrect volume input')
            MassCalc()

        #Calculation
        for i in chems:
            print('')
            print(i)
            desired_Molarity = input('What is the desired molarity in mols per L? ')
            if desired_Molarity.isnumeric() == False:
                print('Incorrect volume input')
                MassCalc()
            Mass = float(volume)*float(desired_Molarity)*float(ChemMW[i])
            print('')
            print('The required mass of')
            print(i)
            print('is')
            print(Mass)
            print('grams')
            print('')
    chems = []

#This script runs the program
def RunScript():
    print('Hello, welcome to the solution mass calculator.')
    print('')
    print('This program lets you calculate a mass of chemical')
    print('for a given molarity and total solution volume.')
    run = True

    #Runs this until told to exit
    while run:
        print('')
        print('')
        print('')
        print('Enter the number next to your choice. These are your options:')
        print('-----------------------------')
        print('| 1: View chemical list     |')
        print('| 2: Enter a new chemical   |')
        print('| 3: Make a new Calculation |')
        print('| 4: Exit                   |')
        print('-----------------------------')

        choice = input()
        if choice == '1':
            ChemList()
        if choice == '2':
            UpdateChemList()
        if choice == '3':
            MassCalc()
        else:
            run = False
        run = True

RunScript()
