#getting username from twitter url
import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

#https://twitter.com/avnishsingh