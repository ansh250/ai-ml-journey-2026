# Guess the Number
'''
import random
target = random.randint(1,1000)
while True:
    user_input = input("Guess the number or Quit(Q) : ")
    if(user_input == "Q"):
        break
    user_input = int(user_input)
    if(user_input == target):
        print("Successfully guessed the number")
        break
    else:
        if(user_input>target):
            print("Your number is too greater guess the smaller number")
        else:
            print("Your number is too smaller guess the greater number")
    
print("-----------Game Over ----------------")
'''
# Random Password Generator
import random
import string
char_value = string.ascii_letters+string.digits+string.punctuation
pass_len = 12
password = ""
for i in range(pass_len):
    password+=random.choice(char_value)
print("Your random password is : ",password)