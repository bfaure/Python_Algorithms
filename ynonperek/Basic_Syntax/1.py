
'''
write a program that asks the user for an integer and prints
the sum of its digits
'''

val=raw_input("Enter an integer:")
tot=sum([int(e) for e in str(val)])
print "Sum of digits: %d"%tot