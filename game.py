import random
print("rules for winning paper vs rock =paper,rock vs scissor = rock, paper vs scissor =scissor")
while True:
 choice=int(input("user choice"))
while (choice >3 or choice<1):
 choice= int(input("enter valid data"))
if(choice == 1):  
    choice_name="rock"
elif(choice == 2):
   choice_name="paper"
else:
  choice_name="scissor"
print("user choice is"+choice_name)
print("computer choice")
comp_choice=random.randrange(1,3)
while(comp_choice == choice):
 if (comp_choice ==1):
  comp_name="rock"
 elif(comp_choice== 2):
  comp_name="paper"
 else:
  comp_name="scissor"
 if(choice ==1 and comp_choice==2) and (choice == 2 and comp_choice == 1):
  print ("paper wins")
  result="paper"
 elif(choice ==1 and comp_choice==3) and (choice == 3 and comp_choice == 1):
  print ("rock wins")
  result="paper"
 else:
  print("scissor wins")
  result="scissor"
  if(result ==choice_name):
   print ("user wins")
  else:
   print("comp wins")
   ans=str(input("enter yes or no to play"))
   if (ans=="n"):
    break
                                        
