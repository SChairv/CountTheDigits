#Create a function that counts the number of digits in a number.
# Conversion of the number to a string is not allowed.

def countdigits(x,y,z):
    while x >= 10:
        x = (x//10)
        y = (y+1)
    print("The number of digits in ", z, "is ", y, ".")


y = 1
x = int(input("Please enter a number"))
z = x
countdigits (x,y,z)

y = 1
x = 1234567898765432123456789
z=x
countdigits (x,y,z)

y = 1
x = int(input("Please enter a number"))
z = x
countdigits (x,y,z)