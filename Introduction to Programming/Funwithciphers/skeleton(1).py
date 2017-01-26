'''
Created on 26 jan. 2017
Graded assigment module 4, from skeleton
@author: Thom
'''

import sys
import os
from functions import to_binary, to_decimal, binary_to_ascii, ceasar_encrypt_single_letter, ceasar_decrypt_single_letter, ceasar_encrypt_sentence, ceasar_decrypt_sentence
from graded_assigment import vignere_encrypt_sentence, vignere_decrypt_sentence

##################
ASCII_NUMBER = 256
''' 
def ceasar_encrypt_single_letter(letter, sleutel):
    encrypted_character = chr((ord(letter)+sleutel)%ASCII_NUMBER)
    return encrypted_character

def ceasar_decrypt_single_letter(encrypted_character, sleutel):
    decrypted_character = chr((ord(encrypted_character)-sleutel)%ASCII_NUMBER)
    return decrypted_character

#Now use the single letter functions for entire sentences

def ceasar_encrypt_sentence(string_sentence, key):
    

def ceasar_decrypt_sentence(string_encrypted_sentence, key):
    
#############''' 

# Converts a list of binary strings to ASCII message

def binary_to_ascii(lst):
    msg = ""
    for b in lst:
        decimal_value = int(to_decimal(b))
        msg += chr(decimal_value)
    return msg

# Caesar cipher
def caesar_decrypt(msg, k):
    lijst = list(msg)
    decrypted_sentence = ''
    for letter in lijst:
        decrypted_letter = ceasar_decrypt_single_letter(letter, k)
        decrypted_sentence += decrypted_letter
    #print decrypted_sentence
    return decrypted_sentence

# Vigenere cipher
def vigenere_decrypt(msg, k):
    list_encrypted_sentence = list(msg)
    list_keyword = list(k)
    #print list_encrypted_sentence
    #print list_keyword
    if len(list_encrypted_sentence) < len(list_keyword):
        while len(list_encrypted_sentence) < len(list_keyword):
            list_keyword = list_keyword[0:-1]
    else:
        index = int(0)
        while len(list_encrypted_sentence) > len(list_keyword):
            list_keyword.append(list_keyword[index])
            index += 1
    #print list_encrypted_sentence
    #print list_keyword
    vignere_decrypted_sentence = ''
    teller = int(0)
    for letter in list_encrypted_sentence:
        vignere_decrypted_letter = ceasar_decrypt_single_letter(letter, ord(list_keyword[teller]))
        teller +=1
        vignere_decrypted_sentence += vignere_decrypted_letter
    #print vignere_decrypted_sentence
    return vignere_decrypted_sentence

def start(filename):
    '''
    TASK: Decrypt a list of binary-encoded encrypted messages.
    '''
    # TODO: read input file
file = open('01_all.txt')
invoer = file.read()
list_of_sentences_to_decrypt = invoer.split('\n')
#print list_of_sentences_to_decrypt

def split_single_sentence(sentence_to_decrypt):
    encryptionmethod_keyword_binary = sentence_to_decrypt.split(':')
    return encryptionmethod_keyword_binary

def determine_encryption_method(sentence_to_decrypt):
    encryptionmethod = split_single_sentence(sentence_to_decrypt)[0]
    #print encryptionmethod
    return encryptionmethod

def read_keyword(sentence_to_decrypt):
    #lijst = sentence_to_decrypt.split(':')
    keyword = split_single_sentence(sentence_to_decrypt)[1]
    #print keyword
    return keyword

#read_keyword(list_of_sentences_to_decrypt[0])

def read_binary_code(sentence_to_decrypt):
    binary_code = split_single_sentence(sentence_to_decrypt)[2]
    lijst_met_binary_code = binary_code.split()
    return lijst_met_binary_code
    
#read_binary_code(list_of_sentences_to_decrypt[0])
#determine_encryption_method(list_of_sentences_to_decrypt[0])
    # TODO: Print solution
    
for sentence_to_decrypt in list_of_sentences_to_decrypt:
    if determine_encryption_method(sentence_to_decrypt) == 'vigenere':
        keyword = read_keyword(sentence_to_decrypt)
        input_in_ascii = binary_to_ascii(read_binary_code(sentence_to_decrypt))
        decrypted_sentence = vigenere_decrypt(input_in_ascii, keyword)
        print decrypted_sentence
    elif determine_encryption_method(sentence_to_decrypt) == 'caesar':
        keyword = int(read_keyword(sentence_to_decrypt))
        input_in_ascii = binary_to_ascii(read_binary_code(sentence_to_decrypt))
        decrypted_sentence = caesar_decrypt(input_in_ascii, keyword)
        print decrypted_sentence
    else:
        print 'There was an error in recognizing the encryption method by decrypting \
the sentence with input:\"%s \".'%sentence_to_decrypt

  

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
