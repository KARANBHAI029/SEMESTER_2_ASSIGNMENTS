#Taking input from user in feet
length_feet=float(input("enter length in feet"))
units = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
conversion_factors = [12, 0.333333, 0.000189394, 304.8, 30.48, 0.3048, 0.0003048]
#Asking user for choice of conversion
print("input 1 for inches\ninput 2 for yards\ninput 3 for miles\ninput 4 for millimeters\ninput 5 for centimeters\ninput 6 for meters\ninput 7 for kilometers\n")
input_1=int(input("enter your choice"))
#printing the output
print(f"{length_feet} is {length_feet*conversion_factors[input_1 -1]} {units[input_1 -1]}")



