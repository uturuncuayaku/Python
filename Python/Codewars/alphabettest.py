import re
import string
def alphabet_position(text):
    text = text.lower()
    x = re.findall('\w',text)
    LETTERS = {letter: str(index) for index, letter in enumerate(string.ascii_letters,start=1)}
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ''.join(numbers)

def alphabet_position1(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())