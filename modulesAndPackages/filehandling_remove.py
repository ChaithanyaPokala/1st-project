import os
file=("C:\\Automation\\python\\filehandling\\file1.txt")
if os.path.exists(file):
    os.remove(file)
else:
    print("File doesn't exist")
