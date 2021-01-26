# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 08:04:56 2021

@author: Aripandi
"""

#create a funtion to diplay the game list
def display_list(game_list):
    print('Here is the current list')
    print(game_list)
    
#create funtion to get position
def position_choice():
    
    #set choice as 'wrong'
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        choice = input('Pick a position(0,1,2): ')
        
        if choice not in ['0','1','2']:
            print("Sorry! Enter a Valid position!")
        
    return int(choice)

#get the function to replacement string
def replacement_choice(game_list,position):
    user_position = input('Enter the string to replace: ')
    
    game_list[position] = user_position
    
    return game_list

def gameon_choice():
    #set choice as 'wrong'
    choice = 'wrong'
    
    while choice not in ['Y','N','y','n']:
        choice = input('Pick a position(Y or N) ')
        
        if choice not in ['Y','N','y','n']:
            print("Sorry! Enter a Valid position!")
        
    if choice == 'Y':
        return True
    else :
        return False
    
game_on = True
game_list = [0,1,2]

while game_on:
    
    #Display the current game_list
    display_list(game_list)
    
    #Get the Position
    position = position_choice()
    
    #get the string to replace
    gamelist = replacement_choice(game_list, position)
    
    #Display the replaced game_list
    display_list(game_list)
    
    #call the game_on choice
    game_on = gameon_choice()
    
    
   
        
    

     

    