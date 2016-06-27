#!/usr/env python
'''
Retrieve hashes for files inside specified directory.
Filename;SHA512 hash
'''

import sys, os, filehashlib

dir = sys.argv[1]

print 'Filename;SHA512 Checksum'
for r, d, f in os.walk(dir, topdown=True):

    for name in f:

        try:

            print '%s;%s' %(os.path.join(r, name), filehashlib.sha512sum(os.path.join(r, name)))

        except OSError:

            continue