# Stewards
"It's only when you are flying above that you realize how incredible the Earth really is."
As you know, stewards are needed for every single flight. Today you will be that one steward, and you will be assisting the passengers in finding their seats.

You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}". You will also be given two more sequences of numbers only.
- First, you have to take the first number of the first sequence and the last number of the second sequence.
- Next, take the sum of those two numbers and find its ASCII character.
- Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger is seated, and the seat is considered taken. Remove both numbers from their sequences.
* If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last, last becomes first).
* If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track of all rotations made.

The program should end under the following circumstances:
- You have found 3 (three) seat matches 
- You have made a total of 10 rotations
### Input
- On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
- On the second and the third line, you will be given two more sequences - integers separated by a comma and a space ", "
### Output
When the program ends, print the following on two different lines:
- Seat matches: {matches separated by comma and space}
- Rotations count: {total rotations made}
### Constraints
- All integers will be in the range [1, 100]
- All letters will be in the range [A-Z]
- You will never run out of numbers in your sequences before the program ends
- You will never have more than one match at a time

# CRUD
The abbreviation CRUD expands to Create, Read, Update and Delete.
These are the four fundamental operations in a database.

In the beginning, you will be given a matrix with 6 rows and 6 columns representing a table with information. 

It consists of:
- Letters - on one or many positions in the table
- Numbers - on one or many positions in the table
- Empty positions - marked with "."

Next, you will receive your first position on the table in the format "({row}, {column})"

On the following lines, until you receive "Stop" you will be receiving commands in the format:
- "Create, {direction}, {value}"
    - The direction could be "up", "down", "left" or "right"

    - If you step in an empty position, create the given value on that position. E.g., if the given value is "A", and the position is empty (".") - change it to "A"

    - If the position is NOT empty, do NOT create a value on that position

- "Update, {direction}, {value}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, update the position with the given value. E.g., if the given value is "h", and the position's value is "12" - change it to "h"

    - If the position is empty, do NOT update the value on that position

- "Delete, {direction}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, delete it, and empty the position. E.g., if the given position's value is "h" - change it to "."

    - If the position is already empty, do NOT delete it

- "Read, {direction}"
    - The direction could be "up", "down", "left" or "right"

    - If you step on a letter or number, print it on the console

    - If the position is empty, do NOT read it

    - You can make only ONE move at a time in the given direction for each command given.

    - In the end, print the final matrix.

### Input
- On the first 6 lines - a matrix with positions separated by a single space
* Letters are in the range [a-zA-Z]
* Numbers are in the range [-100, 100]
- On the next line - your first position in the format: "({row}, {column})"
- On the following lines until you receive the command "Stop" - commands in the format shown above
### Output
- In the end, print the final matrix, each row on a new line, each position separated by a single space.
### Constraints
- You will always receive valid coordinates
- You will always receive directions in the range of the table
- You will always receive letters or numbers

# Song Creator
Create a function called add_songs().
It receives one or many tuples.
Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position.
The list can consist of one, many, or no strings - each representing a line of the lyrics of the song. 
The function collects the information and concatenates the lyrics for each song (each string on a different line). If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.

In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"

If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.

### Input:
There will be no input, just tuples passed to your function.
### Output:
Return the desired result as described above.
### Constraints:
You will always have a song's name on the first position of the tuple.

# Collecting Eggs
Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.

On the first line, you will receive a sequence of numbers, each representing an egg with its size.
On the second line, you will receive another sequence of numbers, each representing a piece of paper with its size. 

You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50. Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.

You should comply with the following conditions:
- If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before it is wrapped with a piece of paper.
- If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg in the box and remove both from the sequences.
- Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them in a box.

During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck to him. You should remove this egg from the sequence before it is wrapped with a piece of paper. 
Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of paper positions to bring the good luck back to Old MacDonald.

Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.

### Input
- In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space ", " in the range [-100, 100]
- In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and space ", " in the range [1, 100]

### Output
- On the first line:

    - If you have at least one box filled, print: 
    "Great! You filled {total count} boxes."
    - If you couldn't fill any boxes, print:
    "Sorry! You couldn't fill any boxes!"

- On the following lines, print the eggs left or pieces of paper left if there are any:

    - Eggs left: {left eggs joined by ", "}
    - Pieces of paper left: {left pieces of paper joined by ", "}

### Constraints
You will always have at least one egg and at least one piece of paper.

# Exit Founder

Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out. Monitor their moves closely and find out who the winner will be!

First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they are received determines the order in which they will take turns. The first player starts first.

Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
- Only one Exit - marked with the "E" letter
- Trap (one, many, or none) - marked with the "T" letter
- Wall (one, many, or none) - marked with the "W" letter
- Empty positions will be marked with "."

