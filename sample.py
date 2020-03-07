weight=input("Enter your weight: ")

is_kg_lb=input("Enter KG as K or LB as L: ")

if is_kg_lb == 'k' or is_kg_lb == 'K':# if is_kg_lb.upper()=='K':
    print(int(weight)*2.2)
else:
    print(int(weight)/2.2)
