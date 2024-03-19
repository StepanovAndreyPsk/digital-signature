from sympy import gcd, mod_inverse, randprime
import random


class PublicKey:
    def __init__(self, e: int, n: int):
        self.e = e
        self.n = n


class PrivateKey:
    def __init__(self, d: int, n: int):
        self.d = d
        self.n = n


def random_prime(n: int = 1024) -> int:
    return randprime(2 ** (n - 1), 2 ** n - 1)


def get_coprime_number(n: int) -> int:
    x = random.randint(2, n)
    while gcd(x, n) != 1:
        x = random.randint(2, n)
    return x


def generate_keypair() -> (PublicKey, PrivateKey):
    p = random_prime()
    q = random_prime()
    n = p * q
    m = (p - 1) * (q - 1)
    e = get_coprime_number(m)
    d = mod_inverse(e, m)
    return PublicKey(e, n), PrivateKey(d, n)


def encrypt(msg: str, pub_key: PublicKey) -> int:
    return pow(int(msg), pub_key.e, pub_key.n)


def decrypt(ciphertext: int, private_key: PrivateKey) -> str:
    return str(pow(ciphertext, private_key.d,  private_key.n))
