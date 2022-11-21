n = int(input())
intersections = []

for _ in range(n):
    data = input()
    first_data, second_data = data.split('-')
    start_1, stop_1 = [int(el) for el in first_data.split(',')]
    start_2, stop_2 = [int(el) for el in second_data.split(',')]
    intersection = range(max(start_1, start_2), min(stop_1, stop_2)+1)
    intersections.append(intersection)

longest = sorted(intersections, key=lambda x: -len(x))[0] #Обратно по дължина ги реди от макс към мин
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