In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will be receiving coordinates for each of the players. They will be taking turns and stepping on different positions on the board until one of them find the Exit or falls into a Trap. Here are the rules:
- If a player hits the letter "E", he escapes the maze and wins the game.
Print "{player} found the Exit and wins the game!" and end the program.
- If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
Print "{player} is out of the game! The winner is {winner}." and end the program.
- If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
Print "{player} hits a wall and needs to rest."
- If a player steps on an empty position ".", nothing happens. 

Both players can step in the same position at the same time.

### Input
- On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
- On the following 6 lines, you will receive the maze board (elements will be separated by a space)
- On the following lines, you will be receiving coordinates in the format: "({row}, {column})"

### Output
- You should print the output as described above.
- The input coordinates will always be valid.

# Shopping Cart
Peter has decided to invite some guests. He should go shopping, but he will need help because 
there are too many things he needs to remember. Would you assist him?

Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:  "Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
- Soup: 3
- Pizza: 4
- Dessert: 2

Once you reach the limit of a meal, you should stop adding products to that meal.
The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the type of meal, and the second is the product for the meal. You need to take each argument and make a dictionary with the meal's name as a key and the products as a value of the corresponding key.

There are some additional requirements:
- If you receive the same product for the same meal more than once, you must not add it again.
- If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart - just sort and return the desired result as described below.
In the end, sort the meals by the number of bought products in descending order. If there are meals with an equal number of products, sort them (the meals) by their name in ascending order (alphabetically). For each meal sort its products in ascending order (alphabetically).
Return an output as described below.

Note: Submit only the function in the judge system

### Input
- There will be no input, just parameters passed to your function
### Output
- Return a string for each of the 3 types of a meal of the sorted result in the format:

"{meal_type}:"

" - {first_product_added}"

" - {second_product_added}"

…

" - {Nth_product_added}"

- If there are no products given for a meal, return just its name in the format shown above.
- If there are NO products in the cart (at all), return the message: "No products in the cart!"
### Constrains
- Each tuple given will always contain the type of meal in the first position and a product in the second.
- There will be no other meals passed than "Soup", "Pizza", and "Dessert".

# Ramen Shop
You will be given two sequences of integers representing bowls of ramen and customers. Your task is to find out if you can serve all the customers.

Start by taking the last bowl of ramen and the first customer. Try to serve every customer with ramen until we have no more ramen or customers left:
- Each time the value of the ramen is equal to the value of the customer, remove them both and continue with the next bowl of ramen and the next customer.
- Each time the value of the ramen is bigger than the value of the customer, decrease the value of that ramen with the value of that customer and remove the customer. Then try to match the same bowl of ramen (which has been decreased) with the next customer.
- Each time the customer's value is bigger than the value of the ramen bowl, decrease the value of the customer with the value of the ramen bowl and remove the bowl. Then try to match the same customer (which has been decreased) with the next bowl of ramen.

### Input
- On the first line, you will receive integers representing the bowls of ramen, separated by a single space and a comma ", ".
- On the second line, you will receive integers representing the customers, separated by a single space and a comma ", ".
### Output
- If all customers are served, print: "Great job! You served all the customers."
- Print all of the left ramen bowls (if any) separated by comma and space in the format: "Bowls of ramen left: {bowls of ramen left}"
- Otherwise, print: "Out of ramen! You didn't manage to serve all customers."
- Print all customers left separated by comma and space in the format "Customers left: {customers left}"

# Martian Explorer
Your rover has landed on Mars, and it needs to find resources to start humanity's first interplanetary colony.
You will receive a 6x6 field on separate lines with:
- One rover - marked with the letter "E"
- Water deposit (one or many) - marked with the letter "W"
- Metal deposit (one or many) - marked with the letter "M"
- Concrete deposit (one or many) - marked with the letter "C"
- Rock (one or many) - marked with the letter "R"
- Empty positions will be marked with "-"

After that, you will be given the commands for the rover's movement on one line separated by a comma and a space (", ").
Commands can be: "up", "down", "left", or "right".
For each command, the rover moves in the given directions with one step, and it can land on one of the given types of deposit or a rock:
- When it lands on a deposit, you must print the coordinates of that deposit in the format shown below and increase its value by 1.
- If the rover lands on a rock, it gets broken. Print the coordinates where it got broken in the format shown below, and the program ends.
- If the rover goes out of the field, it should continue from the opposite side in the same direction.
Example: If the rover is at position (3, 0) and it needs to move left (outside the matrix), it should be placed at position (3, 5).

The rover needs to find at least one of each deposit to consider the area suitable to start our colony. 
Stop the program if you run out of commands or the rover gets broken.

### Input
- On the first 6 lines, you will receive the matrix.
- On the following line, you will receive the commands for the rover separated by a comma and a space.
### Output
- For each deposit found while you go through the commands, print out on the console: "{Water, Metal or Concrete} deposit found at ({row}, {col})"
- If the rover hits a rock, print the coordinates where it got broken in the format: "Rover got broken at ({row}, {col})"
- After you go through all the commands or the rover gets broken, print out on the console:

    - If the rover has found at least one of each deposit, print on the console: "Area suitable to start the colony."
    - Otherwise, print on the console: "Area not suitable to start the colony."

