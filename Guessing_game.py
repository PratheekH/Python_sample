guess=9;
i=1;

#while(i<=3):
#    num = int(input("Guess: "))
#    if(num==guess):
#        print("you win!!")
#        exit()
#    else:
#        i+=1
#print("Sorry u failed!")

while(i<=3):
    num = int(input("Guess: "))
    i+=1
    if (num == guess):
        print("you win!!")
        break
else:
    print("Sorry u failed!")

