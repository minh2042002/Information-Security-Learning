from random import choice

LETTER = 'abcdefghijklmnopqrstuvwxyz'
#number = int('{0:05b}'.format(5))


def plaintextToBinary(plaintext): # chuyển bản rõ thành binary
	plaintextBinary = list([])

	for i in range(len(plaintext)):
		plaintextBinary[i] = LETTER.index(plaintext[i])

	return plaintextBinary 

def printBinary(textBinaryConvert): # chuyển đổi từ list số sang str binary
	textBinary = list([])

	for i in range(len(textBinaryConvert)):
		textBinary[i] = int('{0:05b}'.format(textBinaryConvert[i]))

	return str(textBinary)

def randomKey(plaintextBinary): # tạo key
	key = list([])
	
	for i in range(len(plaintextBinary)):
		key[i]= choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])

	return key

def Encrypt(plaintextBinary, key): # mã hoá bản rõ từ nhị phân
	ciphertextBinary = list([])

	for i in range(len(plaintextBinary)):
		ciphertextBinary[i] = plaintextBinary[i] ^ key[i]

	return ciphertextBinary

def Decrypt(ciphertextBinary, key): # giải mã tạo ra bản rõ với dạng nhị phân
	plaintextBinary = list([])

	for i in range(len(key)):
		plaintextBinary[i] = ciphertextBinary[i] ^ key[i]

	plaintext = binaryToPlaintext(plaintextBinary)

	return plaintext

def binaryToPlaintext(plaintextBinary): # chuyển bản rõ từ nhị phân sang bản gốc
	plaintext = list([])

	for i in range(len(plaintextBinary)):
		plaintext[i] = LETTER[plaintextBinary[i]]  

	return str(plaintext)

def cutStringToList_5(__string):
	pass
	
# def inputKey(binaryKey):
	


# 	for i in range(len(binaryKey)):
# 		i += 4

def main():
	plaintext = str(input("Plaintext: "))

	# plaintextBinary = plaintextToBinary(plaintext	)

	# key = randomKey(plaintextBinary)

	print(plaintext.split(' '))

main()