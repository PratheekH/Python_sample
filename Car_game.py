s1=input(">").upper()
print('''
start--->To start the car
stop---->To stop the car
quit---->To end the game
    ''')
is_start=True
while(is_start):

    no_quit=True
    while(no_quit):
        usr_in = input(">").upper()
        if (usr_in == "START"):
            print("Car started")
            break
        elif (usr_in == "STOP"):
            print("Car stopped")
            break
        elif(usr_in == "QUIT"):
            print("Now u have quit the game")
            no_quit = False
            is_start= False
            break
        else:
            print("I dont understand u r cmd")






