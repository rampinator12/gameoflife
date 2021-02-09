#New approach: make one funtion that counts live/dead cells sorrounding it, and one that checks if
#index is valid or not (ie still in the matrix) Then create a new_state that uses this function only 
# to determine if in next generation cell remains dead or alive ect.

import numpy as np
import random as rand
from matplotlib import pyplot as plt 

# function that returns a 2D array of random values from zero to 1
def random_state(width,height):

    x = np.random.randint(0,2, size = (width, height))

    return x

#create array a from random state. This is the starting board
a = random_state(10,10)
rows = a.shape[0]
columns = a.shape[1]

#if index is outside (0to rows-1, 0to columns-1) returns False, if within bounds returns true
def is_valid_index(i, j):

    if i >= 0 and i < rows:
        if j >= 0 and j < columns:
            return True
    else:
        return False

#goes around a cell to look at 8 neighbors, if alive and within index bounds adds one
def count_neighbors(board_state, i, j):

    count = 0

    if is_valid_index(i-1, j-1) == True:
        if board_state[i-1, j-1] == 1:
            count +=1
    if is_valid_index(i-1, j) == True:
        if board_state[i-1, j] == 1:
            count +=1
    if is_valid_index(i-1, j+1) == True:
        if board_state[i-1, j+1] == 1: 
            count +=1
    if is_valid_index(i, j+1) == True:
        if board_state[i, j+1] == 1:
            count +=1
    if is_valid_index(i+1, j+1) == True:
        if board_state[i+1, j+1] == 1: 
            count +=1
    if is_valid_index(i+1, j) == True:
        if board_state[i+1, j] == 1:
            count +=1
    if is_valid_index(i+1, j-1) == True:
        if board_state[i+1, j-1] == 1:
            count +=1
    if is_valid_index(i, j-1) == True:
        if board_state[i, j-1] == 1:
            count +=1

    return count

# creates same size array with tot counts of live sorrounding cells
def count_array(board_state):

    count_tot = np.zeros((rows,columns))

    for i in range(0, rows):
        for j in range(0, columns):
            count_tot[i,j] = count_neighbors(board_state, i, j)
    
    return count_tot

#creates next gen board (same analysis as last game)
def new_state(board_state):

    count = count_array(board_state)
    next_gen = np.zeros((rows, columns))

    for i in range(0, rows-1):
        for j in range(0, columns -1):

            if board_state[i,j] == 1:

                if count[i,j] <= 1:
                    next_gen[i,j] = 0
                elif count[i,j] >= 2 and count[i,j] <= 3:
                    next_gen[i,j] = 1
                else:
                    next_gen[i,j] = 0
            
            if board_state[i,j] == 0:

                if count[i,j] == 3:
                    next_gen[i,j] = 1
                else:
                    next_gen[i,j] = 0

    return next_gen

#sets current board to initial board state, prints out matrix form
current_board = a
print(current_board)

#first output image is a, yellow cells are alive purple are dead
plt.figure(figsize = (rows, columns))
plt.imshow(a)
plt.title("This is the starting generation")
plt.show()

#for loop that creates and shows image of next generations with 9 we have 10 total boards
for n in range(2,11):

    b = str(n)
    current_board = new_state(current_board)
    print(current_board)
    plt.imshow(current_board)
    plt.title("Generation: " + b)
    plt.show()





        

