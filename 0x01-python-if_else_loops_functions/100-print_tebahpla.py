#!/usr/bin/python3
for lowercase in range(ord('z'), ord('a') - 1, -1):
    if lowercase % 2 == 0:
        uppercase = 0
    else:
        uppercase = 32
    print('{}'.format(chr(lowercase - uppercase)), end='')
