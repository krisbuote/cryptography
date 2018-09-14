import string

''' --- CAESARIAN CIPHERZ --- '''
''' Plaintext is shifted an int. See "substitution cipher" on wikipedia. '''
''' Author: Kristopher Buote '''

def buildCoder(shift):
    assert shift >=0 and shift <=26
    coder = dict()
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    alpha_length = len(alpha_lower)

    # Use a dictionary to map the input char to the shifted char
    # e.g. coder['a'] = 'd' if shift == 3
    # The coder dictionary handles lower case and upper case letters
    for i in range(-shift, alpha_length-shift):
        char_lower = alpha_lower[i]
        char_lower_shifted = alpha_lower[i+shift]

        char_upper = alpha_upper[i]
        char_upper_shifted = alpha_upper[i+shift]

        coder[char_lower] = char_lower_shifted
        coder[char_upper] = char_upper_shifted

    return coder

def applyCoder(plaintext, coder):

    # alphabetic characters are ciphered, punctation remains constant
    ciphertext = []

    for char in plaintext:
        if char in coder:
            cipherChar = coder[char]
            ciphertext.append(cipherChar)
        else:
            ciphertext.append(char)

    # Return the joined list of characters to return a single string of cipher text.
    return ''.join(ciphertext)


# Here's an example
myCoder = buildCoder(shift=17)
text = 'Hello, World!'
ciphertext = applyCoder(plaintext=text, coder=myCoder)
print(ciphertext)

# Input your own plain text and receive the ciphertext!
inpText = input('Input your plaintext: ')
print(applyCoder(inpText,myCoder))
