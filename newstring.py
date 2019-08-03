def new_string(string):
    if string.startswith("is"):
        return string
    else:
        return "is"+string







string=input("enter the string:")
print(new_string(string))
