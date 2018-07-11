import math

def split_phrase(phrase):
    # Create a list of sub-strings from the message, which will fit into a cube
    phrase_list = []
    phr = ''
    num_strings = math.ceil(len(phrase) / 8)
    for i, c in enumerate(phrase):
        phr += c
        if i > 0 and (i+1) % 8 == 0 or i == (len(phrase) - 1):
            phrase_list.append(phr)
            phr = ''


    return phrase_list
message = 'This is a security message'
print(split_phrase(message))        

