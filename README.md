# 2x2-Rubiks-Cube-Solver
**Used Python and a 2 sided Breadth First Search to solve a 2x2 Rubiks Cube.**
https://youtu.be/ZHxLO6fubaU
Inspired by project in MIT 6.006. Created from scratch uniquely.

## Cube format
**Created the cube API, Algorithm, and GUI from scratch.** Each of the 6 sides has 4 different squares resulting in 24 squares. Furthermore, there are a total of 8 corner pieces that make up the cube, each of which has 3 orientations and therefore goes along with the 24 squares. 

I defined each of the 24 subsections of each side as a string with 'xyz' as the format where x is the color immediately facing and the y and z go in clockwise order around the cube for that corner. 

I went around the cube and assigned each side with a fixed number representing the solved state. For example, 0, 1, 2, 3 are the 4 parts of the front facing white side where 0 is top left and the ohter go in clockwise order.

There are 12 moves that can be performed on the cube. Right, left, top, bottom, front, back. Each of these also have their counter clockwise motions so 6x2 = 12 moves. Each of these 12 manipulate half of the cube so 12 squares. To make these moves, I created dictionaries for each of the 6 clockwise for which sub-square rotates from the original to the following position. To do the primes, I just switched the keys and values.

## Solution
Solving this problem is especially tricky due to the huge amount of possible permutations of the cube. There are 24 sub-squares and that comes out to 24P24 = **24!.** This is on the magnitude of 10^23. There are less than this amount due to certain situations but the number is still enormous.

To create the tree, I would have to run each of the moves and run all the moves from the moves which gets very big. 12^height of the tree. I was able to limit this size through creating a dict of visited positions so it wouldn't redo the action for previously visited permutations. 

I started with creating a 1 sided BFS but that would hit the recursion limit since the branching tree would get too large. To fix this, I used a **2 sided BFS by alternating creating branches from the start and the ending solution.** It would create the trees and check if the opposite side had already found the point. If it did, it would return the connecting point. 

During all of this, each node saves it's parent (for the front branching) or child (for the back branching). To find the route it took I recursively found the parent from the connecting node and then all the children of that point. This resulted in an array of the positions it took from the scrambled to solved.

## Learning
This project applied my use of **graph theory and Breadth First Search**. I improved my ability in Python and recursion. I also experimentally found the max moves to solve a 2x2 cube to be **11 moves** since I could never find a solution that took longer

Learned how to use tkinter library to make GUI for the project

