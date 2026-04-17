# Control Statement:-

# Conditional(if, if-else, if-elif and if-elif-else),
# Looping/Iterative(while, while-else, for and for-else) and 
# Transfer(continue, break and pass)


# Conditional Statement

# single condition
# checking if number is even or not

# n=eval(input("enter a number"))
# if n%2==0:
#     print(f'given number is {n} is even')
#     print('hello1')
# else:
#     print('not even')



# multiple condition
# checking if number is even, odd or zero

# n=eval(input("enter a number"))
# if n==0:
#     print(f'given number {n} is zero')

# elif n<0:
#     print(f'given number {n} is negative')

# elif n%2==0:
#     print(f'given number {n} is even')

# elif n%2==1:
#     print(f'given number {n} is odd')



# Looping/Iterative Statement
# while loop


# n=5
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+1


# addition

# n=5
# sum,i=0,1
# while i<=n:
#     sum=sum+i
#     if i<n:
#         print(i, end=',')
#     else:
#         print(i, end="=")
#     i=i+1
# print(sum)


# multiplication, factorial

n=5
mul,i=1,1
while i<=n:
    mul=mul*i
    if i<n:
        print(i, end=',')
    else:
        print(i, end="=")
    i=i+1
print(mul)
