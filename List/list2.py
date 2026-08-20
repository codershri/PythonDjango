fruits=['apple', 'chicken Alfredo', 'orange', 'grape', 'kiwi', 'mango', 'lichi', 'jamun']

newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]

print(newlist)