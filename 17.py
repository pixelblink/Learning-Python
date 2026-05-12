# 2.default positional argument

# def add(x=0,y=0,z=0):
#     print(x+y+z)

# sum()
# sum(5)
# sum(5,5)
# sum(5,5,5)

# 3.variable's length positional argument(*args)
# packing and unpacking# * holds value in the form of tuple, it is used to pack and unpack data into tuple

# syntax
# def fun_name(*args):
#     print(args)
#     print(type(args))

# fun_name(args1)
# fun_name(args)

# example
# def display(*n):
#     print(n)
#     print(type(n))

# display()
# display(10,20)
# display(10,"python",20)





# def display(*n):
#     print(n)
#     print(type(n))

# values=eval(input("enter values"))
# display(*values)




# def add(x,y,z):
#     print("x", x)
#     print("y", y)
#     print("z", z)

# add(z=10,y=20,x=30)

# # these will throw errors(for understanding errors)
# add()
# add(x=10)
# add(x=10,y=20)
# add(x=10,y=20,z=30,p=40)



# 4. default keyword argument

# def add(x=0,y=0,z=0):
#     print("x", x)
#     print("y", y)
#     print("z", z)

# add(z=10,y=20,x=30)
# add()
# add(x=10)
# add(x=10,y=20)
# # this will throw errors(for understanding errors)
# add(x=10,y=20,z=30,p=40)


# 6. variable length keyword argument

# def add(**toPackDictionary): # double * is used for dictionary packing
#     print(toPackDictionary)
#     print(type(toPackDictionary))

# add()
# add(x=10,y=20,z=30)


# d={"x":300,"y":"soldiers","z":200}
# sum=0
# for i in d:
#     sum=sum+d.get(i)
#     sum=sum+d(i)


# for i in d.value():
#     sum=sum+i

