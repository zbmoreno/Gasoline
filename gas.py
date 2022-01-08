# Gasoline

gallons_gas = input("Enter gallons of Gassoline: ")

gallons_gas = float(gallons_gas)

print("Gallons: ", gallons_gas)

#liters
gas_liters = gallons_gas * 3.7854
print("Liters equivalent: ", gas_liters)

#barrel of oil
oil_barrels = gallons_gas / 19.5
print("requires: ", oil_barrels)

#CO2 produced
CO2_produced = gallons_gas * 20
print("CO2 produced: ", CO2_produced)

#ethanol
ethanol = (gallons_gas * 115000) / 75700
print("ethanol: ", ethanol)

#U.S dollar

dollar = gallons_gas * 4.00
print("dollar: ", dollar) 
