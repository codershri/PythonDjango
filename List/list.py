mylist=["apple","banana","orange","grape"]
mylist2=[1,2,3,4,5,6,7,8,9,0]
mylist3=[True,False,True]
def Listfun():
    print(mylist)
Listfun()

def FindLength():
    print(len(mylist))
FindLength()

def DataTypeOfList():
    print(type(mylist))
    print(type(mylist2))
    print(type(mylist3))
    global list4 
    list4 = list(("x","y","z"))
    print(type(list4))
DataTypeOfList()
