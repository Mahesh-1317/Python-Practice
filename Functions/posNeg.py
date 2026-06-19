# n = int(input("Enter a num: "))
# for i in range (-n,1):
#     print(i,end=" ")
# print()
# for i in range (n-1,-1,-1):
#     print(i,end=" ")

def pos(n):
    for i in range(n-1,-1,-1):
        print(i,end=" ")
def neg(n):
    for i in range(n,1):
        print(i,end=" ")
def main():
    n = int(input("Enter a number: "))
    if n > 0:
        return pos(n)
    elif n < 0:
        return neg(n)
    else:
        print("Already Zero")
main()