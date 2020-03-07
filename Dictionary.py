customer= {
    "name" : "Pratheek",
    "age"  : 26,
    "Email" : "pratheekharalike993@gmail.com"
}

customer["name"] = "Pratheek Haralike"

customer["Place"]= "Puttur"

print(customer["name"])
print(customer.get("Email"))

print(customer.get("birthdate","31st May 1993"))

print(customer.get("Place"))


