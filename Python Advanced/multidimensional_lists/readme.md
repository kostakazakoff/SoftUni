# Exercises: Multidimensional Lists
Problems for in-class lab for the Python Advanced Course @SoftUni. 

## 1. Diagonals
Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ". You should find the matrix's diagonals, prints them and their sum in the format:
"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
## 2. Diagonal Difference
Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
On the first line, you will receive an integer N - the size of a square matrix. The following N lines hold the values for each column - N numbers separated by a single space. Print the absolute difference between the primary and the secondary diagonal sums.
![image](https://user-images.githubusercontent.com/104040753/194773172-92eb2212-373c-4d22-84cf-017e8b3f50b3.png)
## 3. 2x2 Squares in Matrix
Find the number of all 2x2 squares containing identical chars in a matrix. On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". On the following rows, you will receive characters separated by a single space. Print the number of all square matrices you have found.
## 4. Maximal Sum
Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
### Input
- On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
- On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]
### Output
- On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
- On the following 3 lines, print each element of the found submatrix, separated by a single space
![image](https://user-images.githubusercontent.com/104040753/194773344-82996ce0-8358-44e5-9e8c-ad8cd24f52b6.png)
## 5. Matrix of Palindromes
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.
- Rows define the first and the last letter: 
> row 0 -> 'a', row 1 -> 'b', row 2 -> 'c', …

- Columns + rows define the middle letter: 
> column 0, row 0 -> 'a', column 1, row 0 -> 'b', column 2, row 0 -> 'c', …
> column 0, row 1 -> 'b', column 1, row 1 -> 'c', column 2, row 1 -> 'd', …

### Input
- The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
- r and c are integers in the range [1, 26]
## 6. Matrix Shuffling
Write a program that reads a matrix from the console and performs certain operations with its elements.
User input is provided similarly to the problems above - first, you read the dimensions and then the data. 
Your program should receive commands in the format:
"swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix.
A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
- If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly). 
- If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.

Your program should finish when the command "END" is entered.

## 7. Snake Moves
You are tasked to visualize a snake's zigzag path in a rectangular matrix with a size N x M. 

A string represents the snake. It starts moving from the top-left corner to the right. When the snake reaches the end of the row, it slithers its way down to the next row and turns left. The moves are repeated to the very end. 

The first cell is filled with the first symbol of the snake. The second cell is filled with the second symbol, etc. The snake's path is as long as it takes to fill the matrix completely - if you reach the end of the string representing the snake, start again at the first symbol. In the end, you should print the snake's path.
### Input
The input data consists of exactly two lines:
- On the first line, you will receive the dimensions N x M of the field in format: "{rows} {columns}". 
- On the second line, you will receive the string representing the snake

### Output
- You should print the snake's zigzag path of size N x M (rows x columns)

### Constraints
- The dimensions N and M of the matrix will be integers in the range [1 … 12]
- The snake will be a string with length in the range [1 … 20] and will not contain any whitespace characters

## 8. *Bombs
You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. On the last line of input, you will receive indexes - coordinates of several cells separated by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals). One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).
### Input
- On the first line, you are given the integer N - the size of the square matrix.
- The following N lines hold each column's values - N numbers separated by a space.
- On the last line, you will receive the coordinates of the cells with the bombs in the format described above.
### Output
- On the first line, you need to print the count of all alive cells in the format: 
"Alive cells: {alive_cells}"
- On the second line, you need to print the sum of all alive cells in the format: 
"Sum: {sum_of_cells}"
- In the end, print the matrix. A space must separate the cells.
### Constraints
- The size of the matrix will be between [0…1000].
- The bomb coordinates will always be in the matrix.
- The bomb's values will always be greater than 0.
- The integers of the matrix will be in the range [1…10000]. 
## 9. *Miner
You are going to create a game called "Miner".
First, you will receive the size of a square field in which the miner should move. 
On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down". 
In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:

> *- a regular position on the field

> e- the end of the route

> c- coal

> s- miner

The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:

- If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
- If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
- If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
### Input
- Field size - an integer number
- Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
- The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
### Output
- There are three types of output as mentioned above.
### Constraints
- The field size will be a 32-bit integer in the range [0 … 2 147 483 647]
- The field will always have only one "s"

## 10. *Radioactive Mutant Vampire Bunnies
You come across an old JS Basics teamwork game. It is about bunnies that multiply extremely fast. There's also a player that should escape from their lair. You like the game, so you decide to port it to Python because that's your language of choice. The last thing left is the algorithm that determines if the player will escape the lair or not.

First, you will receive a line holding integers N and M, representing the lair's rows and columns.

Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There will be only one player. The bunnies are marked with "B", the player is marked with "P", and everything else is free space, marked with a dot ".". 

Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:

> L - the player should move one position to the left

> R - the player should move one position to the right

> U - the player should move one position up

> D - the player should move one position down

After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny cell or a bunny reaches the player, the player dies. If the player goes out of the lair without encountering a bunny, the player wins.
When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the bunnies spread normally), but there are no more turns. There will be no cases where the moves of the player end before he dies or escapes.
In the end, print the final state of the lair with every row on a separate line. On the last line, print either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where the player has died or the last cell he has been in before escaping the lair.

