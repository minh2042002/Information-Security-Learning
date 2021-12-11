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

print(mod_inv(15, 2^1064-1))