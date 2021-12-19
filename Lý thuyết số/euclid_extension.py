import sys
from math import gcd

def extended_euclid(a, b):
	if b == 0:
		return a,1,0
	else:
		d_, x_, y_ = extended_euclid(b, a%b)
		d, x, y = (d_, y_, x_ - int(a/b)*y_)
		return d, x, y

def mod_inv(a, n):
	d, x, y = extended_euclid(a, n)
	b = x%n 
	return b

def modular_exponent(a, b, n):
    if b == 0: return 1
    if b == 1: return a
    r = modular_exponent(a, b//2, n)
    r = (r*r)%n
    if b%2 == 1: 
        r = (r*a)%n
    return r%n

# def check_dict(ans):
#     for i in ans:
#         if 
def check_gcd():
    for b in range(13, 2000):
        ans = {}
        for i in range(b):
            if gcd(i,b) == 1:
                ans[mod_inv(i, b)] = i

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


if __name__ == '__main__': 

    sys.setrecursionlimit(3000)
    print(modular_exponent(5,-1,709551629))