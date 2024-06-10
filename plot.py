# Program to plot a graph based on the users input
# Dhiya Ramadhar
# 22/05/2021

import math

function = input("Enter a function f(x):\n")

for row in range(10, -11, -1):
    for col in range (-10, 11): 
        x = col 
        funct= round(eval(function)) # Calculates the function according to the value of x
        if col == 0 and row == 0 and not row == funct: # to get the centre of the grid; at row == funct are the points of the graph ie where the *'s will go
            print("+", end='')
        elif row == 0 and not row == funct:
            print('-', end='')
        elif col == 0 and not row == funct:
            print("|", end='')
        elif row == funct:
            print("*", end='')
        else:
            print(' ', end='')
    print()