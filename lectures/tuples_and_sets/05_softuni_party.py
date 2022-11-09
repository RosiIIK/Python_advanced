lines = int(input())

guest_list = set()
arrived_guests = set()

for i in range(lines):
    guest_list.add(input())

arrival = input()
while not arrival == "END":
    arrived_guests.add(arrival)
    arrival = input()

missing_guests = guest_list.difference(arrived_guests) #this is equal to 'guest_list - arrived_guests'
print(len(missing_guests))

#version 1
for guest in sorted(missing_guests):
    print(guest)

#or version 2
missing_vips = set(guest for guest in missing_guests if guest[0].isdigit())
missing_regulars = missing_guests - missing_vips

for vip in sorted(missing_vips):
    print(vip)
for guest in sorted(missing_regulars):
    print(guest)
