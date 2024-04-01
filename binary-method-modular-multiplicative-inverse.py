def binary(p):
    result = ""
    if p > 1:
        result += binary(p//2)
    result += str(p % 2)
    return result

def inverse(a,p):
    x = binary(p-2)
    rev_x = x[::-1]
    inv = 1
    
    for d in range(len(rev_x)):
        if rev_x[d] == "1":
            inv *= ((a**(2**d)) % p)

    print(inv % p)

inverse(4,17) # output = 13
