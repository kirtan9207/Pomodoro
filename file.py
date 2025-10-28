file_name =input("enter file name")
try:
    file = open("file name","r")
    data= file.read()
    print(data)
    file.close()
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("permission denied")
except Exception:
    print("some error")
else:
    print(data)      