import os
import zipfile

folder_name, zip_name = "txts", "txts.zip"
zip_obj = zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED)

for foldername, subfolders, filenames in os.walk(folder_name):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        zip_obj.write(file_path, os.path.relpath(file_path, folder_name))
zip_obj.close()
