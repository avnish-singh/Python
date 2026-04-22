# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_house(student): #sort students by house
    return student["house"]

for student in sorted(students, key=get_house, reverse=False): #
    print(f"{student['name']} is in {student['house']}")