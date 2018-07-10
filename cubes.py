import math
import sys

"""
         b2_____b3
        /|      /|
       / |     / |
      a2______a3 |
      |  b1___|_b4
      | /     | /
      |/      |/
      a1_____a4
"""

class Cube:

    def __init__(self, message):
        self.corners    = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
        self.down       = ['b1', 'a1', 'a4', 'b4', 'b2', 'a2', 'a3', 'b3']
        self.up         = ['a2', 'b2', 'b3', 'a3', 'a1', 'b1', 'b4', 'a4']
        self.right      = ['a4', 'a3', 'b3', 'b4', 'a1', 'a2', 'b2', 'b1']
        self.left       = ['b1', 'b2', 'a2', 'a1', 'b4', 'b3', 'a3', 'a4']

# Create an empty dictionary.  This way the cube has all the corners.
        self.ver = {}
        for k in self.corners:
            self.ver[k] = ''

# Fill in the corners with available letters
        mes = [message[i] for i in range(len(message))]
        for i, c in enumerate(mes):
            self.ver[self.corners[i]] = c

    def print_message(self):
        message = ''.join(self.ver[key] for key in self.corners)
        return message

    def rotate_up(self):
        temp = {}
        for i, key in enumerate(self.corners):
            temp[self.up[i]] = self.ver[key]
        self.ver = temp

    def rotate_down(self):
        temp = {}
        for i, key in enumerate(self.corners):
            temp[self.down[i]] = self.ver[key]
        self.ver = temp

    def rotate_left(self):
        temp = {}
        for i, key in enumerate(self.corners):
            temp[self.left[i]] = self.ver[key]
        self.ver = temp

    def rotate_right(self):
        temp = {}
        for i, key in enumerate(self.corners):
            temp[self.right[i]] = self.ver[key]
        self.ver = temp

        

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
    print(cube.print_message())
    cube.rotate_up()
    cube.rotate_down()
    cube.rotate_left()
    cube.rotate_right()
    print(cube.print_message())

