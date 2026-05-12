# methods

s={1,2,3,4,5}

# add() #add single element in random position
s.add(1000)
print(s)
# update() #adds multiple element in random position
tup=(100,200,"yes")
s.update(tup)
print(s)

# remove() #remove element if present and if not present then throws an error
s.remove(100)
print(s)
# discard() #remove element if present and if not present then no error is given
s.discard(1000)
print(s)

# pop() #remove random element

# clear() #clears every elements in the set
# s.clear()
# print(s)

# copy() #


# frozenset() 
fs=frozenset(s)
print(fs)
print(type(fs))
print(id(fs))
print(len(fs))
