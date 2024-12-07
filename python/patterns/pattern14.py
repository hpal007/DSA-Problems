def alpha_ramp_pattern(n):
    """
    Problem Statement: Given an integer N, print the following pattern :

    A
    B B
    C C C

    """
    v = 64
    for i in range(1,n+1):
        for j in range(i):
            print(chr(v+i), end=" ")
        print()


alpha_ramp_pattern(4)
