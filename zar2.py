
import random

print "--dice--"
prompt ="yes"
while prompt == "yes": 
	secim=int(input("for one dice press 1, for two dice press 2: "))
	if secim == 1 or secim == 2: 
		random_list=[]
		for number in range(secim):
			random_list.append(random.randint(1,6))
		print random_list
	else: 
		print "wrong choice"
	prompt = raw_input("try again?(yes or anything else)") 
print "thanks for playing!"
