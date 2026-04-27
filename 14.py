# pattern printing using for loop

# static
# n=5
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()
    


# dynamic 
# n=int(input("enter number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()



# right angle triangle
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()




n=int(input("enter number"))
for i in range(1,n+1):
    ch="A"
    for _ in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()