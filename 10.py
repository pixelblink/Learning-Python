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

# n=5
# mul,i=1,1
# while i<=n:
#     mul=mul*i
#     if i<n:
#         print(i, end=',')
#     else:
#         print(i, end="=")
#     i=i+1
# print(mul)



# HW
# even 
# 2,4,6,8,10
#  
# 
# 
# 



n=eval(input("enter number"))
td=0
while n>0:
    td=td+1
    n=n//10
print(f'total digits= {td}')