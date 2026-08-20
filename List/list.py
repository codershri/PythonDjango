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

def ChangeInList():
    mylist[1]=["chicken Alfredo"]
    print(mylist)
ChangeInList()

def changeRangeOfItem():
    mylist2[1:5]=[11,12]
    print(mylist2)
changeRangeOfItem()

def InsertItem():
    mylist3[2]=[False]
    print(mylist3)
    mylist.insert(6,"kiwi")
    print(mylist)
InsertItem()

def appendItems():
    mylist2.append(100)
    print(mylist2)

    list2=["mango","lichi","jamun"]
    mylist.extend(list2)
    print(mylist)
appendItems()

def addIterable_tuple_set_dic():
    thistuple=(1010,2020,3030)
    mylist2.extend(thistuple)
    print(mylist2)
addIterable_tuple_set_dic()

def removeDelete():
    mylist.remove("grape")
    print(mylist)
    mylist2.pop(3)
    del mylist3[0]
    print(mylist2)
    print(mylist3)

removeDelete()