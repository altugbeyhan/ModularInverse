# shortest way : print(pow(2,-1,7)) -> output = 4

def inverse(a,n):
    check = 0
    for x in range(n):
        if ((a*x)%n) == 1:
            check = x
    return check

print(inverse(a=2,n=7)) # output = 4
print(inverse(a=3,n=7)) # output = 5
print(inverse(a=-3,n=7)) # output = 2
print(inverse(a=3,n=15)) # output = 0
print(inverse(a=5,n=15)) # output = 0
print(inverse(a=7,n=15)) # output = 13
