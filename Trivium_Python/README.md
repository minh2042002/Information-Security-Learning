# Trivium
## Installation
Yêu cầu cài đặt thư viện bitstring 
```
pip install bitstring
```
Yêu cầu cài đặt thư viện PyNaCL
```
pip install PyNaCL
```

## Usage
@Tạo dãy bit ngẫu nhiên IV và KEY
```
Cú pháp: python trivium.py -m iv
         python trivium.py -m key

optional:
  iv                  tạo dãy IV dưới dạng hexa độ dài 80 bit
  key                 tạo khóa Key dưới dạng hexa độ dài 80 bit
```

@Chạy chương trình trivium
```
Cú pháp: python trivium.py [-m {e,d}] [-k, --key KEY] [-iv IV] -t message
Ví dụ về cú pháp:
python trivium.py -m e -k 29bf54b7dffa7a7fe4ed -iv ca65c826cbe6cf2241f9 ABCD
```

Encyption và Decyption với thuật toán hệ mã dòng Trivium.

positional arguments:
  message               bản rõ hoặc bản mã

optional arguments:
  -h, --help            hiển thị trợ giúp, hướng dẫn sử dụng chương trình CLI
  -m {e,d}
                        chọn chế độ: e - Encyption, d - Decyption
  -k, --key KEY         key có độ dài 80 bit e.g.: 29bf54b7dffa7a7fe4ed
  -iv IV                IV có độ dài 80 bit e.g.: ca65c826cbe6cf2241f9
                        
```