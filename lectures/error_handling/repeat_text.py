text = input()

try:
    n = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text * n)
