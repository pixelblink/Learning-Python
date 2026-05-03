# transfer statement

# Continue statement -> Skip current iteration 
# Example:
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
#     i=i+1

# Break statement -> Terminate current loop
# Example:
# for i in range(5):
#     if i == 2:
#         break
#     print(i)
#     i=i+1

# Pass Statement -> Skip current block
# Example:

# for i in range(5):
#     if i == 2:
#         pass
#     print(i)
#     i=i+1



# Dynamic Calculator in Pythonnnn 



while True:
    print("1.ADDITION \n 2.SUBSTRCTION \n 3.MULTIPLE \n 4.DIVISION \n 5.OFF \n")
    n=int(input("Enter above mention any option:"))
    if n==1 or n==2 or n==3 or n==4 or n==5:
        numm=[1,2,3,4,5]
    if n in numm:
        if n==1:
            x=int(input("Enter how many no you want to add"))
            sum=0
            for i in range(1,x+1):
                number=int(input(f'enter {i} number:'))
                sum=sum+number
            print("Addition Answer is:",sum)

        if n==2:
            x=int(input("Enter how many no you want to subtract"))
            sub=int(input("enter 1 number:"))
            for i in range(2,x+1):
                number=int(input(f'enter {i} number:'))
                sub=sub-number
            print("Subtraction Answer is:",sub)

        if n==3:
            x=int(input("Enter how many no you want to multiply"))
            mul=1
            for i in range(1,x+1):
                number=int(input(f'enter {i} number:'))
                mul=mul*number
            print("Multiplication Answer is:",mul)

    else:
        print("Plz enter valid option")