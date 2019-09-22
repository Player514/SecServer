import sympy
class diffhellman:
    def __init__(self):
        self.sharedPrime = sympy.randprime(1,100)
        self.sharedBase = 8
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