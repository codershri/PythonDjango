fruits=['apple', 'chicken Alfredo', 'orange', 'grape', 'kiwi', 'mango', 'lichi', 'jamun']



def forloopwithLettermatch():
    newlist = []
    for x in fruits:
        if "a" in x:
          newlist.append(x)

    print(newlist)

    newlist = [x for x in fruits if "a" in x]

    print(newlist)
forloopwithLettermatch()

def sortingListAlphnumerically():
    fruits.sort()
    print("Acending order-->",fruits)
    fruits.sort(reverse=True)
    print("Decending order-->",fruits)
sortingListAlphnumerically()

def copylist():
    thislist = fruits.copy()
    print(thislist)
copylist()

def copylist2():
    thislist = fruits[:]
    print(thislist)
copylist2()

def copylist3():
    thislist = list(fruits)
    print(thislist)
copylist3()