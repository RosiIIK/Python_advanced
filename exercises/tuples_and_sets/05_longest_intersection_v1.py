n = int(input())
intersections = []

for _ in range(n):
    data = input()
    first_data, second_data = data.split('-')
    start, stop = [int(el) for el in first_data.split(',')]
    first_seq = range(start, stop+1)
    start, stop = [int(el) for el in second_data.split(',')]
    second_seq = range(start, stop+1)
    intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0] #Обратно по дължина ги реди от макс към мин
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
