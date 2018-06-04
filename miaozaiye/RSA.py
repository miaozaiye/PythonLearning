# RSA algorithm to encrypt and decrypt data
'''
1. 随意选择两个大质数
2。根据欧拉函数，求的一个欧拉数 r = f(n) = f(p)f(a) = (p-1)(q-1)
3. 求得一个小于欧拉数r的整数e
4. 求的e关于r的模逆元 d
5. 其中（ n,e)是公钥，（n,d)是私钥
6。对于明文P和密文 C
7。加密： C= （P^e)mod n
8。解密：P = (C^d)mod n

'''

import random
import sys


def get_Eula(a,b):
    print('get_eula({0})'.format([a,b]))

    '''

    :param a:
    :param b:
    :return:
    '''

    lx = [1,0,b]
    ly = [0,1,a]
    while ly[2]!=1:
        if ly[2] !=0:
            return 0
        q = lx[2]/ly[2]
        lt = [lx[i]-ly[i]*q for i in range(3)]
        lx = ly
        ly = lt

    return ly[1]%b

def coprime(a,b):
    print('coprime({0})'.format([a,b]))
    if a < b:
        a,b = b,a
    while b!=0:
        t = a%b
        a = b
        b = t
    print('return {0}'.format([a,b]))
    return (a,b)

def get_e(e_n):
    print('get_e({0}'.format(e_n))
    flag = 1
    while flag:
        e = random.randrange(e_n)
        if coprime(e,e_n) == (1,0):
            print('coprime = (1,0)')
            flag = 0
    print('return: ',e)
    return e



def encrypt(plaintext,n,e):
    '''
    先将文字转换成utf-8码
    再将utf-8码转换成加密数字
    :param text:
    :param n:
    :param e:
    :return:
    '''
    print('encrypt({0}'.format([plaintext,n,e]))

    ciphertext = [pow(c,e,n).to_bytes(8,byteorder='big',signed = False) for c in plaintext]
    print('ciphertext is:',ciphertext)

    return b''.join(ciphertext)

def decrypt(text_encrypted,d,n):
    ciphertext = [pow(c,d,n).to_bytes(8,byteorder='big',signed = False) for c in text_encrypted]
    print('ciphertext is:',ciphertext)
    return b''.join(ciphertext)

def AKS(a,n):
    print('ASK({0}'.format([a,n]))
    if pow(17-a,n,n) == pow(17,n,n)-(a%n):
        return 1
    else:
        return 0

def big_rand():
    print('big_rand')
    flag = 0
    l,u = 2**16,2**32
    while not flag:
        n = random.randrange(l,u)
        if any([n%x == 0 for x in[2,3,5,7,13]]):
            continue
        flag = AKS(2,n)

    print('return {0}'.format(n))
    return n
    pass


def get_key():
    print('get_key()')
    p = big_rand()
    q = big_rand()
    n = p*q
    e_n = n-p-q+1
    e = get_e(e_n)
    d = get_Eula(e,e_n)

    print('return{0}'.format([e,n,e_n,d,p,q]))
    return[e,n,e_n,d,p,q]


def main():
    print('main function starts')
    k = get_key()
    text = 'like you'.encode('utf8')
    print('text is:',text)
    encrypted_text = encrypt(text,k[0],k[1])
    print(encrypted_text)

    decrypted_text = decrypt(encrypted_text,k[3],k[1])

    print(decrypted_text)

main()