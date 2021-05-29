chance=5
ans=8
print("number Guessing Game")
print("Choose a number (between 0-9)")


# if(inputAnswer==ans):
#     print("Congratulations!! You won")
# elif(inputAnswer<=3):
#     print("Your guess is too low...choose a number greater than 5")
#     wrong+=1
# elif (inputAnswer>5 | inputAnswer<=7):
#      print("Your guess is too low...choose a number greater than 7") 
#      wrong+=1
# elif(inputAnswer==9):
#      print("Your guess is too high...choose a number less than 9")
#      wrong+=1
# if(wrong==3):
#     print("You Lost....The number is ",ans)

while (chance>=0):
    inputAnswer=int (input("Enter Your Guess:- "))
    if(inputAnswer!=ans):
        chance-=1
        print("Guess a number greater then ",inputAnswer )
    elif(inputAnswer==8):
     print("Congratulations!! You won")    
    if(chance==0):
        print("You lost....the correct answer is ",ans)
 