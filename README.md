# Text-based Graph Drawer

## Description
The `plot.py` is a Python program that draws a text-based graph of a mathematical function `f(x)`. The program uses axis limits of -10 to 10 and only plots discrete points i.e., points with integer value ordinates.

The program uses nested loops to print the entire area of the graph (i.e., an outer loop for rows and an inner one for columns), keeping track of the current `x` and `y` values. Whenever the (rounded) value of the function `f(x)`, entered by the user, is equal to the current `y` value, it outputs "*" (an asterisk), otherwise, it outputs either the appropriate axis character or a space.

The program supports the entering of arbitrary functions by obtaining user input in the form of a string, then within the inner loop, whenever `f(x)` is to be calculated, it uses the Python `eval` function on that string.

## How to Run
To run the program, open a terminal, navigate to the directory containing `plot.py`, and type `python plot.py`.
Alternately, if you have VS Code install python. Then select an interpreter by clicking Control+Shift+P and trying Python: Select Interpreter and choose one. Navigate to the directory containing `plot.py` and run it.

## User Interaction
The program will ask you to enter a function and will draw a text-based graph based on the function.