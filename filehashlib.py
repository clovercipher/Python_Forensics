'''
Module for calculating file hashes in a memory efficient method.
Maps a portion of the file content instead of the entire file.
'''

import hashlib, sys

def md5sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create md5 hashlib object
            hash = hashlib.md5()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()

def sha1sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create sha1 hashlib object
            hash = hashlib.sha1()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()

def sha224sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create md5 hashlib object
            hash = hashlib.sha224()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()

def sha256sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create sha256 hashlib object
            hash = hashlib.sha256()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()

def sha384sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create sha384 hashlib object
            hash = hashlib.sha384()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()

def sha512sum(f):

    try:

        with open(f, 'rb') as handle:
            #Create md5 hashlib object
            hash = hashlib.sha512()
            #While handle still has more content
            while True:
                #Read 4096 bytes of file
                content = handle.read(4096)
                #If no additional content exists, kill loop
                if not content:

                    break
                #Update hash object with new content
                hash.update(content)

    except IOError:
        sys.stdout.write("Please give a valid file as input.\n")
        sys.exit()

    return hash.hexdigest()