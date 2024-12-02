# Take Skip
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given step.

# Dictionary Iterator
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

# Countdown Iterator
Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.

# Sequence Repeat
Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement an iterator to return the given elements, so they form a string with a length - the given number. If the number is greater than the number of elements, then the sequence repeats as necessary.

# Take Halves
You are given a skeleton with the following code:

Implement the three generator functions:
- integers() - generates an infinite amount of integers (starting from 1)
- halves() - generates the halves of those integers (each integer / 2)
- take(n, seq) - takes the first n halves of those integers

# Fibonacci Generator
Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current number with the previous one.

# Reader
Create a generator function called read_next() which should receive a different number of arguments (all iterable). On each iteration, the function should return each element from each sequence.

# Prime Numbers
Create a generator function called get_primes() which should receive a list of integer numbers and return a list containing only the prime numbers from the initial list.

# Possible permutations
Create a generator function called possible_permutations() which should receive a list and return lists with all possible permutations between its elements.