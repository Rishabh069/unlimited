#learning about dictionary python functions
my_dict = {
    "Name": "Rishi",
    "Age":"16",
    "Address":{
        "Kathmandu"
        "Zip":{
            "Zip1": 44800,
            "Zip2": 44600
        }
    
}
}

my_dict["Age"] = 21
print(my_dict)

# my_dict = {"college": "Islington College"}
my_dict["college"] = "Islington College"
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get("Age"))
print(my_dict["Address"]["Zip"]["Zip1"])

# del my_dict["Age"]
new_age = my_dict.pop("Age")
print(new_age)
print(my_dict)



