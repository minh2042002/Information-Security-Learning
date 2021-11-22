LETTER = 'abcdefghijklmnopqrstuvwxyz'
# key(a,b)
N = 26 # Module

def gcd(number_1, number_2):
	if number_1 < number_2:
		tmp = number_1
		number_1 = number_2
		number_2 = tmp

	if number_1 % number_2 == 0:
		return number_2
	else:
		return gcd(number_2, number_1%number_2)

def inverseModule(number, module, x=0):
	if (module*x+1) % number == 0:
		return int((module*x+1)/number)
	else:
		return int(inverseModule(number, module, x+1))

def affineEncrypt(plaintext, a, b):
	text = ''
	
	for t in plaintext:
		text += LETTER[(a * LETTER.index(t) + b) % N]
	
	return text

def affineDecrypt(ciphertext, a, b):
	text = ''
	inverse_a = inverseModule(a, N);

	for t in ciphertext:
		text += LETTER[(inverse_a * (LETTER.index(t) - b) ) % N]
	
	return text

def main():

	while True:
		print("Key(a,b)=>")
		a = int(input("a: "))
		b = int(input("b: "))
	
		if gcd(a, N) == 1:
			text = input("Text: ")
			selection = int(input("Enter 0 to Encrypt - 1 to Decrypt:"))
			if selection == 0:
				print(affineEncrypt(text, a, b))
				break
			else:
				print(affineDecrypt(text, a, b))
				break
		else:
			print("Key invalid!")

main()