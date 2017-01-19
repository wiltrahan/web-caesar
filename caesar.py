
def alphabet_position(letter):
    return ord(letter)

def rotate_character(char, rot):

    if char.isalpha():
        rotate = alphabet_position(char)
    else:
        return char

    if rotate >= 97 and rotate <= 122: #for lower case
        cipher = chr(((rotate - 97 + rot) % 26) + 97)
        return cipher
    elif rotate >= 65 and rotate <= 90: # for upper case
        cipher = chr(((rotate - 65 + rot) % 26) + 65)
        return cipher.upper()


def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        elif char.isalpha() == False:
            encrypted = encrypted + char
        else:
            encrypted = encrypted + rotate_character(char, int(rot))

    return encrypted
