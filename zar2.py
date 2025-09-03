
import random

print("--dice--")
prompt = "yes"

while prompt.lower() == "yes": 
    try:
        choice = int(input("How many dice? (1-6): "))
        if 1 <= choice <= 6: 
            dice_results = []
            for _ in range(choice):
                dice_results.append(random.randint(1, 6))
            print(f"You rolled: {dice_results}")
            print(f"Total: {sum(dice_results)}")
        else: 
            print("Please choose between 1-6 dice")
    except ValueError:
        print("Please enter a valid number")
    
    prompt = input("Roll again? (yes/no): ")

print("Thanks for playing!")

# Here is the old version ------------------------------------
# import random

# print "--dice--"
# prompt ="yes"
# while prompt == "yes": 
# 	secim=int(input("for one dice press 1, for two dice press 2: "))
# 	if secim == 1 or secim == 2: 
# 		random_list=[]
# 		for number in range(secim):
# 			random_list.append(random.randint(1,6))
# 		print random_list
# 	else: 
# 		print "wrong choice"
# 	prompt = raw_input("try again?(yes or anything else)") 
# print "thanks for playing!"
