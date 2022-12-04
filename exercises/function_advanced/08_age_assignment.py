def get_name(names, letter):
    for name in names:
        if name.startswith(letter):
            return name

def age_assignment(*names, **kwargs):
    people = {}
    result = ''
    for key, value in kwargs.items():
        name = get_name(names, key)
        people[name] = value

    sorted_people = dict(sorted(people.items(), key=lambda x: x[0]))
    for person in sorted_people.items():
        result += f"{person[0]} is {person[1]} years old." + "\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))
