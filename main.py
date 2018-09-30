from aes import *

Nb = 4
Nk = 4
Nr = 10

# aes 256
Nk = 8
Nr = 14

inp = None
with open('inputfile', 'rb') as f:
    inp = f.read()
    length = 16 - (len(inp) % 16)
    inp += bytes([length])*length

key = None
with open('keyfile', 'rb') as f:
    key = f.read()
w = [int(x) for x in KeyExpansion(key, Nk, Nb, Nr)]
print(w)


def toByteBlock(y):
    return [x for x in y]

final = []

for x in range():
    part = [hex(x) for x in Cipher(toByteBlock(inp[16*c:16*(c+1)]),w,Nb,Nr)]
    final.append(part)
print([hex(x) for x in Cipher(toByteBlock(inp[0:16]),w,Nb,Nr)])
print([hex(x) for x in Cipher(toByteBlock(inp[16:32]),w,Nb,Nr)])

with open('outputfile', 'rb') as f:
    out = f.read()
    print([hex(x) for x in out])
