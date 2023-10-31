#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet == ord('q') or alphabet == ord('e'):
        continue
    print('{:c}'.format(alphabet), end='')
