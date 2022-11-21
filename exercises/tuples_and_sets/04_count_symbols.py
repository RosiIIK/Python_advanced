text = input()
symbols = {}

for char in text:
    symbols[char] = text.count(char)

sorted_data = sorted(symbols.items(), key=lambda x: x[0]) #sorting dict by key - return tuples

for el in sorted_data:
    print(f"{el[0]}: {el[1]} time/s")
