def isAscii(text):
    return all(ord(char) < 128 for char in text)

def dictToList(dict):
    return list(dict.keys())