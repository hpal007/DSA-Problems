#TC: O(N) SC: O(N) (as array is used to store)

# def fibonacci_of_n(n):
#     if n <2:
#         return n
#     return fibonacci_of_n(n-1) + fibonacci_of_n(n-2)

# a = []
# n = 6
# for i in range(n+1):

#     val = fibonacci_of_n(i)
#     a.append(val)

# print(a)


#TC O(N) SC O(1) (since we are not using array)
def fibonacci_series(n):
    if n ==0:
        print(0)
    else:
        second_last = 0
        last= 1
        print(f"The Fibonacci Series up to {n}th term:")
        print(second_last)
        print(last)
        curr = 0
        for _ in range(1, n):
            curr = last + second_last
            second_last, last = last, curr
            print(curr)
 
fibonacci_series(5)