RED = "red"
BLUE = "blue"
YELLOW = "yellow"

Primary_Colour = ("red,blue,yellow")

colour1=input("Please enter colour 1 ")
colour2=input("Please enter colour 2 ")

if (colour1 == "red" or "blue" or "yellow"):
    print()
else:
    print("Invalid Colour1")

if (colour2 == "red" or "blue" or "yellow"):
    print()
else:
    print("Invalid Colour2")

if (colour1 == colour2):
    print("Error: The two colours you entered are the same")

if (colour1 == "red" and colour2 == "blue"):
    print("the secondary colour is purple")

if (colour1 == "red" and colour2 == "yellow"):
    print("the secondary colour is orange")

if (colour1 == "blue" and colour2 == "red"):
    print("the secondary colour is purple")

if (colour1 == "blue" and colour2 == "yellow"):
    print("the secondary colour is green")

if (colour1 == "yellow" and colour2 == "red"):
    print("the secondary colour is orange")

if (colour1 == "yellow" and colour2 == "blue"):
    print("the secondary colour is purple")