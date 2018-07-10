import math
import sys

class Cube:

    def __init__(self, message):
        self.vert = [c for c in message if len(message) > 0 and len(message) < 9]

    def print_message(self):
        for c in self.vert:
            print(c)
        

#class Encoder():
#    def encode(self, phrase, key):
#"""
#        encode receives a phrase to encrypt and a key, and 
#        it returns the encrypted version of that phrase.
#
#        The number of cubes required and rotation sequence comes
#        as a key.  
#"""
#
#        return encoded_phrase 
#
#
#    def decode(self, phrase ,key):
#"""
#        decode receives an encrypted phrase and a key, and returns
#        that phrase decrypted per the key's instructions.
#"""
#
#        return word
#
#    def keyGenerator(self, phrase):
#"""
#        keyGenerator is just a utility function, which makes generating
#        random encryption keys easier.
#        All it does is return a new random key back to the caller.
#
#        In order to know how many cubes to use for the encryption we 
#        need the phrase as an input.
#"""
#        num_cubes = math.ceil(len(phrase) / 8)  # there are 8 corners for 8 letters
#
#        for c in range(num_cubes):
#
#
#
#        return key

if __name__=='__main__':
    if  len(sys.argv) > 1:
        phrase = sys.argv[1]
        
    else:
        phrase = 'Secure'

    cube = Cube(phrase)
    cube.print_message()
