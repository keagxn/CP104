"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Keagan McKay
ID: 210924090
Email: mcka4090@mylaurier.ca
__updated__ = "2020-09-17"
-------------------------------------------------------
"""
length = float(input("Foundation length (m): "))

width = float(input("Foundation width (m): "))

height = float(input("Foundation height (m): "))

wall = float(input("Wall height (m): "))

cc = float(input("Cost of concrete ($/m^3): "))

bricks = float(input("Cost of bricks ($/m^2): "))

foundation = length * width * height

conc = cc * foundation

ye = wall * length

ah = wall * width

bn = (ye + ah) * 2

cb = bn * bricks

total = conc + cb

print("")

print(f"Concrete needed for foundation (m^3): {foundation:0.2f}")

print(f"Cost of concrete: ${conc:0.2f}")

print(f"Bricks needed for walls (m^2): {bn:0.2f}")

print(f"Cost of bricks: ${cb:0.2f}")

print(f"Total cost: ${total:0.2f}")