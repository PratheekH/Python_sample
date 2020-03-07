name=input("What is your name ")
print("Hi " +name +" Welcome to KMC")
age=input("What is your age ")
is_newpatient=input("New or Old ")
is_true=bool(is_newpatient);
print(type(is_newpatient))
if(is_true):
        print("Admitted to A")
else:
        print("Admitted to B")
