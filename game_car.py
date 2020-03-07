command=""
started=False
while True:
    command=input(" >").upper()
    if(command=="HELP"):
        print('''
start--->To start the car
stop---->To stop the car
quit---->To end the game
            ''')
    elif(command=="START"):
        if(started):
            print("Car already started")
        else:
            print("Car is started")
            started=True
    elif(command=="STOP"):
        if(not started):
            print("Car is already stopped")
        else:
            print("Car is stopped")
            started=False
    elif(command=="QUIT"):
        break
    else:
        print("I dont understand that...")