import click
import nacl.utils
from bitstring import BitArray 


@click.command()
@click.option('-iv', type= str,default= False, help='Generate 80 bit IV in hex.')
@click.option('-k', type= str, default= False, help='Generate 80 bit Key in hex.')
def do_work(iv, k): 
    if iv == 'y':
        iv_hex = str(BitArray(nacl.utils.random(10)))
        iv = iv_hex[2:]
        print('IV: ', iv)
    if k == 'y': 
        key_hex = str(BitArray(nacl.utils.random(10)))
        key = key_hex[2:]
        print('Key:', key)
        
if __name__ == '__main__':
    do_work()