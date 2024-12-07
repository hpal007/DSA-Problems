


def nested_loop(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

    * 
    * *
    * * *
    * * * *
    * * * * *

    """

    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

nested_loop(5)