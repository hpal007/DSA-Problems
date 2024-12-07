def number_crown_pattern(n):
    """
    Number Crown Pattern

    Problem Statement: Given an integer N, print the following pattern : 

    1          1
    12        21
    12       321
    1234    4321
    12345  54321
    123456654321

    """
    space = 2*(n-1)
    for i in range(1,n+1):
        
        #number
        for j in range(1,i+1):
            print(j, end=" ")
        #space
        for _ in range(space):
            print(" ", end=" ")
        #number
        for j in range(i, 0, -1):
            print(j, end=" ")
            
        print()
        space -=2
        


number_crown_pattern(5)