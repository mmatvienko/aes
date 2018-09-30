from aes import *
import argparse

parser = argparse.ArgumentParser(description='Use AES with ECB.')
parser.add_argument('--keysize', type=int, default=128,
                    help="""Define key size. Pick between
                    128-bit or 256-bit.""")
parser.add_argument('--keyfile', type=str,
                    help="""Location of the file
                    that contains your key.""")
parser.add_argument('--inputfile', type=str,
                    help="""Location of what you want to
                    encrypt. """)
parser.add_argument('--outputfile', type=str,
                    help="""Path of your output""")
parser.add_argument('--mode', type=str,
                    help="""Do you want to encrypt or decrypt""")

args = parser.parse_args()

KEY_SIZE = args.keysize
KEY_FILE = args.keyfile
INPUT_FILE = args.inputfile
OUTPUT_FILE = args.outputfile
MODE = args.mode


# define basic params to be passed into cipher
# bock width doesn't change
Nb = 4
# aes 128
if KEY_SIZE == 128:
    Nk = 4
    Nr = 10
elif KEY_SIZE == 256:
# aes 256
    Nk = 8
    Nr = 14
else:
    exit("Key Size has to be 128 or 256 bits")

inp = None
with open(INPUT_FILE, 'rb') as f:
    inp = f.read()
    # do some padding
    # thx for the code michael <3
    length = 16 - (len(inp) % 16)
    inp += bytes([length])*length

key = None
with open(KEY_FILE, 'rb') as f:
    key = f.read()
# perform key expansion
w = [int(x) for x in KeyExpansion(key, Nk, Nb, Nr)]

final = []
if MODE == 'encrypt':
    for c in range(len(inp)//16):
        for x in Cipher(inp[16*c:16*(c+1)],w,Nb,Nr):
            final.append(x)
elif MODE == 'decrypt':
    # do decrypt stuff
    pass
else:
    exit("modes can either be encrypt of decrypt only")
# just making sure everything is padded
if len(final) % 16 != 0:
    print("length is not a multiple of 16... it should be")

with open(OUTPUT_FILE, "wb") as f:
    f.write(bytes(final))
