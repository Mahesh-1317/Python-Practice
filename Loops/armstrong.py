n = int(input("Enter a number: "))
m = n
sum = 0
while m != 0:
    ld = m % 10 
    sum += ld * ld * ld
    m //= 10
if sum == n:
    print(f"{sum} is an armstromg number")
else:
    print(f"{n} is not armstrong number")