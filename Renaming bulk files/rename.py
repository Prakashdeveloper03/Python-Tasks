import os

path = "./txts"

for filename in os.listdir(path):
    new_filename = filename.replace("sample", "input")
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
