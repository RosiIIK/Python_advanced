def start_spring(**data):
    springs_dict = {}
    result = []
    for value, key in data.items():
        if key not in springs_dict:
            springs_dict[key] = []

        springs_dict[key].append(value)

    springs_dict = sorted(springs_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for sp_obj, values in springs_dict:
        result.append(f"{sp_obj}:")
        for val in sorted(values):
            result.append(f"-{val}")

    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
