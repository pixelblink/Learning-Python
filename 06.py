# Dictionary

# mutable in nature
# collection of "key":"value" pairs
# enclosed with {}
# pairs are separated by comma
# key, value separated by colon :
# key is unique
# value can be duplicate
# indexing is not supported
# slicing is not supported
# homogenious and heterogenious both are supported,keys can be numbers as string



d={
    "name":"person",
    "age":18,
    "city":"bhopal",
}

# print(d)
# print(type(d))
# print(len(d))
# print(max(d))
# print(min(d))



# Dictionary Methods

# # copy() create new object
# d1=d.copy()
# print(d1)
# d1=d.copy()

# # clear() rename all pairs from dictionary
# d1.clear()
# print(d1)
# del(d1)

# # get() dictName.get('key') will return 'value'
# x=d.get("name")
# print(x)

# # keys()
# print(d.keys())

# # values()
# print(d.values())

# # items()
# print(d.items())

# fromkeys() 


# updated()
l={"new":"yes","part":2}
d.update(l)
print(d)

# # d.pop() tho dictionary dont support indexing it can be targetted by key names and delete 
# d.pop('name')
# print(d)

# # d.popitem() to del the last item
# d.popitem()
# print(d)

# setdefault() if the passed key value pair is available in the dictionary then there will be no changes, if absent then key value pair will be created
d.setdefault("name1(key)","yeahh(value)")
print(d)


































# setdefault()
# pop()
# popitem()






