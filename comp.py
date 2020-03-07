name=input("Enter your name ")

size=len(name)

if size<3:
    print("Name should be more than 3")
elif size>50:
    print("Name should not be more than 50")
else:
    print("Name looks fine")