

subTable = [
            ['a','5','4','3','2','1'],
            ['6','b','w','x','y','z'],
            ['7','v','c','o','n','m'],
            ['8','u','p','d','k','l'],
            ['9','t','q','j','e','g'],
            ['0','s','r','i','h','f']
            ]

key = 'ADFGVX'

string = 'I LOVE YOU YOU LOVE ME'.replace(' ','').lower()

def findIndex(char, subTable):

    index = [0,0]

    for i,line in enumerate(subTable):
        for j,e in enumerate(line):
            if e == char:
                index[0] = i
                index[1] = j

    return index

def midCipherText(string):

    cipherText = ""

    for char in string:

        index = findIndex(char,subTable)
        encryptedChar = key[index[0]] + key[index[1]]
        cipherText += encryptedChar

    return cipherText

