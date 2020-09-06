#quick test
print("Pay counter by altoid")
Er = input("Enter Pay: ")
Fr = input("Enter Rate: ")
try:
    sh = float(Er)
    tr = float(Fr)
except:
    print("Please Enter a number stupid")


print("counting....")
Xr = int(Er) * int(Fr)
print("Your Pay:",Xr)