n = int(input())
matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal = 0
for index in range(n):
    diagonal += matrix[index][index]

print(diagonal)
