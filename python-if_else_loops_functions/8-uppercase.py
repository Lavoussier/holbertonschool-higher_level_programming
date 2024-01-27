#!/usr/bin/python3

def islower(c):
    '''islower returns a boolean
    '''
    return 'a' <= c <= 'z'

def uppercase(s):
    offset = ord('A') - ord('a')
    print(''.join(chr(ord(c) + offset) if 'a' <= c <= 'z' else c for c in s))
