
class_names = [	"jack","bob","mary","jeff","ann","pierre",
				"martha","clause","pablo","susan","gustav"]

def create_dataset():
	import random
	num_entries = 50000000 # 50 million lines
	f = open("data.txt","w") 
	for i in range(num_entries):
		current = random.choice(class_names)
		f.write(current+"\n")
	f.close()

def read_dataset_list():
	class_counts = []
	for c in class_names:
		class_counts.append(0)
	f = open("data.txt","r")
	for line in f:
		idx = class_names.index(line)
		class_counts[idx]+=1
	print class_counts 

def read_dataset_dict():
	class_counts = {}
	for c in class_names:
		class_counts[c]=0
	f = open("data.txt","r")
	for line in f:
		class_counts[line]+=1
	print class_counts

import time 

start = time.time()
create_dataset()
print "Dataset creation took %0.1f seconds" % time.time()-start 






