conversions=[
   lambda t:t*1000,  # tonnes to kilograms
   lambda kilo:kilo*1000,     # kilograms to grams
   lambda gram:gram*1000,      # grams to milligrams
   lambda mili:mili*0.00000220462  # milligrams to pounds

]

tonns=float(input("enter weight in tonns:"))

kg = conversions[0](tonns)
gm = conversions[1](kg)
mg = conversions[2](gm)
lb = conversions[3](mg)


print("Kilograms:", kg)
print("Grams:", gm)
print("Milligrams:", mg)
print("Pounds:", lb)