# Words Sorting
Write a function words_sorting which receives a different number of words.

Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.

Then, sort the dictionary:
- By values in descending order, if the sum of all values of the dictionary is odd
- By keys in ascending order, if the sum of all values of the dictionary is even

Note: Submit only the function in the judge system

### Input
- There will be no input, just any number of words passed to your function
### Output
- The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
### Constraints:
- There will be no case with capital letters.
- There will be no case with a string consisting of other than letters.

# Flower Finder
You will be given two sequences of characters, representing vowels and consonants. Your task is to start checking if the following words could be found:
- "rose"
- "tulip"
- "lotus"
- "daffodil"

Start by taking the first character of the vowels collection and the last character from the consonants collection. Then check if these letters are present in one or more of the given words. If a letter is present, that part of the word is considered found. The word is gradually revealed with each letter found. Continue processing the next couple of letters until you find one of the given words above.

A letter (vowels or consonants) could participate in more than one word or more than one time in a word, for example:
- The letter "o" is present in "rose", "lotus", and "daffodil". 
- The letter "l" is present in "tulip", "lotus", and "daffodil".
- The letter "f" is present in the word "daffodil" twice.
- The consonant and the vowel are always removed from the collection after trying to match them with the letters in the given words (whether successful or not). In the end, the program stops when a word is found, or there are no more vowels or consonants.

As a result, if you found a word, print it and the remaining letters in each collection in the format described below. Otherwise, print "Cannot find any word!" on the first line and the remaining letters in each sequence in the format described below.

### Input
- On the first line, you will receive vowels, separated by a single space (" ").
- On the second line, you will receive consonants, separated by a single space (" ").

### Output
- On the first line:
    - If a word is found, print it in the format: "Word found: {word_found}"
    - Otherwise, print: "Cannot find any word!"
- On the next lines, print the remaining letters in each collection (if there are any left):
    - "Vowels left: {vowel_one} {vowel_two} … {vowel_N}"
    - "Consonants left: {consonants_one} {consonants_two} … {consonants_N}"

### Constraints
- All letters will be lowercase.
- The letter 'y' will always be a vowel.
- The letter 'w' will always be a consonant.

# Pawn Wars

![image](https://user-images.githubusercontent.com/104040753/196009575-fe760361-a228-4cbf-aa24-52a6bb4da868.png)


A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.). In this problem colors of the board will be ignored.

We will play the game with two pawns, white (w) and black (b), where they can:
- Only move forward in a straight line:
    - White (w) moves from the 1st rank to the 8th rank direction.
    - Black (b) moves from 8th rank to the 1st rank direction.
- Can move only 1 square at a time.
- Can capture another pawn in from of them only diagonally:

![image](https://user-images.githubusercontent.com/104040753/196009595-00ea4b81-18e1-4420-8e8f-669b7968c275.png)


When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.

Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w), then black moves (b), then white (w) again, and so on. 


### Some rules apply when moving paws:
- If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
- If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

### Input
- On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
    - Empty positions are marked with "-".
    - White pawn is marked with "w"
    - Black pawn is marked with "b"

### Output
Print either one of the following:
- If a pawn captures the other, print:
    - "Game over! {White/Black} win, capture on {square}."
- If a pawn reaches the last rank, print:
    - "Game over! {White/Black} pawn is promoted to a queen at {square}."

### Constraints
- The input will always be valid.
- The matrix will always be 8x8.
- There will be no case where two pawns are placed on the same square.
- There will be no case where two pawns are placed on the same column.
- There will be no case where black/white will be placed on the last rank.

# Springtime
Spring is the season of new beginnings. Fresh buds bloom, animals awaken and the earth seems to come to life again. Farmers and gardeners plant their seeds and temperatures slowly rise.
Write a function called start_spring which will receive a different number of keyword arguments.
Each keyword holds a key with a name of the spring object (string), and each value holds its type (string).

For example, dahlia="flower", shrikes="bird", dogwood="tree".

The function should sort the given spring objects in collections by their type:
- The collections sorted by their number of elements in descending order. If two or more collections have the same number of elements in them, return them in ascending order (alphabetically) by the type's name. 
- Each collection's elements should be sorted in ascending order (alphabetically) by the object's name.

Note: Submit only the function in the judge system

### Input
- There will be no input. Just parameters passed to your function.
### Output
- Return the result, sorted as described above in the format:

"{type_one}:

-{spring_object_of_this_type_one}

-{spring_object_of_this_type_two}

…

-{spring_object_of_this_type_N}

{type_two}:

…

{type_N}:

…

-{last_spring_object_of_typeN}"


