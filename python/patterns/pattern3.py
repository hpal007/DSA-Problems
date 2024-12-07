def seeding(n):
    """
    Problem Statement: Given an integer N, print the following pattern : 

    * * * * *
    * * * *
    * * *
    * *
    *

    """

    for i in range(n):
        for _ in range(1, n-i+1):
            print("*", end=" ")
        print()

seeding(5)