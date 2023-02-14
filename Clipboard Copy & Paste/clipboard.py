from pyperclip import copy, paste

lines = paste().split("\n")  # paste the recently copied text from the clipboard
for i in range(len(lines)):
    lines[i] = f"* {lines[i]}"
copy("\n".join(lines))  # copy the modified text to the clipboard
