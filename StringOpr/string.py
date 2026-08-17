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