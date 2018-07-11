import math
import sys
import random

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

    def get_message(self):
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

        

class Encoder():
    def encode(self, phrase, key):
        """
        encode receives a phrase to encrypt and a key, and 
        it returns the encrypted version of that phrase.

        The number of cubes required and rotation sequence comes
        as a key.  
        """

        # We will create a list of lists from the key
        # The main list will be a list of cubes and for each cube
        # we will have a list of rotations.  That should work.
        # A key looks like this:   0:U:U:L:D,1:D,2:L:U:L
        cube_list = key.split(',')
        ops_list = []
        for cube in cube_list:
            ops = cube.split(':')
            ops_list.append(list(ops[1:]))

        # Create a list of sub-strings from the message which will fit into a cube
        phrase_list = []
        phr = ''
        for i, c in enumerate(phrase):
            phr += c
            if i > 0 and (i+1) % 8 == 0 or i == (len(phrase) - 1):
                phrase_list.append(phr)
                phr = ''

        print(phrase_list)
        

        # Now we encode the message according to these instructions
        encoded_phrase = ''
        self.encoding = []
        for cube_ops, sub_phrase in zip(ops_list, phrase_list):
            cube = Cube(sub_phrase)
            for op in cube_ops:
                if op == 'U':
                    cube.rotate_up()
                elif op == 'D':
                    cube.rotate_down()
                elif op == 'L':
                    cube.rotate_left()
                else:
                    cube.rotate_right()
            print(cube.get_message())  
            self.encoding.append(cube)
            encoded_phrase += cube.get_message()
        
        return encoded_phrase 


    def decode(self, phrase ,key):
        """
        decode receives an encrypted phrase and a key, and returns
        that phrase decrypted per the key's instructions.
        """

        return word

# TODO: need to change this method into something like class method or static to
# allow people to call it without instantiating the class
    def keyGenerator(self, phrase):
        """
        keyGenerator is just a utility function, which makes generating
        random encryption keys easier.
        All it does is return a new random key back to the caller.

        In order to know how many cubes to use for the encryption we 
        need the phrase as an input.

        An example of an encryption key is:
        0:U:U:L:D,1:D,2:L:U:L
        Here cube 0 is rotated up, up, left, down,
        cube 1 is rotated down, and cube 2 is rotated left, up, left
        """
        # First determine how many cubes are required to hold the message
        # Last cube may not be filled completely
        num_cubes = math.ceil(len(phrase) / 8)  # there are 8 corners for 8 letters

        # Now for each cube we assign a random number of rotations in random directions
        dirs = ['U', 'D', 'L', 'R']
        key = ''
        for c in range(num_cubes):
            if c > 0:
                key += ','
            key += str(c)
            # Select random number of rotations
            for rot in range(1, random.randint(2, 5)):
                # Each time we pick a random direction
                key += ':' + dirs[random.randint(0, len(dirs) - 1)]
        return key

def main():
    if  len(sys.argv) > 1:
        phrase = sys.argv[1]
    else:
        phrase = 'Security is the key to prosperity'

#    cube = Cube(phrase)
#    print(cube.print_message())
#    cube.rotate_up()
#    cube.rotate_down()
#    cube.rotate_left()
#    cube.rotate_right()
#    print(cube.print_message())

    encoder = Encoder()
    print(phrase + ' is ' + str(len(phrase)) + " characters long")
    key = encoder.keyGenerator(phrase)
    print(key)
    encoded_phrase = encoder.encode(phrase, key)
    print(encoded_phrase)


if __name__=='__main__':
    main()

