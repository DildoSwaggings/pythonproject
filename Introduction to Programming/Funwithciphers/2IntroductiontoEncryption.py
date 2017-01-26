'''
Created on 24 jan. 2017
Assigment Ceaser cipher
@author: Thom
'''

from functions import to_binary, to_decimal, binary_to_ascii
#questions for werkcollege: how about CAPITALLETTERS?
#start with functions for single letter encryption
#constants
ASCII_NUMBER = 256

def ceasar_encrypt_single_letter(letter, sleutel):
    encrypted_character = chr((ord(letter)+sleutel)%ASCII_NUMBER)
    return encrypted_character

def ceasar_decrypt_single_letter(encrypted_character, sleutel):
    decrypted_character = chr((ord(encrypted_character)-sleutel)%ASCII_NUMBER)
    return decrypted_character

#Now use the single letter functions for entire sentences

def ceasar_encrypt_sentence(string_sentence, key):
    lijst = list(string_sentence)
    encrypted_sentence = ''
    for letter in lijst:
        encrypted_letter = ceasar_encrypt_single_letter(letter, key)
        encrypted_sentence += encrypted_letter
    #print encrypted_sentence
    return encrypted_sentence

def ceasar_decrypt_sentence(string_encrypted_sentence, key):
    lijst = list(string_encrypted_sentence)
    decrypted_sentence = ''
    for letter in lijst:
        decrypted_letter = ceasar_decrypt_single_letter(letter, key)
        decrypted_sentence += decrypted_letter
    #print decrypted_sentence
    return decrypted_sentence

#testing the encrypt and decrypt functions
m = "hallo ik ben thom %% r 3 0 ()"
for k in range(1,1024):
    if ceasar_decrypt_sentence(ceasar_encrypt_sentence(m, k), k) != m:
        print ("Error for key %d on %s" %(k, m))
print 'lekker bezig'
print ceasar_decrypt_sentence('jgnnq hoi', 2)
print ceasar_encrypt_sentence('hallo ik ben thom %% r 3 0 ()', 2)

'''
print ceasar_decrypt_single_letter('b', 1)
test = ceasar_encrypt_single_letter('h', 25)
print 'dit is de test: %s'%test
print chr(((ord('b')-ord('a')+0)%26)+ord('a'))
print ord('a')
'''