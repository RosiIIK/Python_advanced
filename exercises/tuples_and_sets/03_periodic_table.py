number_n = int(input())
chemical_compounds = set()

for _ in range(number_n):
    elements = input().split()
    for element in elements:
        chemical_compounds.add(element)

for element in chemical_compounds:
    print(element)
