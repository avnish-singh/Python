import re

name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ?")
#     name = f"{first} {last}"

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    # last, first = matches.groups()
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")