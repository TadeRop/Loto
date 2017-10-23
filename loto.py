import random

print ("Welcome to the Lottery numbers generator.")
n = int(raw_input("Please enter how many random numbers would you like to have:"))
print random.sample(xrange(1,100), n)

print ("END")