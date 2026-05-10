# .   any character except a new line
# *   0 or more repetitions
# +   1 or more repetitions
# ?   0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string
# []    set of characters
# [^]   complementing the set
# \d    decimal digit
# \D    not a decimal digit
# \s    whitespace characters
# \S    not a whitespace character
# \w    word character, as well as numbers and the underscore
# \W    not a word character
# A|B     either A or B
# (...)   a group
# (?:...) non-capturing version
# full expression to validate email
# ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$



# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")


import re

email = input("What's your email? ").strip()

# if re.search(r"^..*@.+\.edu$", email): # (..* and .+* is same)
# if re.search(r"^[^@]+@+[^@]+\.edu$", email): # ([^@] will not allow @ on that position)
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # (..* and .+* is same)
    print("valid")
else:
    print("Invalid")


# Mail Regex 
#^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
