# simple encryption algorithm
try:
    import pyperclip #copies text to clipboard
except ImportError:
    pass

# set up the constants
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

print('Encryption by wanyekey@github.com')
print()
while True: #Main program loop
    print("Enter a message to encrypt/decrypt(or QUIT):")
    message = input("> ")
    
    if message.upper() == "QUIT":
        break #out of the main loop

    #rotate the letters in message by 13 characters hence the name rot13cipher
    translated = ''
    for character in message:
        if character.isupper():
            #concatenate uppercase translated character
            transCharIndex = (UPPER_LETTERS.find(character) + 13) % 26
            translated += UPPER_LETTERS[transCharIndex]

        elif character.islower():
            #concatenate lowercase translated character
            transCharIndex = (LOWER_LETTERS.find(character) + 13) % 26
            translated += LOWER_LETTERS[transCharIndex]

        else:
            #concatenate the character untranslated
            translated += character

    #display the translation
    print("The translated message is: ")
    print(translated)
    print()

    try:
        #copy translation to clipboard
        pyperclip.copy(translated)
        print("(Copied to clipboard.)")
    except:
        pass
