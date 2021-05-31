chance=5
ans=8
print("number Guessing Game")
print("Choose a number (between 0-9)")

while (chance>=0):
    inputAnswer=int (input("Enter Your Guess:- "))
    if(inputAnswer<=7):
        chance-=1
        print("Guess a number greater then ",inputAnswer )
    elif(inputAnswer==8):
     print("Congratulations!! You won")
     break

    elif(inputAnswer==9):
        print("Enter a number less than 9")
        chance-=1
    if(chance==0):
        print("You lost....the correct answer is ",ans)
        break
 
