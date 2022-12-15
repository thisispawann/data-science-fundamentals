'''
the seek() function sets the position of a file pointer
and the tell() function returns the current position of a
file pointer.
file handle or pointer denotes the position from which the file
contents will be used or written.
to change the file handle position use seek() function.

syntax:
f.seek(offset, whence)

How many points the pointer will move is computed from adding offset to a reference point; the reference point is given by the whence argument.

The allowed values for the whence argument are: –

A whence value of 0 means from the beginning of the file.
A whence value of 1 uses the current file position
A whence value of 2 uses the end of the file as the reference point. 
The default value for the whence is the beginning of the file, which is 0
'''

# opening text file
f = open('text', 'r')

# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)
 
# prints current position
print(f.tell())
 
print(f.readline())
f.close()