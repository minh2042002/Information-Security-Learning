#include <iostream>
#include <string>
using namespace std;

string Encrypt(int a, int b, string x) {
   string y;
   for (int i = 0; i < x.length(); i++)
      y += (char)((a * (x[i]-'a') + b+26) % 26+'a');
   return y;
}

string Decrypt(int inverse_a, int b, string y) {
   string x;
   for (int i = 0; i < y.length(); i++) {
      x = x + (char)(inverse_a * ((int)(y[i] - 'a') - b + 26) % 26 + 'a');
   }
   return x;
}
int modInverse(int a, int m) {
   for (int x = 1; x < m; x++)
      if (((a % m) * (x % m)) % m == 1) return x;
   return 1;
}

int main() {
   int a, b, c;
   // a = [1,3,5,7,9,11,15,17,19,21,23,25]
   string str;
   cout << "\nInsert Key: a=";
   cin >> a;
   cout << "\nInsert Key: b=";
   cin >> b;
   cout << "\nEnter string: ";
   cin >> str;
   cout << "\nType 0 to Encrypt, type 1 to Decrypt: ";

   cin >> c;
   if (c)
      cout << Decrypt(modInverse(a, 26), b, str);
   else
      cout << Encrypt(a, b, str);

   return 0;
}