#!/usr/env python
'''
Retrieve metadata for file inside specified directory.
Modified Date, Modified Time, Access Date, Access Time
Creation Date, Creation Time, Permissions, File Name
Access Date;Access Time;Modify Date;Modify Time;Create Date;Create Time;Permissions;User ID;Group ID;File Size;Filename
'''

import os, time, sys

dir = sys.argv[1]

'''
Convert time to MySQL datetime format.
Takes epoch time as input.
'''
def convert_time(t):

    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(t))

print 'Access Time;Modify Time;Create Time;Permissions;User ID;Group ID;File Size;File'

'''
Traverse filesystem in a topdown fashion.
Returns list of the following:
r: root directory
d: directory
f: file
'''
for r, d, f in os.walk(dir, topdown=True):

    for name in f:   #Retrieve file name from list of files

        try:

            perm, inode, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(os.path.join(r, name))
            print '%s;%s;%s;%s;%d;%d;%d;%s' %(str(convert_time(atime)),str(convert_time(mtime)),\
            str(convert_time(ctime)),oct(perm)[-3:],uid,gid,size,os.path.join(r, name))

        except OSError:

            continue

    for name in d:      #Retrieve directory name from list of directories

        try:

            perm, inode, dev, nlink, uid, gid, size, atime, mtime, ctime = os.stat(os.path.join(r, name))
            print '%s;%s;%s;%s;%d;%d;%d;%s' %(str(convert_time(atime)),str(convert_time(mtime)),\
            str(convert_time(ctime)),oct(perm)[-3:],uid,gid,size,os.path.join(r, name))

        except OSError:

            continue
