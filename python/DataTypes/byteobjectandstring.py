'''
Strings are sequences of characters. They are human-readable. 
They can't be directly stored on the disk, you have to encode 
them into a machine-readable format that is bytes.
'''
s = 'Hello Namaste'

# Encoding the string into bytes
bytes_obj = s.encode('ASCII')
print(bytes_obj)

# Output:
b'Hello Namaste'

'''
Byte objects are immutable sequences of bytes, that is, integers in the range 0 to 255. 
Bytes can be directly stored on the disk. They are machine-readable, you have to decode 
them into a human-readable format which is a string. If you want it back to its original 
form then you have to decode it.
'''
# Byte Object
bytes_obj = b'Hello Namaste'

# Decoding the bytes into string
s = bytes_obj.decode('ASCII')
print(s)

# Output:
'Hello Namaste'
