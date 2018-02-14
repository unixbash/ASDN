def isAscii(text):
    return all(ord(char) < 128 for char in text)