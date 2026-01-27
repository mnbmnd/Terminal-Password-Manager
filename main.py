##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Password Strength Checker & Generator                                                                                        #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: pchstpch                                                                                                                  #
#                                                                                                                                            #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator

def getUserPassword():
    userPassword = input("Please enter your password: ")
    return userPassword
 
 # TODO: Change function name to something more suitable
 def passwordLength():
    length = int(input("Answer: "))
    while (length < 8) | (length > 32):
        print("Please enter a number between 8 and 32 (inclusive) to continue!")
        print()
        length = int(input("Answer: "))
    return length

def passwordMode():
    mode = int(input("Answer: "))
    return mode

def getGeneratedPassword():
    generatedPassword = password_generator.generatePassword(passwordLength(), passwordMode())
    return generatedPassword

def displayPasswordEntropy():
    print("Entropy: {:.1f}".format(entropy.getEntropy(getUserPassword())))
    
def displayTimeToCrack():
    print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(getUserPassword())))

def displayGeneratedPassword():
    print("Your generated password is: " + getGeneratedPassword())
    

def passwordCheckerMenu():
    print("PASSWORD STRENGTH CHECKER")
    print("Welcome to Password Strength Checker")
    # TODO: Add a section detailing what this password checker does and references to pass entropy

def passwordGeneratorMenu():
    print("PASSWORD GENERATOR")
    print("Welcome to Password Generator!")
    print("Please answer the questions below to generate a password to your liking")
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
    print("How long would you like your password to be? (Enter a number from 8-32 inclusive)")
    
        
def displayMenu():
    print("==================================================================")
    print("==================================================================")
    print()
    print()
    print("==================================================================")
    print("==================================================================")

if __name__ == "__main__":
    displayMenu()
        
# end main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #