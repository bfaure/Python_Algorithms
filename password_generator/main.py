
from urllib2 import urlopen
from random import choice,randint
from passwordmeter import test
from os.path import isfile

if not isfile('words.txt'):
	print 'Downloading words.txt...'
	url='https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
	words_file=open('words.txt','w')
	words_file.write(urlopen(url).read())

words=open('words.txt','r').read().split("\n")
special_chars=['!','?']

def create_password(num_words=2,num_numbers=4,num_special=1):
	pass_str=''
	for _ in xrange(num_words):
		pass_str+=choice(words).lower().capitalize()
	for _ in xrange(num_numbers):
		pass_str+=str(randint(0,9))
	for _ in xrange(num_special):
		pass_str+=choice(special_chars)
	return pass_str

def main():
	pass_str=create_password()
	strength,_=test(pass_str)

	print '\nPassword: %s'%pass_str
	print 'Strength: %0.5f'%strength

if __name__ == '__main__':
	main()