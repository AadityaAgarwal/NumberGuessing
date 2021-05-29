chance=5
ans=8
print("number Guessing Game")
print("Choose a number (between 0-9)")

while (chance>=0):
    inputAnswer=int (input("Enter Your Guess:- "))
    if(inputAnswer!=ans):
        chance-=1
        print("Guess a number greater then ",inputAnswer )
    elif(inputAnswer==8):
     print("Congratulations!! You won")    
    if(chance==0):
        print("You lost....the correct answer is ",ans)
 
