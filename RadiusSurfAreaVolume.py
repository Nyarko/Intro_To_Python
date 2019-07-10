import math

radius = int(input("Input the radius: "))

def surface():
    ans = radius**2 *math.pi * 4
    return ans

def volume():
    vol = radius**3 *math.pi*4/3
    return vol

print ("The surface area is: ", surface())
print ("The volume is: ", volume())
