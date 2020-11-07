import sys
import math
import random


max_PrimLength = int(math.sqrt(sys.maxsize))

class Rsa:

    def imod(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.imod(b % a, a)
            return (g, x - (b // a) * y, y)

    def is_prime(self,n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        max_ = math.floor(math.sqrt(n)) + 1

        for divisor in range(3, max_, 2):
            if n % divisor == 0:
                return False
        return True

    def generate_prime_number(self):
        while (1):
            ranPrime = random.randint(10, max_PrimLength)
            if self.is_prime(ranPrime):
                return ranPrime

    def generate_keyPairs(self,p1,p2):

        n = p1 * p2
        phi = (p1 - 1) * (p2 - 1)

        e = random.randint(1, phi)
        g = math.gcd(e, phi)
        while g != 1:
            e = random.randint(1, phi)
            g = math.gcd(e, phi)

        d = self.imod(e, phi)[1]


        d = d % phi
        if (d < 0):
            d += phi

        return ((e, n), (d, n))


    def pow_function(self,base, exp,n):

        result = 1

        while True:
            if exp & 1:
                result = (result * base % n)
            exp >>= 1
            if not exp:
                break
            base = (base * base % n )

        return result


    def decrypt(self,cipher_text, private_key):
        try:
            key, n = private_key

            text = []

            for item in cipher_text:

                unicode_value = self.pow_function(item,key,n)
                character = chr(unicode_value)
                text.append(character)
            original_text = "".join(text)

            return original_text

        except TypeError as e:
            print(e)

    def encrypt(self,plain_text, public_key):
        key, n = public_key
        cypher_text = []

        for single_character in plain_text:

            unicode = ord(single_character)
            cipher = self.pow_function(unicode,key,n)
            cypher_text.append(cipher)

        return cypher_text
