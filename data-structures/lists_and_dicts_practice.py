# Lists & Dicts practice

people = [
    {"name": "Ali", "age": 23},
    {"name": "Max", "age": 30},
]

# print all names
for p in people:
    print(p["name"])

# build a dict: name -> age
name_to_age = {p["name"]: p["age"] for p in people}
print(name_to_age)
