import string

''' --- CAESARIAN CIPHERZ --- '''
''' Plaintext is shifted an int. See "substitution cipher" on wikipedia. '''
''' Author: Kristopher Buote '''

def buildCoders(shift):
    assert shift >=0 and shift <=26
    encoder = dict()
    decoder = dict()
    
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

        # Build the encoder
        encoder[char_lower] = char_lower_shifted
        encoder[char_upper] = char_upper_shifted

        # Build the decoder
        decoder[char_lower_shifted] = char_lower
        decoder[char_upper_shifted] = char_upper

        
    return encoder, decoder



def applyCoder(text, coder):

    # alphabetic characters are ciphered, punctation remains constant
    transformed_text = []

    for char in text:
        if char in coder:
            newChar = coder[char]
            transformed_text.append(newChar)
        else:
            transformed_text.append(char)

    # Return the joined list of characters to return a single string of cipher text.
    return ''.join(transformed_text)


# Here's an example
myEncoder, myDecoder = buildCoders(shift=17)
sample_text = 'Hello, World!'
ciphertext = applyCoder(text=sample_text, coder=myEncoder)
plaintext = applyCoder(text=ciphertext, coder=myDecoder)
print('Ciphertext: {0} \nPlaintext: {1}\n'.format(ciphertext, plaintext))

# Input your own plain text and receive the ciphertext!
inpText = input('Input your plaintext: ')
print('Your ciphertext: ', applyCoder(inpText,myEncoder))
