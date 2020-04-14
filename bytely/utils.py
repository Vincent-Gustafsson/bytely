from random import choices
import string

def generate_random_string(size):
    """
    Generates a string of random characters

    Keyword arguments:
    
    size -- The length of the string to be generated
    """
    characters = string.digits + string.ascii_letters
    random_string = ''.join(choices(characters, k=size))
    return random_string
