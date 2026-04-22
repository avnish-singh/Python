# # names = []

# # for _ in range(3):
# #     names.append(input("Enter a name: "))

# # for name in sorted(names):
# #     print(f"Hello, {name}!")

# #Now save the values to a file
# name = input("Enter a name: ")

# # file = open("names.txt","a") #w for write, a for append
# with open("names.txt","a") as file: #with statement automatically closes the file after the block is executed
#     file.write(f"{name}\n")
# # file.close() #not needed when using with statement

# with open("names.txt","r") as file:
#     # lines = file.readlines()
#     # for line in lines:
#     #     # print(f"Hello, {line}", end="") #en d="" prevents adding an extra newline character since line already contains one
#     #     print(f"Hello, {line.strip()}!") #strip() removes any leading/trailing whitespace characters, including the newline character
#     for line in file:
#         print(f"Hello, {line.rstrip()}!")

#1
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

#2
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print(f"Hello, {line.rstrip()}!")