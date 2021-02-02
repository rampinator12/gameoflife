#Rules:
# 1) Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# 2) Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
# 3) Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# 4) Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

import numpy as np 
import random as rand 


# function that returns a 2D array of random values from zero to 1
def random_state(width,height):

    x = np.random.randint(0,2, size = (width, height))

    return x

#create array a from random state. This is the starting board
a = random_state(5,5)
rows = a.shape[0]
columns = a.shape[1]

#creates an array of same size as incominf array
# and replaces 0 with empty string (space) and 1 with an #
def render(board_state):

    b = np.empty((rows, columns), dtype = str)

    for i in range(0, rows):
        for j in range(0, columns):
            
            if board_state[i,j] == 0:
                b[i,j] = " "
            else:
                b[i,j] = "#"
    return b

#4 functions that count live cells around a corner

def count_cornerTL(board_state):   #top left corner live count

    live_countTL = 0          

    if board_state[0,1] == 1:
        live_countTL += 1
    if board_state[1,1] == 1:
        live_countTL += 1
    if board_state[1,0] == 1:
        live_countTL += 1

    return live_countTL

def count_cornerTR(board_state):  #top right corner live count

    live_countTR = 0  

    if board_state[0, columns - 2] == 1:
        live_countTR += 1
    if board_state[1, columns - 2] == 1:
        live_countTR += 1
    if board_state[1, columns-1] == 1:
        live_countTR += 1
    
    return live_countTR

def count_cornerBL(board_state):  #bottom left corner live count

    live_countBL = 0 

    if board_state[rows - 2, 0] == 1:
        live_countBL += 1
    if board_state[rows - 2, 1] == 1:
        live_countBL += 1
    if board_state[rows - 1, 1] == 1:
        live_countBL += 1

    return live_countBL

def count_cornerBR(board_state):  #bottom right corner live count

    live_countBR = 0 
        
    if board_state[rows-1, columns-2] == 1:
        live_countBR += 1
    if board_state[rows-2, columns-2] == 1:
        live_countBR += 1
    if board_state[rows-2, columns-1] == 1:
        live_countBR  += 1

    return live_countBR

# top_edge_count goes through top edge and creates a row vector with live counts from
# sorrounding cells. its 1st and last value should always be zero

def top_edge_count(board_state):

    live_countTE = np.zeros(columns)

    for i in range(1, columns - 1):

        if board_state[0, i-1] == 1:
            live_countTE[i] += 1
        if board_state[1, i-1] == 1:
            live_countTE[i] += 1
        if board_state[1, i] == 1:
            live_countTE[i] += 1
        if board_state[1, i+1] == 1:
            live_countTE[i] += 1
        if board_state[0, i+1] == 1:
            live_countTE[i] += 1

    return live_countTE

## Now same approach for bottom edge:

def bottom_edge_count(board_state):

    live_countBT = np.zeros(columns)

    for i in range(1, columns - 1):
      
        if board_state[rows-1, i-1] == 1:
            live_countBT[i] += 1
        if board_state[rows-2, i-1] == 1:
            live_countBT[i] +=1
        if board_state[rows-2, i] == 1:
            live_countBT[i] += 1
        if board_state[rows-2, i+1] == 1:
            live_countBT[i] += 1
        if board_state[rows-1, i+1] == 1:
            live_countBT[i] += 1
        
    return live_countBT

#same approach for left edge
def left_edge_count(board_state):

    live_countLE = np.zeros(rows)

    for i in range(1, rows -1):

        if board_state[i-1, 0] == 1:
            live_countLE[i] += 1
        if board_state[i-1,1] == 1:
            live_countLE[i] += 1
        if board_state[i, 1] == 1:
            live_countLE[i] += 1
        if board_state[i+1, 1] == 1:
            live_countLE[i] += 1
        if board_state[i+1, 0] == 1:
            live_countLE[i] += 1

    return live_countLE
    

#same approach for the right edge
def right_edge_count(board_state):

    live_countRE = np.zeros(rows)

    for i in range(1, rows -1):

        if board_state[i-1, columns -1] == 1:
            live_countRE[i] += 1
        if board_state[i-1, columns -2] == 1:
            live_countRE[i] += 1
        if board_state[i, columns -2] == 1:
            live_countRE[i] += 1
        if board_state[i+1, columns -2] == 1:
            live_countRE[i] += 1
        if board_state[i+1, columns -1] == 1:
            live_countRE[i] += 1
        
    return live_countRE

#counts sorrounding live cells in center block
def center_count(board_state):

    live_center_count = np.zeros((rows, columns))

    for i in range(1, rows-1):
        for j in range(1, columns-1):

            if board_state[i-1,j-1] == 1:
                live_center_count[i,j] += 1
            if board_state[i-1, j] == 1:
                live_center_count[i,j] += 1
            if board_state[i-1, j+1] == 1:
                live_center_count[i,j] += 1
            if board_state[i, j+1] == 1:
                live_center_count[i,j] += 1
            if board_state[i+1, j+1] == 1:
                live_center_count[i,j] += 1
            if board_state[i+1, j] == 1:
                live_center_count[i,j] += 1
            if board_state[i+1, j-1] == 1:
                live_center_count[i,j] += 1
            if board_state[i, j-1] == 1:
                live_center_count[i,j] += 1

    return live_center_count


#create a full array same size as starting array with all the live counts in each cell

def live_count_tot(board_state):

    full_count = center_count(board_state)
    full_count[0, 0:columns] = top_edge_count(board_state)
    full_count[rows-1, 0:columns] = bottom_edge_count(board_state)
    full_count[0:rows, 0] = left_edge_count(board_state)
    full_count[0:rows, columns-1] = right_edge_count(board_state)
    full_count[0,0] = count_cornerTL(board_state)
    full_count[0, columns-1] = count_cornerTR(board_state)
    full_count[rows-1,0] = count_cornerBL(board_state)
    full_count[rows-1,columns-1] = count_cornerBR(board_state)

    return full_count

# 1) Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
# 2) Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
# 3) Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
# 4) Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

def new_state(board_state):

    count = live_count_tot(board_state)
    a1 = np.zeros((rows, columns))

    for i in range (0, rows-1):
        for j in range (0, columns-1):

            if board_state[i,j] == 1:

                if count[i,j] <= 1:
                    a1[i,j] = 0
                elif count[i,j] >= 2 and count[i,j] <= 3:
                    a1[i,j] = 1
                else:
                    a1[i,j] = 0

            if board_state[i,j] == 0:

                if count[i,j] == 3:
                    a1[i,j] = 1
                else:
                    count[i,j] = 0

    return a1


print("The starting board is: ")
print(render(a))

print("The second generation board is: ")
a1 = new_state(a)
print(render(a1))

print("The third generation is: ")
a2 = new_state(a1)
print(render(a2))

print("The fourth generation is: ")
a3 = new_state(a2)
print(render(a3))

print("The fifth generation is: ")
a4 = new_state(a3)
print(render(a4))
