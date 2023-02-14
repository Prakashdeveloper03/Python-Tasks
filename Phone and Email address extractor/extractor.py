import re

text = input("Enter the text to search phone number & email address : ")

email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
emails = re.findall(email_pattern, text)

phone_pattern = re.compile(r"\+\d{1,2}-\d{10}")
phones = re.findall(phone_pattern, text)

print(f"Emails : {emails}")
print(f"Phone numbers : {phones}")
