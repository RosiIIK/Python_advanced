size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(el)for el in input().split()])

while True:
    line = input()
    if line == "END":
        break

    command_args = line.split()
    command = command_args[0]
    row, col, value = [int(el) for el in command_args[1:]]
    if row < 0 or col < 0 or row >= size or col >= size: #проверява дали елемента е в матрицата или не
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row in matrix:
    print(*row, sep=' ')
