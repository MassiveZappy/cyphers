# 00110 to g
# 10011 to u
# 10110 to y
# 10001 to s
cypher = {
    "a": "00000",
    "b": "00001",
    "c": "00010",
    "d": "00011",
    "e": "00100",
    "f": "00101",
    "g": "00110",
    "h": "00111",
    "i": "01000",
    "j": "01000",
    "k": "01001",
    "l": "01010",
    "m": "01011",
    "n": "01100",
    "o": "01101",
    "p": "01110",
    "q": "01111",
    "r": "10000",
    "s": "10001",
    "t": "10010",
    "u": "10011",
    "v": "10011",
    "w": "10100",
    "x": "10101",
    "y": "10110",
    "z": "10111"
}
# subtract 1 from the value of each letter in the string and return the new string
def encode(str):
    encodedStr = ""
    for char in str:
        try:
            if char == " ":
                pass
            encodedStr += cypher[char.lower()] + " "
        except KeyError:
            print("Invalid character")
            exit()
    return encodedStr[:-1]

def decode(str):
    decodedStr = ""
    for letter in str.split(" "):
        for key in cypher:
            if cypher[key] == letter:
                decodedStr += key
    return decodedStr
# get sting to encode/decode
startingStr = input("Enter a string: ")
# encode/decode string
encodeBool = input("Encode or decode? (e/d): ")
if encodeBool == "e":
    encodedStr = True
elif encodeBool == "d":
    encodedStr = False
else:
    print("Invalid input")
    exit()
if encodedStr:
    print(encode(startingStr))
else:
    print(decode(startingStr))