# Christmas Elves

Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost all toys. Now Santa's elves fear they won't be able to meet their December deadline. It could be a disaster, and some children around the world may not get their Christmas toys. Luckily, you've come up with an idea, and you just need to write a program that manages your plan.

The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.

First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given another sequence of integers, each representing a number of materials in a box.

Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.

You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last box of materials and tries to create the toy:
- Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy decreases by the used energy, and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which increases his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
- Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward and goes to the end of the line, similar to the first bullet.
- Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is already spent, and it needs to be added to the total elves' energy.
    - If an elf creates 2 toys, but he is clumsy, he breaks them.
- If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy, the elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.

Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does NOT TAKE a box, but he takes a day off. Remove the elf from the collection.

Stop crafting toys when you are out of materials or elves.

### Input
- The first line of input will represent each elf's energy - integers, separated by a single space
- On the second line, you will be given the number of materials in each box - integers, separated by a single space

### Output
- On the first line, print the number of created toys:
"Toys: {total_number_of_toys}"

- On the second line, print the total used energy:
"Energy: {total_used_energy}"

- On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:

"Elves left: {elf1}, {elf2}, … {elfN}"

"Boxes left: {box1}, {box2}, … {boxN}"

### Constraints
- All the elves' values will be integers in the range [1, 100]
- All the boxes' values will be integers in the range [1, 100]

# North Pole Challenge

You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items scattered around the workshop.

You will be given the size of the matrix in the format "{rows}, {columns}".

It is the Santa's workshop represented as some symbols separated by a single space:
- Your position is marked with the symbol "Y"
- Christmas decorations are marked with the symbol "D"
- Gifts are marked with the symbol "G"
- Cookies are marked with the symbol "C"
- All of the empty positions will be marked with "."

After the field state, you will be given commands until you receive the command "End".
The commands will be in the format "right/left/up/down-{steps}".
You should move in the given direction with the given steps and collect all the items that come across. If you go out of the field, you should continue to traverse the field from the opposite side in the same direction.
You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items.
If you've collected all items at any point, end the program and print: "Merry Christmas!".

### Input
- On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
- On the next lines, you will receive each row with its columns - symbols, separated by a single space.
- On the following lines, you will receive commands in the format described above until you receive the command "End" or until you collect all items.

### Output
- On the first line, if you have collected all items, print:
"Merry Christmas!"
- Otherwise, skip the line
- Next, print the number of collected items in the format:

>    "You've collected:
>    - {number_of_decoration} Christmas decorations
>    - {number_of_gifts} Gifts
>    - {number_of_cookies} Cookies"

Finally, print the field, as shown in the examples.

### Constrains
- All the commands will be valid
- There will always be at least one item
- The dimensions of the matrix will be integers in the range [1, 20]
- The field will always have only one "Y"
- On the field, there will always be only the symbols shown above.

# Naughty or Nice

Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents, so Santa Claus is preparing his list this year to check which child has been good or bad.

Write a function called naughty_or_nice_list which will receive
- A list representing Santa Claus' "Naughty or Nice" list full of kids' names
- A different number of arguments (strings) and/or keywords representing commands

The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords. 
Each argument is a command. The commands could be the following:

"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.

"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
    
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"): 
If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids depending on the value in the keyword. Then, remove it from the Santa list.

Otherwise, ignore the command.

All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.

Note: Submit only the function in the judge system

### Input
There will be no input. Just parameters passed to your function.

### Output
The function should return strings with the names on each list on separate lines, if there are any, otherwise skip the line:
    "Nice: {name1}, {name2} … {nameN}"
    "Naughty: {name1}, {name2} … {nameN}"
    "Not found: {name1}, {name2} … {nameN}"


# Aladdin's Gifts

Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie for help to prepare the wedding presents.
First, you will receive a sequence of integers representing the materials for every wedding present. After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.


| Gift | Magic needed |
| ---- | ------------ |
| Gemstone | 100 to 199 |
| Porcelain Sculpture | 200 to 299 |
| Gold | 300 to 399 |
| Diamond Jewellery | 400 to 499 |


To make a present, you should take the last integer of materials and sum it with the first magic level value. If the result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
- If the product of the operation is under 100:
    - And if it is an even number, double the materials, and triple the magic, then sum it again. 
    - And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between or equal to any of the numbers in the table above.
- If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. Then, check again if it is between or equal to any of the numbers in the table above.
- If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.

Stop crafting gifts when you are out of materials or magic level.

You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.

### Input
- The first line of input will represent the values of materials - integers, separated by a single space
- On the second line, you will be given the magic levels - integers, separated by a single space

### Output
- On the first line - print whether you have succeeded in crafting the presents:

"The wedding presents are made!"

"Aladdin does not have enough wedding presents."

- On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:

"Materials left: {material1}, {material2}, …"

