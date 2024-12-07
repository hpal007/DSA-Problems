
def rectangular_star(n,m):
    """
    Problem Statement: Given an integer N, print the following pattern.

    * * * * *
    * * * * *
    * * * * *
    * * * * *

    """

    for i in range(n):
        for j in range(m):
            print("* ", end=" ")
        print("\n")

rectangular_star(4,5)