
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_decode(message, offset):
    final_msg = ""
    for character in message:
        if character in alphabet:
            position = alphabet.find(character)
            final_msg += alphabet[(position + offset) % 26]
        else:
            final_msg += character
    return final_msg

def caesar_encode(message, offset):
    value_of = -offset
    return caesar_decode(message, value_of)

def vig_cihper(message, keyword):
    key_phrase = ""
    counter = 0
    final_msg = ""
    for character in message:
        if character in alphabet:
            key_phrase += keyword[counter]
            counter += 1
            if counter == len(keyword):
                counter = 0
        else:
            key_phrase += character
    for i, letter in enumerate(message):
        final_msg += caesar_encode(letter, (26 - (alphabet.find(key_phrase[i]))))
    
    return final_msg

def vig_encryption(message, keyword):
    key_phrase = ""
    counter = 0
    final_msg = ""
    for character in message:
        if character in alphabet:
            key_phrase += keyword[counter]
            counter += 1
            if counter == len(keyword):
                counter = 0
        else:
            key_phrase += character
    for i, letter in enumerate(message):
        final_msg += caesar_encode(letter, ((alphabet.find(key_phrase[i]))))
    
    return final_msg
