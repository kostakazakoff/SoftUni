# Lab: File Handling Problems for in-class for the Python Advanced Course @SoftUni.

## 1. File Opener

You are given a file called text.txt with the following text:

> This is some random line
> 
> This is the second line
> 
> And this is the third one

Create a program that opens the file. If the file is found, print 'File found'. If the file is not found, print 'File not found'.

## 2. File Reader

You are given a file called numbers.txt with the following content:

> 1
> 
> 2
> 
> 3
> 
> 4
> 
> 5

Create a program that reads the numbers from the file. Print on the console the sum of those numbers.

## 3. File Writer

Create a program that creates a file called my_first_file.txt. In that file, write a single line with the content: 'I just created my first file!'

## 4. File Delete

Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times, print the message: 'File already deleted!'.

## 5. Word Count

Write a program that reads a list of words from the file words.txt and finds how many times each of the words is contained in another file text.txt. Matching should be case-insensitive.

The results should be written to other text files. Sort the words by frequency in descending order.

# Exercise: File Handling
Problems for exercise and homework for the Python Advanced Course @SoftUni.
## 1. Even Lines
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.


## 2. Line Numbers
Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and punctuation marks. The result should be written to another text file. 

## 3. File Manipulator
Create a program that will receive commands until the command "End". The commands can be:
- "Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)
- "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it, and add the content
- "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
- "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

## 4. Directory Traversal
Write a program that traverses a given directory for all files.
Search through the first level of the directory only and write information about each found file in report.txt.
The files should be grouped by their extension.
Extensions should be ordered by name alphabetically.
The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.

