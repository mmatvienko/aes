from aes import *

Nb = 4
Nk = 4
Nr = 10

inp = None
with open('input', 'rb') as f:
    inp = f.read()

key = None
with open('key', 'rb') as f:
    key = f.read()

w = [hex(x) for x in KeyExpansion(key, Nk, Nb, Nr)]

def toByteBlock(x):
    return [hex(x) for x in inp]

print(Cipher(toByteBlock(inp),w,Nb,Nr))
# input is strig for some reason in AddRoundKey. fix that
