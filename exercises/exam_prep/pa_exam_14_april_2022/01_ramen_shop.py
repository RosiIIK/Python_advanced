from collections import deque

bows_of_ramen = [int(el) for el in input().split(", ")]
customers = deque([int(el) for el in input().split(", ")])


while bows_of_ramen and customers:
    if bows_of_ramen[-1] == customers[0]:
        bows_of_ramen.pop()
        customers.popleft()
        continue
    elif bows_of_ramen[-1] > customers[0]:
        bows_of_ramen[-1] -= customers[0]
        customers.popleft()
        continue
    elif customers[0] > bows_of_ramen[-1]:
        customers[0] -= bows_of_ramen[-1]
        bows_of_ramen.pop()
        continue

if len(customers) <= 0:
    print("Great job! You served all the customers.")
    if bows_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bows_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")
