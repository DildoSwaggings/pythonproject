import sys
import os

# Converts a list of binary strings to ASCII message
def binary_to_ascii(msg):
    return ''

# Caesar cipher
def caesar_decrypt(msg, k):
    return ""

# Vigenere cipher
def vigenere_decrypt(msg, k):
    return ""

def start(filename):
    '''
    TASK: Decrypt a list of binary-encoded encrypted messages.
    '''
    # TODO: read input file

    # TODO: Print solution


# No need to modify this
if __name__ == '__main__':
    # Get the first command line argument
    if len(sys.argv) < 2:
        print("Usage %s <input_file>" % (sys.argv[0],))
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("Could not find input file %s." % (filename,))
        sys.exit(1)
    start(filename)
