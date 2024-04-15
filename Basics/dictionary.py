# key-value pairs 
chai_types = {
    "Masala": "Spicy",
    "Ginger": "Zesty",
    "Green": "Mild"
}

# Printing the element in dictionary
print (chai_types["Masala"])
print (chai_types.get ("Ginger"))

# Dictionary is mutable
chai_types["Ginger"] = "Sweet"
print (chai_types)

# Using for loop
print ()
print ("Printing dictionary using for loop...")
for chai in chai_types:
    print (chai, chai_types[chai])


# Printing all the items in the dictionary
print ()
print ("Printing all the items in the dictionary: ")
for key, value in chai_types.items():
    print (key, value)

if "Masala" in chai_types:
    print ("Masala tea is present")
else:
    print ("Masala tea is not present")

# Square numbers in dictionary
print ()
print ("Square numbers in dictionary: ")
sqaured_nums  = {num: num ** 2 for num in range(10)}
print (sqaured_nums)