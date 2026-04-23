# for loop


# jumping a single character one step

# s=eval(input("data"))
# x=ord(s)
# print(x)
# y=x+1
# print(y)
# print(chr(y))
# # OR
# print(chr(ord(input("enter a character"))+1))





# jumping a single character one step

s="abc"
s1=''
for ch in s:
    s1=s1+chr(ord(ch)+1)
print(s1)