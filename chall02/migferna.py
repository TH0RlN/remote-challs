import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter.isalpha():
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ''
        else:
            if letter.isspace():
                cipher += ' '
            else:
                print "usage: ./xlogin.py <a-zA-Z string>"
                exit(1)

    return cipher

def main(argv):
  if len(argv) == 2 and len(argv[1]) > 0:
    result = encrypt(argv[1].upper()) 
    print (result) 
  else:
    print("usage: ./xlogin.py <a-zA-Z string>")

# Executes the main function
if __name__ == '__main__':
    main(sys.argv)