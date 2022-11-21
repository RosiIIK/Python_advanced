number_of_usernames = int(input())
usernames = set()

for _ in range(number_of_usernames):
    usernames.add(input())

for username in usernames:
    print(username)
