

def search(arr, term): # Using a simple linear search, could be improved later
    for i in range(0, len(arr)):
        if arr[i] == term:
            return i

def parseword(word, file): # Parse a single word
    lines = []
    slines = [] # Split lines
    with open(file, 'r+') as f:
        lines = f.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        sp = lines[i].split(": ")
        if sp[0] == word:
            return sp[1]
    return word # If the word isn't found in the file just return the word

def parsetext(text, file):
    newtext = ""
    for word in text:
        newtext += parseword(word, file)
    return newtext


t = "a b a b b"
print(t)
print("--->")
print(parsetext(t, "dict.txt"))
