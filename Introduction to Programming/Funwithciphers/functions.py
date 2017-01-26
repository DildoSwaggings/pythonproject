'''
Created on 24 jan. 2017
Assigment Introduction to binary numbers
@author: Thom
'''

def to_binary(getal):
    if getal == 0:
        return ''
    else:
        return to_binary(getal/2) + str(getal%2)

getal = to_binary(0)
print getal

def to_decimal(bin):
    lijst = map(int, str(bin))
    print lijst
    som = int(0)
    teller = 0
    for element in lijst:
        som += element * 2**(int(len(lijst))-teller-1)
        teller += 1
    return som                    
    print som
    

# By using your function to decimal you can now decode the message.
def binary_to_ascii(lst):
    msg = ""
    for b in lst:
        decimal_value = int(to_decimal(b))
        msg += chr(decimal_value)
    print(msg)

 #ceasar encrypt functions:
 
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