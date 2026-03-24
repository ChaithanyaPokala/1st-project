with open("C:\\Automation\\python\\filehandling\\file1.txt","r") as file:
    readfile=file.read()
    file.close()
    print(readfile)