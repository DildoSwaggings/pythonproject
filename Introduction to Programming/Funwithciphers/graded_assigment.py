'''
Created on 26 jan. 2017

@author: Thom
'''
from functions import to_binary, to_decimal, binary_to_ascii, ceasar_encrypt_single_letter, ceasar_decrypt_single_letter, ceasar_encrypt_sentence, ceasar_decrypt_sentence

#define vignere encrypt and decrypt sentence:
def vignere_encrypt_sentence(sentence, keyword):
    list_sentence = list(sentence)
    list_keyword = list(keyword)
    #print list_sentence
    #print list_keyword
    if len(list_sentence) < len(list_keyword):
        while len(list_sentence) < len(list_keyword):
            list_keyword = list_keyword[0:-1]
    else:
        index = int(0)
        while len(list_sentence) > len(list_keyword):
            list_keyword.append(list_keyword[index])
            index += 1
    #print list_sentence
    #print list_keyword
    vignere_encrypted_sentence = ''
    teller = int(0)
    for letter in list_sentence:
        vignere_encrypted_letter = ceasar_encrypt_single_letter(letter, ord(list_keyword[teller]))
        teller +=1
        vignere_encrypted_sentence += vignere_encrypted_letter
    #print vignere_encrypted_sentence
    return vignere_encrypted_sentence

def vignere_decrypt_sentence(encrypted_sentence, keyword):
    list_encrypted_sentence = list(encrypted_sentence)
    list_keyword = list(keyword)
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

if __name__ == '__main__':
    #testing    
    vignere_encrypt_sentence('ATTACKADAWN', '  ')
    vignere_decrypt_sentence('attackdawn', ' ')
    print 'test'





    