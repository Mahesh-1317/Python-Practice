for i in range(1000):
    m = i
    sum = 0
    while m != 0:
        ld = m % 10
        sum += ld*ld*ld
        m //= 10
    if i == sum:
        print(i)