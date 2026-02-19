#######################################################################################
# Author: Muneeb Mennad                                                              #
# Project Name: Passman                                                             #
# File Name: system.py                                                             #
# Project Start: 2026-01-24                                                         #
# Github: https://github.com/mnbmnd                                                  #
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import subprocess


def clear_screen():
    subprocess.run(["clear"])


# Quits program and clears the screen
def reset():
    subprocess.run(["reset"])


# Gets system username
def whoami():
    whoami = subprocess.run(["whoami"], capture_output=True, text=True)

    return whoami.stdout.replace(
        "\n", ""
    )  # Returns output of whoami without the newline chr


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