"Magic left: {magicValue1}, {magicValue2}, …

- On the next lines, print the gifts alphabetically that the Genie has crafted at least once:

"{present1}: {amount}

{present2}: {amount}

…

{presentN}: {amount}"

### Constraints
All the materials values will be integers in the range [1, 1000]
Magic level values will be integers in the range [1, 1000]


# Ball in the Bucket

You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points (integers) and buckets marked with the letter "B". 

Rules of the game:
- You can throw a ball only 3 times.
- When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
- You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
- If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 

After the board state, you are going to receive the information for every throw on a separate line. The coordinates’ information of a hit will be in the format: "({row}, {column})".

Depending on how many points you have collected, you win one of the following:


| Football | 100 to 199 points |
| -------- | ----------------- |
| Teddy Bear | 200 to 299 points |
| Lego Construction Set | 300 and more points |


Your job is to keep track of the scored points and to check if you won a prize. 
For more clarifications, see the examples below.

### Input
- 6 lines – matrix representing the board (each position separated by a single space)
- On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

### Output
-On the first line:
-If you won a prize, print: 

"Good job! You scored {points} points, and you've won {prize}."

- If you did not win any prize, print the points you need to get at least the first prize: 

"Sorry! You need {points} points more to win a prize."

### Constraints
- All of the given points will be integers in the range [1, 30]
- All the given indexes will be integers in the range [0, 30]
- There always will be exactly 6 buckets - 1 on each column


# Shopping List

Write a function called shopping_list which will receive an integer number representing the budget in leva and a different number of keywords. Each key represents the product (string), and each value will be a tuple with the product's price (integer or float number) at the first position and quantity (integer) at the second position.

Your job is to return which products you bought with the given budget. You only buy a product if you can buy all of its quantity.
You could only start shopping if you have at least 100 leva budget. Otherwise, you should stop the program and return "You do not have enough budget.".

Also, you are carrying a basket that cannot hold more than 5 types of products. You should stop buying products:
- if you reach the allowed amount of types of products (no matter their quantity)
- if you did not reach the allowed amount, but you do not have more products on the shopping list

You should always buy products successively!

For each product (all its quantity) you succeeded to buy, return a string on a new line in the following format:
- "You bought {product_name} for {total_price} leva."

Note: Submit only the function in the judge system

### Input
- There will be no input, and just parameters passed to your function

### Output
- The function should return strings on separate lines containing the bought products and their price in the format described above.
- The total price should be formatted to the second decimal point.


# Pizza Orders

On the first line, you will receive a sequence of pizza orders. Each order contains a different number of pizzas, separated by comma and space ", ". On the second line, you will receive a sequence of employees with pizza-making capacities (how much pizzas an employee could make), separated by comma and space ", ".
Your task is to check if all pizza orders are completed. 

To do that, you should take the first order and the last employee and see:
- If the number of pizzas in the order is less than or equal to the employee's pizza making capacity, the order is completed. Remove both the order and the employee.
- If the number of pizzas in the order is greater than the employee's pizza making capacity, the remaining pizzas from the order are going to be made by the next employees until the order is completed. 
- If there are no more employees to finish the order, consider it not completed.

The restaurant does not take orders for more than 10 pizzas at once.
- If an order is invalid (less than or equal to 0), you need to remove it before it is taken by an employee. 

You should keep track of the total pizzas that are being made.

### Input
- On the first line you will be given a sequence of pizza orders each represented as a number – integers separated by comma and space ", "
- On the second line you will be given a sequence of employees with pizza-making capacities – integers separated by comma and space ", "

### Output
- If all orders are successfully completed, print:

All orders are successfully completed!

Total pizzas made: {total count}

Employees: {left employees joined by ", "}

- Otherwise, if you ran out of employees and there are still some orders left print:

Not all orders are completed.

Orders left: {left orders joined by ", "}

### Constraints
-You will always have at least one order and at least one employee
-All integers will be in range [-100, 100]


# Darts

Two players bare-handedly throw small sharp-pointed missiles known as darts at a round target known as a dartboard. Who is going to win this game?
You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:

