#You can get the data type of any object by using the type() function:

#x= 100

def addition(num1):
    global x
    x=50
    #print("Protein needed", num1/x*2,"kg")

addition(65)

print("Protein needed", 65/x*2,"kg")
print(type(x))



'''
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''