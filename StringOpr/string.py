string1="""Hi my name is shrirang. 
this is sample string"""
print(string1)

def stringAreArrays():
    print(string1[14::1])
stringAreArrays()

def stringForLoop():
    for x in string1:
        print(x,end=" ")
    for x in string1:
            print(x)
stringForLoop()

def stringLength():
    print(len(string1))
stringLength()

def stringwordCheck():
    print("shrirang" in string1)
    if "this" in string1:
        print("True")
    if "hello" not in string1:
        print("true")
stringwordCheck()

def stringSlice():
    print(string1[6:10])
    print(string1[:10])
    print(string1[2:])
    print(string1[-3:-1])
stringSlice()

def stringModify():
    print(string1.upper())
    print(string1.capitalize())
    print(string1.lower())
    print(string1.lower())
    print(string1.strip())
    print(string1.casefold())
    #print(string1.replace("H","J"))
    print(string1.split())
    #print(string1.center())
stringModify()

def stringconcatinate():
    string2="dumbo"
    print(string1+string2)
stringconcatinate()
