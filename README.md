# AES
To run the algorithm simply use: 

`
python3 main.py --keysize $KEYSIZE --keyfile $KEYFILE --inputfile $INPUTFILE --outputfile$OUTFILENAME --mode $MODE
`

## `main.py`
`main.py` takes arguments shown above. 
`--keysize` can vary between 128 and 256 and defines the key length (`Nk`), which can be 4 or 8 bytes respectively.
`Nb`, the block width, does not change.
`Nr`, the number of rounds, is either 10 or 14 respectively.


Based of whether the mode is encrypt or decrypt, the `cipher` or `inv_cipher` functions are called.
If encrypting then the input file is also padded.

## `aes.py`
This file contains a lot of array's that are supposed to make multiplication in GF(2^8) possible.

`sub_bytes` and its inverse counterpart just plug into the `sbox array`.

`transpose` was written because at one point I confused row and column order 
and didn't have enough time ot rewrite the math.

`shift_rows` and the inverse counterpart shift the 0th row by 0, the 1st by 1, and so on - 
all in their respective direction.

`mix_columns` and its inverse counterpart do matrix multiply with some constants.
To make multiplication possible I used the constant array at the head of the file.

`add_round_key` adds the word generated in KeyExpansion
 for the respective round.

 `rot_word` just rotates the bytes in a word
 , and `sub_word` substitutes each byte using the `sbox`.

 `key_expansion` sandwhiches bytes from the byte array input and does what it does. 
 Most of which just involves XOR and plugging into `sub_word`, `rot_word`, and `rcon`

 `cipher` and `inv_cipher` implement all the functions in the correct order as specified by NIST.