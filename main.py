from src.LoginAuthentication import *
#os will help with cross platform compatibility to handle file path construction in different OS systems
import os
# Getpass will help to hide the password the user is writing at login for security "reasons"
import getpass
def main():
    # construct the file path to the login data
    loginData = os.path.join('Data','LoginData.json')
    
    print("""
######################################
####### Welcome to SocioScope ########
######################################
# Your Social Network Analysis Tool ##
######################################
######################################
#        LogIn (e) or Exit (x)       #
#           ##############           #""")
    
    choice = input("(e/x)? ")
    if choice == "e":    
        username = input("\nUsername: ")
        passcode = getpass.getpass("Password (will be hidden for your security!): ")
        
    elif choice == "x":
        print("\n:(")
        print("Exiting SocioScope...\n")
        exit()
    pass
main()