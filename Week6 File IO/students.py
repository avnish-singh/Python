# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"]): # sort students by name; lamda is an anonymous function that takes a student and returns the student's name
#     print(f"{student['name']} is from {student['home']}")


#CSV Library
# import csv
# students = []

# with open('students.csv') as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})


# with open('students.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # students.append({"name": row["name"], "home": row["home"]})
#         students.append(row)

# for student in sorted(students, key=lambda student: student["name"]): # sort students by name; lamda is an anonymous function that takes a student and returns the student's name
#     print(f"{student['name']} is from {student['home']}")

import csv

name=input("Name: ")
home=input("Home: ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home,"name": name },)