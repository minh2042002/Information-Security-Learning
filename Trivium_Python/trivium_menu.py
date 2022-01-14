from collections import deque
from email import message # hàng đợi 2 đầu
from itertools import repeat
from statistics import mode # trình lặp lại nhanh hơn khi sử dụng for
from bitstring import BitArray 
# BitArray là một dãy Bit có thể thay đổi,
# BitArray cũng chuyển đổi 1 string thành 1 dãy bit 
# e.g: a = '0x10101' - 1 string
# b = BitArray(a) - 1 dãy bit 0x10101
import argparse # thư viện tạo chương trình CLI (command line interface)
import nacl.utils

class Trivium:
    def __init__(self, key, iv):
        self.register = None
        self.key = key
        self.iv = iv

        # Khởi tạo thanh ghi
        # (s1; s2; : : : ; s93) (K1; : : : ; K80; 0; : : : ; 0)
        init_register = self.iv
        init_register += list(repeat(0, 13))
	
        #(s94; s95; : : : ; s177) (IV1; : : : ; IV80; 0; : : : ; 0)
        init_register += self.key
        init_register += list(repeat(0, 4))

        #(s178; s279; : : : ; s288) (0; : : : ; 0; 1; 1; 1)
        init_register += list(repeat(0, 108))
        init_register += [1,1,1]

        self.register = deque(init_register) # chuyển thanh ghi thành deque

        # Chạy pha khởi động với 4 chu kỳ
        for i in range(4*288):
            self.gen_keystream()  

    def gen_keystream(self): # Hàm tạo từng Si trong keystream
        register_1 = self.register[65] ^ self.register[92]
        register_2 = self.register[161] ^ self.register[176]
        register_3 = self.register[242] ^ self.register[287]

        Si = register_1 ^ register_2 ^ register_3

        register_1 = register_1 ^ self.register[90] & self.register[91] ^ self.register[170]
        register_2 = register_2 ^ self.register[174] & self.register[175] ^ self.register[263]
        register_3 = register_3 ^ self.register[285] & self.register[286] ^ self.register[68]

        self.register.rotate() # Dịch thanh ghi sang bên phải 1 vị trí

        self.register[0] = register_3
        self.register[93] = register_1
        self.register[177] = register_2

        return Si

    def keystream(self, msglen): # Hàm tạo keystream với độ dài của message

        counter = 0
        keystream = []

        while counter < msglen:
            keystream.append(self.gen_keystream()) # Thêm một Si vào sau dãy keystream
            counter += 1

        return keystream
        
    def encrypt(self, msg): # Hàm mã hóa
        cipher_text = []

        for i in range(len(msg)):
            hex_plain = hex(ord(msg[i]))    # chuyển message thành dạng hex
                                            # ord() chuyển kí tự thành dạng int
            plain = BitArray(hex_plain)
            
            keystream = self.keystream(8) #list
            keystream = '0b' + ''.join(str(i) for i in keystream)
            keystream = BitArray(keystream)
            # Dãy bit cipher
            cipher = [x ^ y for x, y in zip(map(int, list(plain)), map(int, list(keystream)))]
            # map(int, list(plain)): chuyển các phần tử của list plain thành dạng int
            # list(plain) dưới dạng [True, False, True, ...]
            """
            Hàm zip(iterator_1, iterator _2) nén 2 tập dữ liệu vào thành 1 tập dữ liệu 
            theo thứ tự lần lượt 
            e.g: list1 = [1, 2, 3], list2 = ['one', 'two', 'three']
            hàm zip(list1, list2) sẽ trả về: {(1, 'one'), (2, 'two'), (3, 'three')}
            để giải nén sử dụng zip(*iterator)
            """

            """
            Hàm map() tích hợp sẵn trong Python có tác dụng duyệt tất cả các phần tử 
            của một iterable (list, tuple, dictionary...) qua một hàm cho trước 
            và trả về một list kết quả sau khi thực thi.
            Cú pháp: map(function, iterable, ...)
            function: Hàm thực thi cho từng phần tử trong iterable.
            iterable: một list, tuple, dictionary... muốn duyệt
            Giá trị trả về từ map() được gọi là map object. 
            Đối tượng này có thể được truyền vào các hàm list() 
            (để tạo list trong Python), hay set() (để tạo một set các phần tử mới)..
            e.g: list(map())
            """
            cipher_text += cipher

            cipher = '0b' + ''.join(str(i) for i in cipher)
            cipher = BitArray(cipher)

            print('{: ^15}{: ^15}{: ^15}{: ^15}{:^15}'.format(hex_plain, plain.bin, keystream.bin, cipher.bin, '0x' + cipher.hex))

        return cipher_text # cipher text dưới dạng list các bit 1 và 0

    def decrypt(self, cipher):
        plain_text = []

        hex_cipher = '0x' + cipher
        hex_cipher = BitArray(hex_cipher)

        for i in range(0, len(hex_cipher), 8):
            keystream = self.keystream(8) # list
            cipher_text = hex_cipher[i:i+8]
            
            bit_plain = [x ^ y for x, y in zip(map(int, list(cipher_text)), map(int, list(keystream)))]
            bit_plain = '0b' + ''.join(str(i) for i in bit_plain)
            char_plain = chr(int(bit_plain, 2))
            plain_text += char_plain

        plain_text_final = ''.join(i for i in plain_text)
        return plain_text_final

