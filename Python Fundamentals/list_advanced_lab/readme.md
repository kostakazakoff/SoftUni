Lists Advanced - LAB


1. No Vowels

Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'


2. Trains

You will receive a number representing the number of wagons a train has. Create a list (train) with the given length containing only zeros. Until you receive the command "End", you will receive some of the following commands:

· "add {people}" – you should add the number of people in the last wagon

· "insert {index} {people}" - you should add the number of people at the given wagon

· "leave {index} {people}" - you should remove the number of people from the wagon. There will be no case in which the people will be more than the count in the wagon.

There will be no case in which the index is invalid!

After you receive the "End" command print the train.


3. To-do List

You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{note}".

Return a list containing all to-do notes sorted by importance in ascending order.

The importance value will always be an integer between 1 and 10 (inclusive)


4. Palindrome Strings

On the first line, you will receive words separated by a single space. On the second line, you will receive a palindrome.
First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".


5. Sorting Names

Write a program that reads a single string with names separated by comma and space ", ".
Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending order (alphabetically).
Print the resulting list.


6. Even Numbers

Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.


7. The Office

You will receive two lines of input:

· a list of employees' happiness as a string of numbers separated by a single space

· a happiness improvement factor (single number).

Your task is to find out if the employees are generally happy in their office.

First, multiply each employee's happiness by the factor.

Then, print one of the following lines:

· If half or more of the employees have happiness greater than or equal to the average:

"Score: {happy_count}/{total_count}. Employees are happy!"

· Otherwise:

"Score: {happy_count}/{total_count}. Employees are not happy!"
