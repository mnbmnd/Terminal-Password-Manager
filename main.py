##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Terminal Password Manager                                                                                                    #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: mnbmnd                                                                                                                    #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator
import system
import authentication
import storage
import getpass

# The main option menu
def second_option_menu():
    print("Choose an option to continue:")
    print("1. Generate a new password")
    print("2. Check password strength")
    print("3. Quit")
    
    option = int(input("Answer: "))
    system.clear_screen()
    
    if option == 1:
        pass_generator_menu()
    elif option == 2:
        pass_checker_menu()

# Gets the user's inputted password
def get_user_password():
    userPassword = getpass.getpass("Enter your password to continue: ")
    
    return userPassword

# Gets user's option to generate either a passphrase or alphanumeric password
def password_type():
    passwordType = int(input("Answer: "))
    print()
    
    return passwordType

# displays the password strength of an inputted password
def display_pass_strength(generatedPassword=None):
    if generatedPassword is None:
        userPassword = get_user_password()
        
        print("Entropy: {:.1f}".format(entropy.getEntropy(userPassword)))
        print(
            "Time to crack (in years): {:.1f}".format(
                entropy.getTimeToCrack(userPassword)
            )
        )
    else:
        print("Entropy: {:.1f}".format(entropy.getEntropy(generatedPassword)))
        print(
            "Time to crack (in years): {:.1f}".format(
                entropy.getTimeToCrack(generatedPassword)
            )
        )
    print()
    print("To find out more about entropy and time to crack, visit the link below:")
    print(
        "https://auth0.com/blog/defending-against-password-cracking-understanding-the-math/"
    )

# Gets the newly generated password
def get_generated_pass(passwordType):
    generatedPassword = password_generator.generatePassword(passwordType)
    
    return generatedPassword

# Displays the generated password back to the user
def display_generated_pass(passwordType):
    generatedPassword = get_generated_pass(passwordType)
    
    print("Your new password is: ", generatedPassword)
    display_pass_strength(generatedPassword)

# Displays the password checker menu
def pass_checker_menu():
    print()
    print("=" * 18)
    print("Password Strength Checker")
    section("Description")
    print(
        "The Password Checker analyzes a password and estimates how secure \nit is against common attack methods."
    )
    print()
    print("It measures:")
    print(
        " 1. Password entropy – a way of quantifying how unpredictable a password \nis based on its length and the characters used."
    )
    print(
        " 2. Time to crack – an estimate of how long it would \ntake to brute-force the password assuming modern hardware and realistic attack speeds."
    )
    print()
    print(
        "Higher entropy generally means more possible combinations, which increases the \n"
        "time required to crack the password. The checker uses this \n"
        "information to give a practical sense of strength rather than \n"
        "a simple “weak/strong” label."
    )
    print()
    display_pass_strength()
    print()
    second_option_menu()

# Displays the password generator menu
def pass_generator_menu():
    print("")
    print("=" * 18)
    print("Password Generator")
    section("Description")
    print(
        "The Password Generator creates new passwords for you using secure randomness."
    )
    print()
    print("You can choose between:")
    print(
        "1. Passphrase – a sequence of randomly selected words that balances security and memorability"
    )
    print("Example: swell posing gruffly slander onto")
    print()
    print(
        "2. Alphanumeric password – a fully random string of letters and numbers, with an optional \nsymbols setting for additional complexity."
    )
    print("Example: a9Fq7XrL2mP8ZKcE")
    print()
    display_generated_pass(password_type())
    print()

# Sections formatter
def section(title: str):
    print()
    print(f"[ {title} ]")

# Splash screen art (First screen that shows)
def splash():
    print()
    print("Password Manager")
    print()
    input("Press enter to continue...")
    system.clear_screen()

# The main menu, shows after splash screen
def main_menu():
    section("Overview")
    print(
        "This project is a terminal-based password utility that helps\nyou both generate strong passwords and evaluate existing ones,\n"
        "it is designed to be simple to use, transparent in how it works,\nand focused on real-world security rather than gimmicks.\n"
    )
    print("To get started, choose an option below:\n")
    print("1. Setup/update your master password")
    print("2. Login with your master password")
    print()
    masterCredentials = authentication.set_master_credentials()
    storage.save_master_credentials(masterCredentials[0], masterCredentials[1], masterCredentials[2])
    second_option_menu()

# Main
if __name__ == "__main__":
    splash()
    main_menu()
# END_MAIN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #