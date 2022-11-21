number_n, number_m = map(int, tuple(input().split()))

set_1, set_2 = set(), set()

for _ in range(number_n):
    set_1.add(int(input()))

for _ in range(number_m):
    set_2.add(int(input()))

for element in set_1 & set_2:
    print(element)
