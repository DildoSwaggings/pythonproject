'''
Created on 24 jan. 2017
Assigment Ceaser cipher
@author: Thom
'''

from functions import to_binary, to_decimal, binary_to_ascii
#questions for werkcollege: how about CAPITALLETTERS?
#start with functions for single letter encryption

def ceasar_encrypt_single_letter(letter, sleutel):
    encrypted_character = chr(((ord(letter)-ord('a')+sleutel)%26)+ord('a'))
    return encrypted_character

def ceasar_decrypt_single_letter(decrypted_character, sleutel):
    decrypted_character = chr(((ord(decrypted_character)-ord('a')-sleutel)%26)+ord('a'))
    return decrypted_character

#Now use the single letter functions for entire sentences

def ceasar_encrypt_sentence(string_sentence, key):
    lijst = list(string_sentence)
    encrypted_sentence = ''
    for letter in lijst:
        encrypted_letter = ceasar_encrypt_single_letter(letter, key)
        encrypted_sentence += encrypted_letter
    print encrypted_sentence
    return encrypted_sentence

def ceasar_decrypt_sentence(string_decrypted_sentence, key):
    lijst = list(string_decrypted_sentence)
    decrypted_sentence = ''
    for letter in lijst:
        decrypted_letter = ceasar_decrypt_single_letter(letter, key)
        decrypted_sentence += decrypted_letter
    print decrypted_sentence
    return decrypted_sentence

ceasar_decrypt_sentence('jgnnq', 2)

'''
print ceasar_decrypt_single_letter('b', 1)
test = ceasar_encrypt_single_letter('h', 25)
print 'dit is de test: %s'%test
print chr(((ord('b')-ord('a')+0)%26)+ord('a'))
print ord('a')
'''