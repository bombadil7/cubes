"""
This program implements a solution to a SoloLearn programming challenge.
A message provided by the user will be encoded using a number of cubes.
Each cube will store 8 of the characters form the message in its corners, 
and then obscure their locations by means of rotations.  It can rotate up,
down, left and right.  The number, order and directions of rotations are
specified by an encryption key provided by the user.

This file creates a convenient graphical user interface to allow user:
- enter the message to encode
- enter desired encryption key
- generate a random encryption key
- encrypt the message and see the result
- decrypt the encrypted message and view the original

__________________________________________________________________
|                                         Original Message
|                                        ______________________      
|                                        | Message             |
| _________________________________      |_____________________|
| | generate random encryption key |       Enter Encryption Key
| |________________________________|     ______________________
|                                        | Key                 |
| _________________________________      |_____________________|
| | encrypt message                |       Encrypted Message
| |________________________________|     ______________________
|                                        | Encrypted Message   |
| _________________________________      |_____________________|
| | decrypt message                |       Decrypted Message
| |________________________________|     ______________________
|                                        | Decrypted Message   |
|      Clera all         Quit            |_____________________| 
|
|__________________________________________________________________

A user can enter a message and a key, then encrypt it, and decrtypt it again,
  or just a message and generate a key for it and then encrypt it, and decrypt it,
  or an encrypted message and a key and decrypt it.

  Should add a "clear all" button and "quit".

"""
from tkinter import *
from cubes import Encoder

window = Tk()
window.wm_title('Encoder')

gen_key_button = Button(window, text="Generate Random Key", width=18)
gen_key_button.grid(row=3, column=2)

encrypt_button = Button(window, text="Encrypt Message", width=18)
encrypt_button.grid(row=5, column=2)

decrypt_button = Button(window, text="Decrypt Message", width=18)
decrypt_button.grid(row=7, column=2)

clear_button = Button(window, text="Clear All", width = 6)
clear_button.grid(row=9, column=1)

quit_button = Button(window, text="Quit", width = 6)
quit_button.grid(row=9, column=3)

message_label = Label(window, text="Original Message", width=25)
message_label.grid(row=1, column=4)

key_label = Label(window, text="Enter Encryption Key", width=25)
key_label.grid(row=3, column=4)

encr_message_label = Label(window, text="Encrypted Message", width=25)
encr_message_label.grid(row=5, column=4)

decr_message_label = Label(window, text="Decrypted Message", width=25)
decr_message_label.grid(row=7, column=4)

message_text = StringVar()
message_entry = Entry(window, textvariable=message_text)
message_entry.grid(row=2, column=4)

key_text = StringVar()
key_entry = Entry(window, textvariable=key_text)
key_entry.grid(row=4, column=4)

encr_message_text = StringVar()
encr_message_entry = Entry(window, textvariable=encr_message_text)
encr_message_entry.grid(row=6, column=4)

decr_message_text = StringVar()
decr_message_entry = Entry(window, textvariable=decr_message_text)
decr_message_entry.grid(row=8, column=4)


window.mainloop()
