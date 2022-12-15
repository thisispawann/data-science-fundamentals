'''
files are named locations on disk to store related information.
they are used to permanently store data in a hard disk.
- we want to read from or write to a file, we need to open it first.

Hence, in Python, a file operation takes place in the following order:
1. Open a file
2. Read or write
3. Close the file
'''

f = open('data.txt', 'r')
print(f) # gives TextIOWrapper, name, mode

# to fetch data
print(f.read())

#write data and print data

f1 = open('text', 'w')
print(f1)

f1.write('New text is generated')

#append
f1 = open('text', 'a')
f1.write(' by file handling append')


#for loop
for data in f:
    print(data)


# image

i = open('fern.jpg', 'rb') #read binary
i1 = open('fern-fern.jpg', 'wb') #write binary

for row in i:
    i1.write(row)