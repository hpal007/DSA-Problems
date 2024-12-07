def reverse_letter_triangle_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern :

    A B C
    A B
    A

    """
    v = 65
    for i in range(n):
        for j in range(n-i):
            print(chr(v+j), end=" ")
        print()


reverse_letter_triangle_pattern(5)
