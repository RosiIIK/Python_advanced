rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(nums)

print(matrix)

#2nd option:
#print([[int(el) for el in input().split(", ") if int(el) % 2 == 0] for _ in range(int(input()))])
