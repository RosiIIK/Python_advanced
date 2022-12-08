from collections import deque

def process_destinations(customers, taxi_cars):
    total_time = 0
    while customers and taxi_cars:
        if customers[0] > taxi_cars[-1]:
            taxi_cars.pop()
            continue

        if customers[0] <= taxi_cars[-1]:
            total_time += customers[0]
            customers.popleft()
            taxi_cars.pop()
            if not customers or not taxi_cars:
                return total_time
    return total_time


customers = deque([int(el) for el in input().split(", ")])
taxi_cars = [int(el) for el in input().split(", ")]

total_time = process_destinations(customers, taxi_cars)

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")





#4, 6, 8, 5, 1 - customer
#1, 9, 15, 10, 6 - taxi cars
# 4 + 6 + 8 + 5 + 1 = 24mins
