def reverse_digits(num):
    reversed_num = 0
    while num>0:
        last_num = num%10
        num = num//10
        reversed_num = 10 * reversed_num + last_num 
    print(reversed_num)

reverse_digits(1234)