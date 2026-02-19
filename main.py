#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: main.py                                                               #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import menus
import system
import authentication


def run_program():
    menus.splash()

    # Program goes to login if user credentials are already setup
    if not authentication.has_master_credentials():
        menus.show_setup_menu()

    loginSuccessful = menus.show_login_menu()

    if loginSuccessful:
        print("\nWelcome,\033[1m", system.whoami(), "\033[0m")
        menus.section_cutter()
        input("Press enter to continue to main menu... ")

        while True:
            system.clear_screen()
            mainMenuChoice = menus.show_main_menu()

            if mainMenuChoice == 1:
                system.clear_screen()
                menus.show_passgen_menu()
            elif mainMenuChoice == 2:
                system.clear_screen()
                menus.show_passcheck_menu()
            elif mainMenuChoice == 3:
                system.reset()
                menus.show_goodbye()
                break
    else:
        print("\nLogin Unsuccessful")
        input("\nPress enter to exit... ")
        system.reset()


if __name__ == "__main__":
    try:
        run_program()
    except KeyboardInterrupt:
        system.reset()
        menus.show_goodbye()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
