O(1) >> O(logN) >> O(N) >> O(NlogN) >> O(N^2) >> O(N^logN) >> O(2^N) >> O(N!)

# Time Complexity Overview

This document provides an overview of common time complexities in algorithms, including their definitions and examples.

| **Complexity** | **Notation** | **Definition**                                               | **Example**                               |
|----------------|--------------|-------------------------------------------------------------|-------------------------------------------|
| Constant       | O(1)        | Execution time is constant, independent of input size.     | Accessing an element in an array by index. |
| Logarithmic    | O(log N)    | Execution time increases logarithmically as input size grows. | Binary search in a sorted array.         |
| Linear         | O(N)        | Execution time increases linearly with input size.         | Iterating through all elements in an array. |
| Linearithmic   | O(N log N)  | Execution time increases in proportion to N times log N.   | Merge sort and quicksort algorithms.     |
| Quadratic      | O(N^2)      | Execution time increases quadratically with input size.    | Bubble sort or nested loops.             |
| Polynomial     | O(N^log N)  | Execution time grows polynomially with respect to N.       | Specific algorithms (less common).       |
| Exponential    | O(2^N)      | Execution time doubles with each additional element.        | Recursive Fibonacci calculation (naive). |
| Factorial      | O(N!)       | Execution time grows factorially with respect to N.        | Generating all permutations of a set.    |


# Space Complexity Overview

| **Complexity Type**    | **Notation** | **Description**                                               | **Example**                                   |
|-------------------------|--------------|---------------------------------------------------------------|-----------------------------------------------|
| Constant                | O(1)        | Fixed amount of space regardless of input size.              | Storing a few variables.                      |
| Logarithmic             | O(log N)    | Space grows logarithmically with input size.                 | Algorithms that halve the problem size.      |
| Linear                  | O(N)        | Space grows linearly with input size.                        | Storing elements in an array of size N.      |
| Linearithmic            | O(N log N)  | Space increases proportionally to N times log N.            | Some efficient sorting algorithms.            |
| Quadratic               | O(N^2)      | Space grows proportionally to the square of input size.      | Creating a two-dimensional array.             |
