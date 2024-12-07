def increasing_number_triangle_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern :
        1
        2 3
        4 5 6
    """
    v = 1
    for i in range(1, n + 1):
        for j in range(0, i):
            print(v, end=" ")
            v += 1
        print()


increasing_number_triangle_pattern(3)