def print_menu():
    print("\nMenu program:");
    print("Enter 'k'  >> General random KEY 80 bits.")
    print("Enter 'iv' >> General random IV 80 bits .")
    print("Enter 'e'  >> Trivium Encrypt.")
    print("Enter 'd'  >> Trivium Decrypt.")
    print("Enter 'q'  >> Quit program.")

def main():
    print("\n\tTRIVIUM PROGRAM")
    while (1):
        print_menu()
        mode = str(input("Enter selection: "))

        # Chế độ encyption
        if mode == 'e':
            key = str(input("Enter key: "))
            iv = str(input("Enter iv: "))
            message = str(input("Enter message: "))

            # Khởi tạo Trivium
            KEY = '0x' + key
            KEY = BitArray(KEY) 
            print('{:<15}{:<2}{:<10}'.format('KEY', '=', KEY.hex))
            KEY = list(map(int, KEY.bin)) # Chuyển đổi key thành 1 list chứa các bit 0 và 1

            IV = '0x' + iv
            IV = BitArray(IV)
            print('{:<15}{:<2}{:<10}'.format('IV', '=', IV.hex))
            IV = list(map(int, IV.bin))

            trivium = Trivium(KEY, IV)
            print('{:<15}{:<2}{:<10}\n'.format('PLAIN TEXT', '=', message))
            print('{: ^15}{: ^15}{: ^15}{: ^15}{: ^15}'.format('INPUT', 'PLAIN TEXT', 'KEYSTREAM', 'CIPHER TEXT', 'OUTPUT'))
            print('{:->75}'.format(' '))
            
            cipher = trivium.encrypt(message)
            cipher = '0b' + ''.join(str(i) for i in cipher)
            cipher= BitArray(cipher)
            cipher_str = str(cipher)[2:]
            print("------------")
            print("CIPHER TEXT:", cipher_str)
        # Chế độ decyption
        elif mode == 'd':
            key = str(input("Enter key: "))
            iv = str(input("Enter iv: "))
            message = str(input("Enter cipher text: "))

            # Khởi tạo Trivium
            KEY = '0x' + key
            KEY = BitArray(KEY) 
            print('{:<15}{:<2}{:<10}'.format('KEY', '=', KEY.hex))
            KEY = list(map(int, KEY.bin)) # Chuyển đổi key thành 1 list chứa các bit 0 và 1

            IV = '0x' + iv
            IV = BitArray(IV)
            print('{:<15}{:<2}{:<10}'.format('IV', '=', IV.hex))
            IV = list(map(int, IV.bin))

            trivium = Trivium(KEY, IV)
            print('{:<15}{:<2}{:<10}\n'.format('CIPHER TEXT', '=', message))
            plain_text = trivium.decrypt(message)
            print('------------')
            print("PLAIN TEXT:", plain_text)
        elif mode == 'k':
            key_hex = str(BitArray(nacl.utils.random(10)))
            key = key_hex[2:]
            print('\nKey:', key)
        elif mode == 'iv':
            iv_hex = str(BitArray(nacl.utils.random(10)))
            iv = iv_hex[2:]
            print('\nIV: ', iv)
        elif mode == 'q':
            print("Program shutdown...")
            break

if __name__ == "__main__":
    main()
