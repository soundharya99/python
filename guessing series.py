import random
b=random.randrange(0,20)
a=int(input("enter ur guessing number"))
if(a==b):
  print("the guessed number is matching")
elif(a>b):
    print("high guessing number")
else:
    print("invalid")
    
