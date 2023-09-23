import re
import os
import sys
from pyfiglet import Figlet

# Morse Code Table
MORSE_CODE_DICT = { 'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ',':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-',
                    "'":".----.",
                    '!':'-.-.--',
                    '&':'.-...',
                    ':':'---...',
                    ';':'-.-.-.',
                    '=':'-...-',
                    '+':'.-.-.',
                    '_':'..--.-',
                    '"':'.-..-.',
                    '$':'...-..-',
                    '@':'.--.-.',
                    '&':'.-...'
                    }

def encrypt(text_message):
    cipher = ''
    for letter in text_message.upper():
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher = cipher + MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher = cipher + ' '
    return cipher.strip()

def decrypt(message):
    # extra space added at the end to access the last morse code
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        # checks for space
        if (letter != ' '):
            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                              .values()).index(citext)]
                citext = ''
    return decipher.title()

def check_encrypt_decrypt(text_data):
    # Define a pattern to match only '.' and '-'
    pattern1 = r'[.\s-]+$'

    # Define a pattern to match invalid characters
    pattern2 = r'[#%^*\[\]{}<>]'

    # Check for invalid characters
    if re.search(pattern2, text_data):
        sys.exit("Invalid characters present in the string")

    # Check if the string consists only of '.' and '-'
    res = re.match(pattern1, text_data)
    if res:
        return True
    else:
        return False

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    while True:
      figlet = Figlet()
      figlet.setFont(font='big')
      print(figlet.renderText('Morse Code '))
      print("Invalid Characters are : # % ^ *  [  ] { } < > ] ")
      print()
      text = input("Enter String: ")
      res = check_encrypt_decrypt(text)
      text_code = ''
      morse_code= ''
      flag=0
      if (bool(res)):
          flag = 1
          text_code=decrypt(text)
      else:
          flag = 0
          morse_code = encrypt(text)
      if(flag==0):
          print("Morse Code of String: ", morse_code)
      else:
          print("Decrypted Text is: ", text_code)
      run_again = input("Do you want to run the program again? (yes/no): ")
      if run_again.lower() != "yes" and run_again.lower() != "y":
          break  # Exit
      else:
          clear_screen()  # clear screen and run program


if __name__=="__main__":
    main()
