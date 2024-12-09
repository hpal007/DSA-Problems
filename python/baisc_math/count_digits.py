def count_digits(num):
    cnt = 0
    while num>0:
        num = num//10
        cnt +=1

    print(cnt)



count_digits(123)