'''
Created on Jan 26th, 2017
Graded Assignment module 4, from skeleton
@author: Thom
'''
###importing###
import sys
import os

###CONSTANTs###
ASCII_NUMBER = 256

###functions###

# Converts a list of binary strings to ASCII message
def binary_to_ascii(lst):
    msg = ""
    for b in lst:
        decimal_value = int(to_decimal(b))
        msg += chr(decimal_value)
    return msg

def to_decimal(bin):
    list = map(int, str(bin))
    sum = int(0)
    counter = 0
    for element in list:
        sum += element * 2**(int(len(list))-counter-1)
        counter += 1
    return sum 

# Caesar cipher
def ceasar_decrypt_single_letter(encrypted_character, sleutel):
    decrypted_character = chr((ord(encrypted_character)-sleutel)%ASCII_NUMBER)
    return decrypted_character

def caesar_decrypt(msg, k):
    lijst = list(msg)
    decrypted_sentence = ''
    for letter in lijst:
        decrypted_letter = ceasar_decrypt_single_letter(letter, k)
        decrypted_sentence += decrypted_letter
    return decrypted_sentence

# Vigenere cipher
def vigenere_decrypt(msg, k):
    list_encrypted_sentence = list(msg)
    list_keyword = list(k)
    if len(list_encrypted_sentence) < len(list_keyword):
        while len(list_encrypted_sentence) < len(list_keyword):
            list_keyword = list_keyword[0:-1]
    else:
        index = int(0)
        while len(list_encrypted_sentence) > len(list_keyword):
            list_keyword.append(list_keyword[index])
            index += 1
    vigenere_decrypted_sentence = ''
    counter = int(0)
    for letter in list_encrypted_sentence:
        vigenere_decrypted_letter = ceasar_decrypt_single_letter(letter, ord(list_keyword[counter]))
        counter +=1
        vigenere_decrypted_sentence += vigenere_decrypted_letter
    return vigenere_decrypted_sentence


#reads input and calls decrypt_caesar_or_vignere(...) function
def split_single_sentence_and_decrypt(sentence_to_decrypt):
    encryptionmethod_keyword_binary = sentence_to_decrypt.split(':')
    method = encryptionmethod_keyword_binary[0]
    keyword = encryptionmethod_keyword_binary[1]
    binary = encryptionmethod_keyword_binary[2]
    list_with_binary_code = binary.split()
    decrypt_caesar_or_vigenere(method, keyword, list_with_binary_code)
    

#decrypts message using caesar or vigenere, depending on input
def decrypt_caesar_or_vigenere(method, keyword, list_with_binary_code):
    if method == 'vigenere':
        input_in_ascii = binary_to_ascii(list_with_binary_code)
        decrypted_sentence = vigenere_decrypt(input_in_ascii, keyword)
        print decrypted_sentence
    elif method == 'caesar':
        keyword = int(keyword)
        input_in_ascii = binary_to_ascii(list_with_binary_code)
        decrypted_sentence = caesar_decrypt(input_in_ascii, keyword)
        print decrypted_sentence
    else:
        print 'There was an error in recognizing the encryption method by decrypting \
the sentence with input:\"%s:%s:%s \".'%(method,keyword,list_with_binary_code)
  
#reads file and starts the whole process
def start(filename):
    file = open(filename)
    invoer = file.read()
    list_of_sentences_to_decrypt = invoer.split('\n') 
    for sentence_to_decrypt in list_of_sentences_to_decrypt:
        split_single_sentence_and_decrypt(sentence_to_decrypt)

###EXECUTE###
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
    

