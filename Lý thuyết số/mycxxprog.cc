#include <iostream>
#include <gmpxx.h> 
#include <assert.h>
using namespace std;

void rsa_keys(mpz_t n, mpz_t d, const mpz_t p, const mpz_t q, const mpz_t e) {    
    mpz_mul(n, p, q);
    
    mpz_t p_1, q_1, e_1;
    mpz_inits(p_1, q_1, NULL); 
    
    mpz_t phi;
    mpz_inits(phi);   
    
    mpz_sub_ui(p_1, p, 1);    
    mpz_sub_ui(q_1, q, 1);    
    mpz_mul(phi, p_1, q_1);   
    
    mpz_t gcd;      
    mpz_init(gcd);    
    mpz_gcd(gcd, e, phi); 
    // void mpz_gcd (mpz_t g, const mpz_t a, mpz_t b)
    // g = gcd(a,b)
    // void mpz_gcdext (mpz_t g, mpz_t x, mpz_t y, const mpz_t a, const mpz_t b,)
    // (g,x,y) = gcdx(a,b)
    // g = a*x + b*y 

    assert(mpz_cmp_ui(gcd, 1) == 0);  
    // phải thoả mãn gcd (e, phi) == 1                                                                        
    // mới có nghịch đảo    
    
    mpz_invert(d, e, phi);            
    // d = e^-1 mod phi(n)    
    mpz_clears(gcd, p_1, q_1, NULL);
    
}

void encrypt(mpz_class c, 
            const mpz_t m, 
            const mpz_t e, 
            const mpz_t n) {
    mpz_t encrypted;
    mpz_init(encrypted);
    mpz_powm(encrypted, m, e, n);
    // void mpz_pown (mpz_t z, const mpz_t a, const mpz_t b, const mpz_t n)
    // z = a^b mod n
    mpz_class result{encrypted};
    mpz_clear(encrypted);
    c = result;
}

void decrypt(mpz_class m,             
            const mpz_t c,            
            const mpz_t d,             
            const mpz_t n) {        
    mpz_t original;
    mpz_init(original);
    mpz_powm(original, c, d, n);
    mpz_class result{original};
    mpz_clear(original);
    m = result;                
}
int main(void)
{
    mpz_class a, b, c;

    a = 1234;
    b = "-5678";
    c = a+b;
    cout << "sum is " << c << "\n";
    cout << "absolute value is " << abs(c) << "\n";

    return 0;
}
