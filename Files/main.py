
'''
# creating a file
f=open('data.txt','w')
f.write('This is some sample data...')
f.close()

# Then open the file and show viewers
'''

'''
# reading from a file
f=open('data.txt','r')
print f.read()
f.close()

# Then run the script and show viewers the output
'''

'''
# appending to a file
f=open('data.txt','a')
f.write('\nAnd this is some more data...')
f.close()

# Then open the file and show viewers
'''

'''
# iterating over each line of a file
f=open('data.txt','r')
for line in f:
	print line.strip() # remove the \n endline
f.close()

# Then show the output in terminal
'''

'''
# printing out each byte of the file
from os.path import getsize
f=open('data.txt','r')
for i in range(getsize('data.txt')):
	f.seek(i)
	print "Byte #%d:\t%s"%(i,f.read(1))
f.close()

# Then show the output in terminal
'''

'''
# overwriting a file
f=open('data.txt','w')
f.write('Out with the old, in with the new.')
f.close()

# Then open the file and show viewers
'''

'''
# checking if a file exists
from os.path import isfile
print "Is data.txt a file?",isfile('data.txt')
print "Is dater.txt a file?",isfile('dater.txt')

# Then show the output in terminal
'''

'''
# viewing the contents of a directory
from os import listdir
print "Elements of current directory:",listdir('.')

# Then show the output in terminal
'''