### Input
- On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
- On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P". All strings will be the same length. There will be only one "P" for all the input
- On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
### Output
- On the first N lines, print the final state of the bunny lair
- On the last line, print:
* If the player won - "won: {row} {col}"
* If the player dies - "dead: {row} {col}"
### Constraints
- The dimensions of the lair are in the range [3…20]
- The directions string length is in the range [1…20]




# Exercise: Multidimensional Lists Problems for exercise and homework for the Python Advanced Course @SoftUni.

## 1. Flatten Lists

Write a program to flatten several lists of numbers received in the following format:

- String with numbers or empty strings separated by "|"

- Values are separated by spaces (" ", one or several)

- Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below

## 2. Matrix Modification

Write a program that reads a matrix from the console and changes its values. On the first line, you will get the matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You will be receiving commands in the following format:

· "Add {row} {col} {value}" – Increase the number at the given coordinates with the value.

· "Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.

If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes are in range [0; len() – 1].

When you receive "END", you should print the matrix and stop the program.

## 3. Knight Game
![image](https://user-images.githubusercontent.com/104040753/193841396-6edd896e-d865-4949-a147-f4b36c00ed0d.png)


Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight.

A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.)

The knight game is played on a board with dimensions N x N.

You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.

Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same number of attacks, remove the top-left one.

### Input

· On the first line, you will receive integer N - the size of the board

· On the following N lines, you will receive strings with "K" and "0"

### Output

· Print a single integer with the number of knights that need to be removed.

### Constraints

· The size of the board will be 0 < N < 30

· Time limit: 0.3 sec. Memory limit: 16 MB

## 4. Easter Bunny

Your task is to collect as many eggs as possible.

On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:

· One bunny - randomly placed in it and marked with the symbol "B"

· Number of eggs placed at different positions of the field and traps marked with "X"

Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.

Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.

### Input

· A number representing the size of the field

· The matrix representing the field (each position separated by a single space)

### Output

· The direction which should be considered as best (lowercase)

· The field positions from which we are collecting eggs as lists

· The total number of eggs collected

### Constraints

· There will NOT be two or more paths consisting of the same total amount of eggs.

## 5. Alice in Wonderland

Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.

You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:

· Alice will be placed in a random position, marked with the letter "A".

· On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.

· There will always be one rabbit hole on the territory marked with the letter "R".

· All of the empty positions will be marked with ".".

After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".

When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.

In the end, the path she walked had to be marked with '*'.

For more clarifications, see the examples below.

### Input

· On the first line, you will be given the integer n – the size of the square matrix

· On the following n lines - matrix representing the field (each position separated by a single space)

· On each of the following lines, you will be given a move command

### Output

· On the first line:

* If Alice steps on the rabbit hole or she go out of the territory, print:

"Alice didn't make it to the tea party."

* If she collected at least 10 bags of tea, print:

"She did it! She went to the party."

· On the following lines, print the matrix.

### Constraints

· Alice will always either go outside the Wonderland or collect 10 bags of tea

· All the commands will be valid

· All of the given numbers will be valid integers in the range [0, 10]

## 6. Range Day

You are participating in a Firearm course. It is a training day at the shooting range.

You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:

· Your position is marked with the symbol "A"

· Targets marked with symbol "x"

· All of the empty positions will be marked with "."

After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:

· "move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".

· "shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").

Validate the positions since they can be outside the field.

Keep track of all the shot targets:

· If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".

· If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".

Finally, print the index positions of the targets that you hit, as shown in the examples.

### Input

· 5 lines representing the field (symbols, separated by a single space)

· N - count of commands

· On the following N lines - the commands in the format described above

### Output

· On the first line, print one of the following:

* If all the targets were shot

"Training completed! All {count_targets} targets hit."

* Otherwise:

"Training not completed! {count_left_targets} targets left."

· Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.

### Constrains

· All the commands will be valid

· There will always be at least one target

## 7. Present Delivery

The presents are ready, and Santa has to deliver them to the kids.

You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.

Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".

Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive. If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or nice). If Santa has been to a house, the cell becomes "-".

Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to these cells, or if he does, he returns to the cell where the cookie was.

If Santa runs out of presents or receives the command "Christmas morning", you should end the program.

Keep in mind that you should check whether all the nice kids received presents.

### Input

· On the first line, you are given the integer m - the count of presents

· On the second - integer n - the size of the neighborhood

· The following n lines hold the values for every row

· On each of the following lines you will get a command

### Output

· On the first line:

* If Santa runs out of presents, but there are still some nice kids left print: "Santa ran out of presents!"

· Next, print the matrix.

· In the end, print one of these messages:

* If he manages to give all the nice kids presents, print: "Good job, Santa! {count_nice_kids} happy nice kid/s."

* "No presents for {count nice kids} nice kid/s."

### Constraints

· The size of the square matrix will be between [2…10].

· Santa's position will be marked with 'S'.

· There will always be at least 1 nice kid.

· There won't be a case where the cookie is on the border of the matrix.
