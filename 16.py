# FUNCTIONS

# required
# def, functionName()

# optional
# parameters, arguments, return

# def add():
#     print(":addition is:",6+7)
    
# add()

# print(add()) # returns none because functions return none to terminate the function


# without argument with return
def add():
    return(":addition is:",6+7)

print(add())


# without argument without return
def sub():
    print(":subtraction is:",6-7)
    
sub()


# with argument with return
def mul(a,b):
    return(":multiplication is:",a*b) 

print(mul(6,7))


# with argument without return
def div(a,b):
    print(":division is:",a/b)

div(6,7)
