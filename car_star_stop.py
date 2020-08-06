command=" "
started=False
while command.lower()!= "quit":
    command=input("enter command: ")
    if command=="start":
        if started:
            print("car is already started")
        else:
            started=True
            print("car started")
    elif command=="stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
            print("car stopped")
    elif command== "help":
        print("""
start=to start the car
stop=to stop the car
quit=to quit
        """)
    elif command=="quit":
        break
    else:
        print("sorry ,i don't understand the command")
