import sys
from math import gcd

# Algorithm extension euclid
def extended_euclid(a, b): # d = gcd(a,b) = a*x + b*y
	if b == 0:
		return a,1,0
	else:
		d_, x_, y_ = extended_euclid(b, a%b)
		d, x, y = (d_, y_, x_ - int(a/b)*y_)
		return d, x, y

# Calculate inverse of number in module
# d = gcd(a,n) = a*x + n*y = a*x mod n
# if d = 1:
#   a^-1 = x mod n 
def mod_inv(a, n):  
	d, x, y = extended_euclid(a, n)
	b = x%n 
	return b

# Calculate exponentiation fast
def modular_exponent(a, b, n):
    if b == 0: return 1
    if b == 1: return a
    r = modular_exponent(a, b//2, n)
    r = (r*r)%n
    if b%2 == 1: 
        r = (r*a)%n
    return r%n


# Discrete logarithm
def DLog(g, a, n): # g^x = a mod n, DLog(g, a) mod n = x
    for x in range(n):
        if modular_exponent(g, x, n) == a:
            return x
    return -1

# fermat's little theorem: 
#   a^(p-1) = 1 mod p
#   a^-1 = a^(p-2)

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

# Find primitive root
def find_primitive_root(N):
    Z = []
    for i in range(1, N):
        if euclid(1, N) == 1:
            Z.append(i)
    S = []
    for i in Z:
        for j in Z:
            if modular_exponent(i, j, N) == 1:
                if j == len(Z):
                    S.append(i)
                break
    
    return S, len(S)

if __name__ == "__main__":
    pass