import random
import sympy
class diffhellman:
    def __init__(self):
        self.sharedPrime = 23  #sympy.randprime(1,100)
        self.sharedBase = 5
        self.secretKey = None

    def handshake(self, sharedPrime, sharedBase):
        self.sharedPrime = sharedPrime
        self.sharedPrime = sharedBase
    def encode(self, secretKey):
        if self.secretKey != type(int):
            print('Please type a natural number:')
            self.secretKey = int(input())

        return self.sharedBase ** self.secretKey % self.sharedPrime
    def decode(self):
        pass



test = diffhellman()

test.encode('dfg')
