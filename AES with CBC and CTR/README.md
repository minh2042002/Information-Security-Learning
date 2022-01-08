### AES with CBC mode and CTR mode use Python

## Installation
Sử dụng thư viện argparse
```
    pip install argparse
Sử dụng thư viện Pycryptodome
```
    pip install pycryptodome

## Usage
@Tạo key ngẫu nhiên 
```
Cú pháp: python aes.py -m key

@Chạy chương trình với chế độ CBC
```
Encrypt:
    Cú pháp: python aes.py -m cbc -s e -k [KEY] -t [MESSAGE]
```
Decrypt:
    Cú pháp: python aes.py -m cbc -s d -k [KEY] -iv [IV] -t [MESSAGE]

@Chạy chương trình với chế độ CTR
```
Encrypt:
    Cú pháp: python aes.py -m ctr -s e -k [KEY] -t [MESSAGE]
```
Decrypt:
    Cú pháp: python aes.py -m ctr -s e -k [KEY] -n [NONCE] -t [MESSAGE]

positional arguments:
    -t MESSAGE             bản rõ hoặc bản mã
optional arguments:
    -h, --help          hiển thị trợ giúp
    -m, --mode {cbc, ctr, key}  
                        chọn mode:
                        cbc - CBC mode
                        ctr - CTR mode
                        key - tạo key ngẫu nhiên
    -s, --selection {e, d}    
                        Chọn chế độ encrypt hoặc decrypt
    -k, --key KEY       khóa sử dụng có độ dài 16 bytes
    -iv, --iv IV        Iv sử dụng cho CBC mode
    -n, --nonce NONCE   Nonce sử dụng cho CTR mode
```