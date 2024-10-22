# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:56:47 2021

@author: Aman Bhalla
"""
import numpy as np
from matplotlib import pyplot as plt



def createboard(): 
    
    '''
    Creates a 7 column, 6 row, numpy 2d array consisting of zeros to become the gameboard
    
    Returns
    -------
    array = 7 column, 6 row matrix (numpy array) 
    
    '''
    
    array = np.zeros((6,7), dtype = int)
    return(array)



def player1token():
    
    '''
    Asks player 1 for their chosen column, if column out of range/full they are asked again
    
    Returns
    -------
    player1input = Player 1 chosen column (integer)

    '''
    
    correctinput = False
    
    while correctinput == False:
        
        # Asks player 1 for input
        player1input = int(input('Player 1, what column would you like to place a token in? (0-6)'))
        
        # If input out of range, loop back to asking input
        if player1input > 6 or player1input < 0:
            print("Column value out of range! Please choose a value from 0-6.")
        # If column filled, loop back to asking input
        elif (columnfilled(player1input)) == True:
            print("Column full! Please choose a different column.")
        # If input correct, return the input
        else:
            correctinput = True
            return(player1input)
        
        

def player2token():
    
    '''
    Asks player 2 for their chosen column, if column out of range/full they are asked again
    
    Returns
    -------
    player2input = Player 2 chosen column (integer)

    '''
    
    correctinput = False
    
    while correctinput == False:
        
        # Asks player 2 for input
        player2input = int(input('Player 2, what column would you like to place a token in?(0-6)')) 
        
        # If input out of range, loop back to asking input
        if player2input > 6 or player2input < 0:
            print("Column value out of range! Please choose a value from 0-6")
        # If column filled, loop back to asking input
        elif (columnfilled(player2input)) == True:
            print("Column full! Please choose a different column.")
        # If input correct, return the input
        else:
            correctinput = True
            return(player2input)



def columnfilled(playerinput):
    
    '''
    Checks if the top slot of the chosen column is equal to 1 or 2 and returns whether this is true
    
    Parameters
    ----------
    playerinput : player 1 or 2 column input

    Returns
    -------
    Columnfill = True, becomes true if column full (boolean)

    '''
    
    if (board[0,playerinput]) == 1 or (board[0,playerinput]) == 2:
        columnfill= True
        return(columnfill)
        
    
 
def player1move(tokencol):
    
    '''
    Takes player1 column input and changes the next avaliable point in that column into a 1
    
    Parameters
    ----------
    tokencol : Input of players chosen column (integer)

    Returns
    -------
    board = board matrix with player 1 token in correct column (numpy array)
    
    '''
    
    #Creating 1d array for specific column
    col1d=board[:,tokencol]
    tokencounter=0
    
    #Checks if there is a player1(1) or player2(2) token in column and places token
    for i in range(0,6):
        if col1d[i]== 1 or col1d[i]==2:
            tokencounter = tokencounter+1
    board[(5-tokencounter),tokencol]=1
    return(board)



def player2move(tokencol):
    
    '''
    Takes player2 column input and changes the next avaliable point in that column into a 2
    
    Parameters
    
    ----------
    tokencol : Integer, input of players chosen column. 

    Returns
    -------
    board = board matrix with player 2 token in correct column (numpy array) 
    
    '''
    
    #Creating 1d array for specific column
    col1d=board[:,tokencol]
    tokencounter=0
    
    #Checks if there is a player1(1) or player2(2) token in column and places token
    for i in range(0,6):
        if col1d[i]== 1 or col1d[i]==2:
            tokencounter = tokencounter+1
    board[(5-tokencounter),tokencol]=2
    return(board)



def wincheck():
    
    '''
    Splits the board into every possible column/row of 4 and compares to a reference array to see if they are equal and outputs if there is a win
    
    Returns
    -------
    nowinner = False, Neither player 1 or player 2 have connected 4 (boolean)
    winner = True, Either player 1 or player 2 have connected 4 (boolean)

    '''
    
    # Defines needed variables
    pconnectedfour=False
    p2connectedfour=False
    playerw=np.array([1,1,1,1])
    player2w=np.array([2,2,2,2])
    nowinner = False
    winner = True
    
    # Vertical wincheck :
    # j loop checks 3 column blocks vertically dowards y = (0-3),(1,4),(2-5)
    for j in range(0,3):
        
        # i loop creates a 1d column array 7 times for each column block
        for i in range(0,7):
            col1d=board[0+j:4+j,i]
            
            # Compares player 1 win array to current column array
            pconnectedfour = np.array_equal(playerw,col1d)
            # Compares player 2 win array to current column array
            p2connectedfour = np.array_equal(player2w,col1d)
            
            # If the arrays are equal, return winner = True and end the wincheck
            if pconnectedfour == True:
                return(winner)
            elif p2connectedfour == True:
                return(winner)
            else:
                nowinner = False
                
    # Horizontal wincheck :
    # j loop checks 4 row blocks horizontal to the right x = (0-3),(1,4),(2-5),(3-6)
    for j in range(0,4):
        
        # i loop creates a 1d row array 6 times for each row block
        for i in range(0,6):
            row1d=board[i,0+j:4+j]
            
            # Compares player 1 win array to current row array
            pconnectedfour = np.array_equal(playerw,row1d)
            # Compares player 2 win array to current row array
            p2connectedfour = np.array_equal(player2w,row1d)
            
            # If the arrays are equal, return winner = True and end the wincheck
            if pconnectedfour == True:
                return(winner)
            elif p2connectedfour == True:
                return(winner)
            else:
                nowinner = False
                
    def a(y,x):
        
        '''
        Takes a starting coordinate, and creates a 1d array for the other 3 values positively diagonal to it
        
        Parameters
        ----------
        y : y value of starting coordinate (integer)
        x : x value of starting coordinate (integer)
            
        Returns
        -------
        nowinner = False, Neither player 1 or player 2 have connected 4 (boolean)
        winner = True, Either player 1 or player 2 have connected 4 (boolean) 
        
        ''' 
        
        # Defines diagonal array                    
        diag1d = np.array([board[y,x]])
        
        # Appends diag1d with the 3 other points positively diagonal to the starting point
        for i in range (1,4):
            diag1d = np.append(diag1d,(board[y+i,x+i]))
            
        # Compares diag1d with references win arrays     
        pconnectedfour = np.array_equal(playerw,diag1d)
        p2connectedfour = np.array_equal(player2w,diag1d)
        
        # If 4 in a diagonal has been confirmed the function stops and returns True, otherwise False is returned
        if pconnectedfour == True:
            return(winner)
        elif p2connectedfour == True:
            return(winner)
        else:
            return(nowinner)
    
    # Inputs all possible starting locations for a positive diagonal into function a, if any location comes up as true, the wincheck stops
    if True in (a(0,3),a(0,2),a(1,3),a(0,1),a(1,2),a(2,3),a(0,0),a(1,1),a(2,2),a(1,0),a(2,1),a(2,0)):
        return(True)
    else:
        nowinner = False
        
    def b(y,x):
        '''
        Takes a starting coordinate, and creates a 1d array for the other 3 values negatively diagonal to it
        
        Parameters
        ----------
        y : y value of starting coordinate (integer)
        x : x value of starting coordinate (integer)
            
        Returns
        -------
        nowinner = False, Neither player 1 or player 2 have connected 4 (boolean)
        winner = True, Either player 1 or player 2 have connected 4 (boolean) 
        
        '''     
        
        # Defines diagonal array              
        diag1d = np.array([board[y,x]])
        
        # Appends diag1d with the 3 other points negatively diagonal to the starting point
        for i in range (1,4):
            diag1d = np.append(diag1d,(board[y+i,x-i]))
            
        # Compares diag1d with references win arrays 
        pconnectedfour = np.array_equal(playerw,diag1d)
        p2connectedfour = np.array_equal(player2w,diag1d)
        
        # If 4 in a diagonal has been confirmed the function stops and returns True, otherwise False is returned
        if pconnectedfour == True:
            return(winner)
        elif p2connectedfour == True:
            return(winner)
        else:
            return(nowinner)
        
    # Inputs all possible starting locations for a positive diagonal into function b, if any location comes up as true, the wincheck stops
    if True in (b(0,3),b(0,4),b(1,3),b(0,5),b(1,4),b(2,3),b(0,6),b(1,5),b(2,4),b(1,6),b(2,5),b(2,6)):
        return(True)
    else:
        nowinner = False
    
    return(nowinner)    
    
       
def plottingboard():
    '''
    Flips the board, then checks the value of each point on the board and plots the appropriate colour (0 being a white dot)
    
    Returns
    -------
    plt.show() = Final board (matplotlib scatter graph)

    '''
    
    # Flips board                  
    flippedboard = np.flipud(board)
    plt.title('Connect 4')
    
    # For j and for i check each point on board
    for j in range(0,6):
        for i in range(0,7):
            
            # Stores y and x value of current point
            y=(0+j)
            x=(0+i)
            
            # Stores point
            slot=flippedboard[y,x]
            
            # If point is 0 a white circle is plotted, if 1 a yellow circle, if 2 a red circle
            if slot == 0:
                plt.plot(x,y,'wo')
            if slot == 1:
                plt.plot(x,y,'yo')
            if slot == 2:
                plt.plot(x,y,'ro')
    return(plt.show())
 
       
print("Welcome to Connect 4!")


# Creates board
board=createboard()
gamewin = False


while gamewin == False:
    
    p1col=player1token() #p1col assigned value of player 1 chosen column from p1token function (int)
    player1move(p1col) #player1move moves the token based off of player 1 chosen column
    print("Player 1 has chosen column", p1col)
    plottingboard() # Plots gameboard
    gamewin = wincheck() #Checks if the player has won as the wincheck occurs after the player move
    if gamewin == True : #If the player has won the game the while loop is stopped
        print("Player 1 Wins")
        break
    
    p2col=player2token() #p2col assigned value of player 2 chosen column from p2token function (int)
    player2move(p2col) #player2move moves the token based off player 2 chosen column
    print("Player 2 has chosen column", p2col)
    plottingboard() # Plots gameboard
    gamewin = wincheck() #Checks if player 2 has won as the wincheck occurs after player 2 move
    if gamewin == True : #If player 2 has won the game the while loop is stopped
        print("Player 2 Wins")
        break
    



