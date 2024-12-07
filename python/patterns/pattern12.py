def increasing_letter_triangle_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern :
    A
    A B
    A B C
    """
    v = 65
    for i in range(1,n+1):
        for j in range(i):
            print(chr(v+j), end=" ")
        print()


increasing_letter_triangle_pattern(5)
