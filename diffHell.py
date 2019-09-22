import sympy
from math import gcd as bltin_gcd
import random
class diffhellman:
    def __init__(self):
        self.sharedPrime = sympy.randprime(1,100)
        required_set = {num for num in range(1, self.sharedPrime) if bltin_gcd(num, self.sharedPrime) }
        self.sharedBase = random.choice([g for g in range(1, self.sharedPrime) if required_set == {pow(g, powers, self.sharedPrime)
                                                        for powers in range(1, self.sharedPrime)}]) % self.sharedPrime
        self.secretKey = None
        self.encodedMessage = None

    def handshake(self, sharedPrime, sharedBase):
        self.sharedBase = sharedBase
        self.sharedPrime = sharedPrime

    def SendSecret(self, secret):
        self.secretKey = secret
        return self.sharedBase ** self.secretKey % self.sharedPrime

    def decode(self, encodedMessage):
        self.encodedMessage = encodedMessage
        return (self.encodedMessage ** self.secretKey) % self.sharedPrime