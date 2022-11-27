from collections import deque

queue = deque()
total_food = int(input())
orders= input().split()

for num in orders:
    queue.append(int(num))

print(max(queue))

for ordered_food in orders:
    if int(ordered_food) <= total_food:
        queue.popleft()
        total_food -= int(ordered_food)
    else:
        str_queue = [str(x) for x in queue]
        print(f"Orders left: {' '.join(str_queue)}")
        exit()

print("Orders complete")
