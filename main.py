##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Generator                                                                                                  #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator

def optionMenu():
    print("Choose an option to continue:")
    print("1. Generate a new password")
    print("2. Check password strength")
    print("3. Quit")
    option = int(input())
    if option == 1:
        passwordGeneratorMenu()
    elif option == 2:
        passwordCheckerMenu()
    else:
        print("Have a wonderful day 👋")

def getUserPassword():
    userPassword = input("Please enter your password: ")
    return userPassword

def passwordMode():
    mode = int(input("Answer: "))
    return mode

def generateNewPassword(mode):
    generatedPassword = password_generator.generatePassword(mode)
    return generatedPassword

def displayPasswordEntropy(generatedPassword = None):
    if generatedPassword == None:
        print("Entropy: {:.1f}".format(entropy.getEntropy(getUserPassword())))
    else:
        print("Entropy: {:.1f}".format(entropy.getEntropy(generatedPassword)))
    
def displayTimeToCrack(generatedPassword = None):
    if generatedPassword == None:
        print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(getUserPassword())))
    else:
        print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(generatedPassword)))

def getGeneratedPassword(mode):
    generatedPassword = generateNewPassword(mode)
    return generatedPassword
    
def displayGeneratedPassword(mode):
    generatedPassword = getGeneratedPassword(mode)
    print("Your new password is: " + generatedPassword)
    displayTimeToCrack(generatedPassword)
    displayPasswordEntropy(generatedPassword)
    
def passwordCheckerMenu():
    print()
    print("=======================================================")
    print("Password Strength Checker")
    print("Details...")
    print()
    print()
    displayTimeToCrack()
    displayPasswordEntropy()

def passwordGeneratorMenu():
    print("")
    print("=======================================================")
    print("Password Generator")
    print("Please answer the questions below to generate a password")
    print()
    print("What kind of password you would like? (Enter '1' or '2')")
    print()
    print("1. Passphrase (Easier to remember)")
    print("Example: swell posing gruffly slander onto")
    print()
    print("2. Random String (Alphanumeric)")
    print("Example: a9Fq7XrL2mP8ZKcE")
    print()
    # TODO: Add a 3rd option as 3. Random String (Alphanumeric + Symbols)
    displayGeneratedPassword(passwordMode())
    print()
    optionMenu()
        
def displayMenu():
    # Change up this design (maybe change project name)
    print("=======================================================")
    print("=======================================================")
    print(r"┏━┓┏━┓┏━┓┏━┓╻ ╻┏━┓┏━┓╺┳┓   ┏━╸┏━╸┏┓╻┏━╸┏━┓┏━┓╺┳╸┏━┓┏━┓")
    print(r"┣━┛┣━┫┗━┓┗━┓┃╻┃┃ ┃┣┳┛ ┃┃   ┃╺┓┣╸ ┃┗┫┣╸ ┣┳┛┣━┫ ┃ ┃ ┃┣┳┛")
    print(r"╹  ╹ ╹┗━┛┗━┛┗┻┛┗━┛╹┗╸╺┻┛   ┗━┛┗━╸╹ ╹┗━╸╹┗╸╹ ╹ ╹ ┗━┛╹┗╸")
    print("=======================================================")
    print("=======================================================")
    print("Text that describes what this does...")
    print()
    optionMenu()

if __name__ == "__main__":
    displayMenu()
        
# end main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #