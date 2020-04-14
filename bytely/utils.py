from random import choices
import string

def generate_random_string(size):
    characters = string.digits + string.ascii_letters
    random_string = ''.join(choices(characters, k=size))
    return random_string
