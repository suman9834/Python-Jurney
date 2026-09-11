name = "suman"  # double quotes ("") can be used for string

age = 20 # number can be integer or float

roll  = 4995599.5995 # point number can be integer or float


#print(name) #printing the name variable


print("my name is:", name)
print("my age is:", age)
print("my roll number is:", roll)


# rules for variable name
# a variable name can only start with a letter or an underscore (_)
# a variable name can only contain letters, numbers, and underscores (_)
# a variable name cannot start with a number
# a variable name cannot contain any special characters like @, $, %, etc.
# a variable name cannot be a reserved keyword in Python like if, else, while, etc.



_suman = "suman" # valid variable name

golu1 = "golu" # valid variable name

golu_1 = "golu" # valid variable name

344suman= "suman" # invalid variable name, cannot start with a number

@suman= "golu1" # invalid variable name, cannot contain special characters

&suman= "golu1" # invalid variable name, cannot contain special characters

golu@1= "golu" # invalid variable name, cannot contain special characters

if = "suman" # invalid variable name, cannot be a reserved keyword in Python

else = "golu" # invalid variable name, cannot be a reserved keyword in Python

# In Python, we can use the type() function to check the data type of a variable. The type() function returns the data type of the variable passed to it as an argument.

print(type(name)) # printing the  type of variable name

print(type(age)) # printing the type of variable age

print(type(roll)) # printing the type of variable roll
