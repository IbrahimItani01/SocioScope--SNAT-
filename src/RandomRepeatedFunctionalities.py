# This file contains some repeated code that I deemed important to put as functions but they are not a core operation in the program
import os
import json

UsersDBPath = os.path.join('Data','USersDb.json')
IDsDBPath = os.path.join('Data','AvailableIDs.json')
hashTablePath = os.path.join('Data','IDtoMatIndexTable.json')

def ExitMessage():
    # O(1)
    print("\nExiting SocioScope...\n")
    exit()
    
def checkChoice(choice,answ1,answ2,answ3=None,answ4=None,answ5=None,answ6=None,answ7=None,answ8=None):
    # O(1)
    try:
        if answ3 == None and answ4==None and answ5==None and answ6==None and answ7==None and answ8==None:
            while choice != answ1 and choice != answ2:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2})? ")
                
        if answ4 == None and answ5==None and answ6==None and answ7==None and answ8==None and answ3 != None:
            while choice != answ1 and choice != answ2 and choice!=answ3:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3})? ")
                
        elif answ5 == None and answ6==None and answ7==None and answ8==None and answ3!=None and answ4!=None:
            while choice != answ1 and choice != answ2 and choice!=answ3 and choice!=answ4:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3}/{answ4})? ")
                
        elif answ6==None and answ7==None and answ8==None and answ3!=None and answ4!=None and answ5!=None:
            while choice != answ1 and choice != answ2 and choice!=answ3 and choice!=answ4 and choice!=answ5:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3}/{answ4}/{answ5})? ")
                
        elif answ7==None and answ8==None and answ3!=None and answ4!=None and answ5!=None and answ6!=None:
            while choice != answ1 and choice != answ2 and choice!=answ3 and choice!=answ4 and choice!=answ5 and choice!=answ6:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3}/{answ4}/{answ5}/{answ6})? ")
                
        elif answ8==None and answ3!=None and answ4!=None and answ5!=None and answ6!=None and answ7!=None:
            while choice != answ1 and choice != answ2 and choice!=answ3 and choice!=answ4 and choice!=answ5 and choice!=answ6 and choice!=answ7:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3}/{answ4}/{answ5}/{answ6}/{answ7})? ")
                
        else:
            while choice != answ1 and choice != answ2 and choice!=answ3 and choice!=answ4 and choice!=answ5 and choice!=answ6 and choice!=answ7 and choice!=answ8:
                print("\nInvalid choice, try again!")
                choice = input(f"({answ1}/{answ2}/{answ3}/{answ4}/{answ5}/{answ6}/{answ7}/{answ8})? ")
                
        return choice
    
    except KeyboardInterrupt:
        print("\nYou pressed a kill program shortcut")
        ExitMessage()
    
def loadUsers():
    # O(1)
    with open(UsersDBPath,'r') as file:
        usersData = json.load(file)
    return usersData

def updateUser(userData):
    # O(1)
    with open(UsersDBPath,'w') as file:
        file.seek(0)
    # writes the userData to the JSON file
        json.dump(userData,file,indent=4)
        
def updateUsersDB(usersData):
    # O(NlgN), where N in the number of Users in the json file
    
    #Always sort the users File by ID in increasing order
    sortedUsersData = dict(sorted(usersData.items(),key=lambda item: int(item[0])))
    with open(UsersDBPath,'w') as file:
    #moves file pointer to the beginning of the JSON file
        file.seek(0)
    # writes the userData to the JSON file
        json.dump(sortedUsersData,file,indent=4)
                
def loadAvailableIdsListSorted():
    # O(NlgN), N being the number of available ids to sort
    
    #Use the sort function to sort the retrieved list of available IDs
    from src.Algorithms import sortAvailableIDsFile
    
    with open(IDsDBPath,'r') as file:
        availableIds = json.load(file)
    Idslist = availableIds["availableIds"]
    if len(Idslist)==0:
        return []
    
    sortAvailableIDsFile(Idslist,0,len(Idslist)-1)
    return Idslist

def updateAvailableIdsList(IdsList):
    # O(1)
    with open(IDsDBPath,'w') as file:
        json.dump({"availableIds":IdsList},file,indent=4)
        
def searchResult(data,withYOB=None):
    print("\n")
    for user_id, user_info in data.items():
        print(f"ID: {user_id}")
        print(f"Name: {user_info['name']}")
        if withYOB is True:
            print(f"Birth Year: {user_info['birthYear']}")
        print("-" * 40)  # Separator line

def displayDictDataNicely(data):
    print("\n")
    for user_id, user_info in data.items():
        print(f"ID: {user_id}")
        print(f"Name: {user_info['name']}")
        print(f"Bio: {user_info['bio']}")
        print(f"Profile Picture: {user_info['profile_picture']}")
        print(f"Birth Year: {user_info['birthYear']}")
        print(f"Interests: {user_info['interests']}")
        print("-" * 40)  # Separator line
        
def displayRecommendationNicely(data,area):
    print("\n")
    if area == "a" or area == "f":
        for user_id, user_info in data.items():
            print(f"ID: {user_id}")
            print(f"Name: {user_info}")
            print("-" * 40)  # Separator line
    elif area == "i":
        for user_id, user_info in data.items():
            print(f"ID: {user_id}")
            print(f"Name: {user_info[0]}")
            print(f"Interests: {" - ".join(user_info[1])}")
            print("-" * 40)  # Separator line

def deleteAllData():
    with open(UsersDBPath,'w') as file:
        file.dump({},file)
    with open(IDsDBPath,'w') as file:
        file.dump({},file)
    print("\nAll Data in SocioScope has been deleted!")