![Screenshot 2022-10-17 125402](https://user-images.githubusercontent.com/104040753/196150492-d44526f0-a9db-4154-a0b8-f22ec68c930c.png)

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player. The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will be in the format: "({row}, {column})".
- If a player hits outside the dartboard, he does not score any points.
- If a player hits a number, it is deducted from his total.
- If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted from his total.
- If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted from his total.
- "B" is the bullseye. If a player hits it, he wins the game, and the program ends.

For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they are deducted from his total.

Your job is to find who won the game and with how many turns.

### Input
- The name of the first player and the name of the second player, separated by ", "
- 7 lines – the dartboard (separated by single space)
- On the next lines - the coordinates in the format: "({row}, {column})"

### Output
- You should print only one line containing the winner and his count of throws: 

"{name} won the game with {count_turns} throws!"

### Constrains
- There will always be exactly 7 lines
- There will always be a winner
- The points will be in range [1, 24]
- The coordinates will be in range [0, 100]


# Flights 

Create a function named flights that receives a different number of arguments representing the information about the flights for a day: 

- the destination of each flight 

- the count of passengers that are boarding the plane 

- a string "Finish" 

You need to take each argument and make a dictionary with the plane’s destination as a key and the passengers as a value of the corresponding key.  

- If there are more than one flight to the same destination, you should count all the passengers that flew to the destination.  

- You should modify the dictionary until the current argument is equal to "Finish". 

Note: Submit only the function in the judge system 

### Input 

There will be no input, just parameters passed to your function 

### Output 

The function should return the final dictionary 

### Constrains 

All numbers will be valid integers in the range [0, 300] 

There will be no flight without given number of passengers 


# Fireworks Show

Maria wants to make a firework show for the wedding of her best friend. 
We should help her to make the perfect firework show.

First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another sequence of integers representing explosive power.

You need to start from the first firework effect and try to mix it with the last explosive power. If the sum of their values is:
- divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
- divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
- divisible by both 3 and 5 – create Crossette firework and remove both materials

Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix the same explosive power with the next firework effect. 

If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other. 

When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive power, you need to stop mixing. 

To make the perfect firework show, Maria needs 3 of each of the firework types.

### Input
- On the first line, you will receive the integers representing the firework effects, separated by ", ".
- On the second line, you will receive the integers representing the explosive power, separated by ", ".

### Output
- On the first line, print:
    - if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
    - if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
- On the second line, print all firework effects left if there are any: 
    - "Firework Effects left: {effect1}, {effect2}, (…)"
- On the third line, print all explosive fillings left if there are any: 
    - " Explosive Power left: {filling1}, {filling2}, (…)"

- Then, you need to print all fireworks and the amount you have of them:
    - "Palm Fireworks: {count}"
    - "Willow Fireworks: {count}"
    - "Crossette Fireworks: {count}"

### Constraints
- All the given numbers will be integers in the range [-100, 100].
- There will be no cases with empty sequences.


# Collecting Coins

You are playing a game, and your goal is to collect 100 coins.

On the first line, you will be given a number representing the size of the field with a square shape. On the following few lines, you will be given the field with: 
- One player - randomly placed in it and marked with the symbol "P"
- Numbers for coins placed at different positions of the field
- Walls marked with "X"

After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left", "right". If the command is invalid, you should ignore it. 

The player moves in the given direction with one step for each command and collects all the coins that come across. If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.

Note: He can go through the same path many times, but he can collect the coins just once (the first time).

There are only two possible outcomes of the game:
- The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
- The player collects at least 100 coins and wins the game.

For more clarifications, see the examples below.

### Input
- A number representing the size of the field (matrix NxN)
- A matrix representing the field (each position separated by a single space)
- On each of the following lines, you will get a move command.

### Output
- If the player won the game, print: "You won! You've collected {total_coins} coins."
- If the player loses the game, print: "Game over! You've collected {total_coins} coins."
    - Collected coins have to be rounded down to the next-lowest number.
- The player's path as cooridnates in lists on separate lines: 

    "Your path:

    [{row_position1}, {column_position1}]

    [{row_position2}, {column_position2}]

    …

    [{row_positionN}, {column_positionN}]"

### Constrains
There will be no case in which less than 100 coins will be in the field
All given numbers will be valid integers in the range [0, 100]


# Cupcake Shop

Maria is opening a cupcake shop. Help her manage her inventory to improve stock availability.

Write a function called stock_availability which receives:
- an inventory list of boxes with different kinds of cupcake flavours
- "delivery" or "sell" as second parameter
- there might or might not be any other parameters – numbers or strings at the end

- In case of "delivery"  to the shop was delivered new boxes with diferent kinds of cupcakes:
    - You should add the boxes at the end of the inventory list
    - There will be always at least one box delivered
- In case of "sell" Maria has a client and she is selling different boxes with cupcakes:
    - If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes and you should remove them from the beginning of the inventory list
    - If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes of the ordered flavour/s. Beware that not everything the buyer has ordered might be in stock, so you should check if the order is valid.  
    - If there are no other parameters, it means that Maria has sold only the first box of cupcakes and you should remove  it of the inventory list

### Input
- There will be no input
- Parameters will be passed to your function

### Output
- The function should return a new inventory list
- All commands will be valid


# Matching
 
First you will be given a sequence of integers representing males. Afterwards you will be given another sequence of integers representing females.

You have to start from the first female and try to match it with the last male.
- If their values are equal, you have to match them and remove both of them. Otherwise you should remove only the female and decrease the value of the male by 2.
- If someone’s value is equal to or below 0, you should remove him/her from the records before trying to match him/her with anybody.
- Special case - if someone’s value divisible by 25 without remainder, you should remove him/her and the next person of the same gender before trying to match them with anybody.

You need to stop matching people when you have no more females or males.

### Input
On the first line of input you will receive the integers, representing the males, separated by a single space. 
On the second line of input you will receive the integers, representing the females, separated by a single space.

### Output
- On the first line of output - print the number of successful matches:
"Matches: {matchesCount}"
- On the second line - print all males left:
    - If there are no males: "Males left: none"
    - If there are males: "Males left: {maleN}, … , {male3}, {male2}, {male1}"
- On the third line - print all females left:
    - If there are no females: "Females left: none"
    - If there are females: "Females left: {female1}, {female2}, {female3},…, {femaleN}"

### Constraints
- All of the given numbers will be valid integers in the range [-100, 100].


# Game of Words

You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
On the next N lines, you will receive the rows of the field.
The player will be placed on a random position, marked with "P". On random positions there will be letters.
All of the empty positions will be marked with "-".

Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
At the end print all letters and the field.

### Input
- On the first line, you are given the initial string
- On the second line, you are given the integer N - the size of the square matrix
- The next N lines holds the values for every row
- On the next line you receive a number M
- On the next M lines you will get a move command

### Output
- On the first line the final state of the string
- In the end print the matrix

### Constraints
- The size of the square matrix will be between [2…10]
- The player position will be marked with "P"
- The letters on the field will be any letter except for "P"
- Move commands will be: "up", "down", "left", "right"

# Scheduling

You are hired to create a program that implements SJF (Shortest Job First). It works by letting the shortest jobs to take the CPU, so jobs won't get frozen.

On the first line you will be given the jobs as integers (clock-cycles needed to finish the job) separated by comma and space ", ". On the second line you will be given the index of the job that we are interested in and want to know how many cycles will pass until the job is done.

The tasks that need the least amount of clock-cycles will be completed first. 
For the jobs that need the same amount of clock-cycles, the order is FIFO (First In First Out).
You have to print how many clock-cycles will pass until the task you are interested in is completed. For more clarifications, see the examples below.

### Input
- On the first line you will receive numbers separated by ", "
- On the second line you will receive the index of the task you are interested in

### Output
- Single line: the clock-cycles that will pass until the task you are interested in is finished


# Checkmate

You will be given a chess board (8x8). On the board there will be 3 types of symbols:
- "." – empty square
- "Q" – a queen
- "K" – the king

Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing the king.

### Input
- 8 lines – the state of the board (each square separated by single space)

### Output
- The positions of the queens that can capture the king as lists
- If the king cannot be captured, print: "The king is safe!"
- The order of output does not matter

### Constrains
- There will always be exactly 8 lines
- There will always be exactly one King
- Only the 3 symbols described above will be present in the input

# List Pureness

Write function called best_list_pureness which will receive a list of numbers and a number K.
You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness (pureness is calculated by summing all the elements in the list multiplied by their indices).
For example, in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26. 
At the end the function should return a string containing the highest pureness and the amount of rotations that were made to find this pureness in the following format: "Best pureness {pureness_value} after {count_rotations} rotations".
If there is more than one highest pureness, take the first one.

Note: Submit only the function in the judge system

### Input
- There will be no input, just parameters passed to your function

### Output
- There is no expected output
- The function should return a string in the following format: "Best pureness {pureness_value} after {count_rotations} rotations"


# Taxi Express

You have created your own taxi company called "Taxi Express". You want to analyze how well your taxi drivers are doing by calculating how much time they need to tend the customers.

You will receive a list of the cutomers (numbers seperated by comma and space ", ") on the first line and list of your taxis (numbers seperated by comma and space ", ").
Each number from the customer list represents how much time it takes to drive the customer to his/her destination.
Each number from the taxis list represents how much time they can drive, before they need to refill their tanks.
Keep track of the total time passed to drive all the customers to their destinations (values of all customers).
Each time you tend customers you should put the first customer in the last taxi until there are no customers left.
- If the taxi can drive the customer to his/her destination, he does and you must add the time passed to drive the customer to his/her destination (the value of the current customer) to the total time. Remove both the customer and the taxi.
- If the taxi cannot drive the customer to his/her destination, leave the customer at the beginning of the queue and remove the taxi. 

At the end if you have successfully driven all the customers to their destinations, print:

"All customers were driven to their destinations"

"Total time: {total_time} minutes"

Otherwise, if you ran out of taxis and there are still some customers left print:

"Not all customers were driven to their destinations"

"Customers left: {left_customers joined by ", "}"

### Input
- On the first line you are given the customers – numbers seperated by comma and space ", "
- On the second line you are given the taxis – numbers seperated by comma and space ", "

### Output
- Print the output as described above

### Constraints
- You will always have at least one customer and at least one taxi


# Minesweeper Generator

Everybody remembers the old mines game. Now it is time to create your own.

You will be given an integer n for the size of the mines field with square shape and another one for the number of bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb.
Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and calculate the numbers in each cell of the field. Each cell represents a number of all bombs directly near it (up, down, left, right and the 4 diagonals).

![image](https://user-images.githubusercontent.com/104040753/196983779-2381db62-6791-4737-b3c5-344deab94ae9.png)

### Input
- On the first line, you are given the integer n – the size of the square matrix.
- On the second line – the number of the bombs.
- The next n lines holds the position of each bomb.

### Output
- Print the matrix you've created.

### Constraints
- The size of the square matrix will be between [2…15].


# Numbers Search

Write a function called numbers_searching which receives a different amount of parameters. All parameters will be integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of duplicates from the given sequence and a missing value, such that all the duplicate values and the missing value are between the smallest and the biggest received number.

The function should return a list with the last missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.

For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]

### Input
- There will be no input
- Parameters will be passed to your function

### Output
The function should return a list in the following format: [missing number, [duplicate_numbers separated with comma and space]]

### Constraints
The missing number will always be between the smallest and the biggest received number


# Bombs

Ezio is still learning how to make bombs. With their help, he will save civilization. We should help Ezio to make his perfect bombs.

You will be given two sequences of integers, representing bomb effects and bomb casings.
You need to start from the first bomb effect and try to mix it with the last bomb casing.
If the sum of their values is equal to any of the materials in the table below – create the bomb corresponding to the value and remove both bomb materials.
Otherwise, just decrease the value of the bomb casing by 5. You need to stop combining when you have no more bomb effects or bomb casings, or you successfully filled the bombs pouch.

Bombs:
- Datura Bombs: 40
- Cherry Bombs: 60
- Smoke Decoy Bombs: 120

To fill the bomb pouch, Ezio needs three of each of the bomb types.

### Input
- On the first line, you will receive the integers representing the bomb effects, separated by ", ".
- On the second line, you will receive the integers representing the bomb casings, separated by ", ".

### Output
- On the first line, print:

if Ezio succeeded to fulfill the bomb pouch: "Bene! You have successfully filled the bomb pouch!"

if Ezio didn't succeed to fulfill the bomb pouch: "You don't have enough materials to fill the bomb pouch."

- On the second line, print all bomb effects left:

If there are no bomb effects: "Bomb Effects: empty"

If there are effects: "Bomb Effects: {bombEffect1}, {bombEffect2}, (…)"

- On the third line, print all bomb casings left:

If there are no bomb casings: "Bomb Casings: empty"

If there are casings: "Bomb Casings: {bombCasing1}, {bombCasing2}, (…)"

- Then, you need to print all bombs and the count you have of them, ordered alphabetically:

"Cherry Bombs: {count}"

"Datura Bombs: {count}"

"Smoke Decoy Bombs: {count}"

### Constraints
- All of the given numbers will be valid integers in the range [0, 120].
- There will be no cases with negative material.


# Snake

Everybody remembers the old snake game. Now it is time to create your own.

You will be given an integer n for the size of the snake territory with square shape. On the next n lines, you will receive the rows of the territory.
The snake will be placed on a random position, marked with the letter 'S'.
On random positions there will be food, marked with '*'.
There might also be a lair on the territory. The lair has two burrows. They are marked with the letter - 'B'.
All of the empty positions will be marked with '-'.

Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
Move commands will be: "up", "down", "left", "right".

If the snake moves to a food, it eats the food and increases the food quantity with one.
If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
If the snake goes out of its territory, it loses, can't return back and the program ends.
The snake needs at least 10 food quantity to win.
When the snake has gone outside of its territory or has eaten enough food, the game ends.

### Input
- On the first line, you are given the integer n – the size of the square matrix.
- The next n lines holds the values for every row.
- On each of the next lines you will get a move command.

### Output
- On the first line:
    - If the snake goes out of its territory, print: "Game over!"
    - If the snake eat enough food, print: "You won! You fed the snake."
- On the second line print all food eaten: "Food eaten: {food quantity}"
- In the end print the matrix.

### Constraints
- The size of the square matrix will be between [2…10].
- There will always be 0 or 2 burrows, marked with - 'B'.
- The snake position will be marked with 'S'.
- The snake will always either go outside its territory or eat enough food.
- There will be no case in which the snake will go through itself.

# List Manipulator

Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters. The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
- In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
- In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
- In case of "remove" and "beginning"
    - If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
    - If there are no other parameters, remove only the first element of the list.
    - Finaly, return the new list
- In case of "remove" and "end"
    - If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
    - Otherwise if there are no other parameters, remove only the last element of the list.
    - Finaly, return the new list

### Input
- There will be no input
- Parameters will be passed to your function
### Output
- The function should return the new list of numbers