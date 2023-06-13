import os
import zipfile

alphabets = [chr(i) for i in range(ord("a"), ord("z") + 1)]

for letter in alphabets:
    try:
        file_name = letter + ".txt"
        with open(file_name, "w") as file:
            file.write("This is the letter: " + letter)
            print("Created txt file:", file_name)
    except:
        print("error")
        exit(1)

version = os.environ.get("VERSION")
for letter in alphabets:
    try:
        zip_name = letter + "_" + version + ".zip"
        with zipfile.ZipFile(zip_name, "w") as zip_file:
            txt_file = letter + ".txt"
            zip_file.write(txt_file)
            print("Created zip file:", zip_name)
    except:
        print("Error occured")
        exit(1)

for letter in alphabets:
    file_name = letter + ".txt"
    os.remove(file_name)