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
dirt = float(input("Enter amount of dirt (m^3): "))

gravel = float(input("Enter amount of gravel (m^3): "))

sand = float(input("Enter amount of sand (m^3): "))

total = dirt + gravel + sand

print('')
print('Material   Cubic Metres')
print(f'Dirt       {dirt:> 5.1f}')
print(f'Gravel     {gravel:> 5.1f}')
print(f'Sand       {sand:> 5.1f}')
print(f'Total      {total:> 5.1f}')




# print(f"""
# Material   Cubic Metres
# Dirt       {format(dirt, "5.1f")}
# Gravel     {format(gravel, "5.1f")}
# Sand       {format(sand, "5.1f")}
# Total      {format(total, "5.1f")}
# """)
