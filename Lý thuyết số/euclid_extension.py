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

G = {1,2,3,4,5,6,7,8,9,10}

def check_set(ans, G):
    for val in G:
        if val not in ans:
            return 0
    return 1

def find_birth_element(G, module): 
    for g in range(module):
        ans = set()
        for x in range(module):
            ans.add((g**x)%11)
        if check_set(ans, G):
            print(f"{g}: ", end=" ")
            for i in ans:
                print(f"{i} ", end=" ")
            print("\n")

# Discrete logarithm
def DLog(g, a, n): # g^x = a mod n, DLog(g, a) mod n = x
    for x in range(n):
        if modular_exponent(g, x, n) == a:
            return x
    return -1

# fermat's little theorem: 
#   a^(p-1) = 1 mod p
#   a^-1 = a^(p-2)
print(modular_exponent(5, 18446744073709551629-2, 18446744073709551629))