#  SET

# collection of  unique celements
# enclosed with {} and elements separated with a comma "," 
# unordered collection
# indexing not supported
# slicing not supported
# mutable in nature

# s={1,2,"yeahh",3,4,5,"yeahh","no","gud","morning"}
# s1={1,2,35,"yeahh","gud","morning"}
# print(s)
# print(type(s))
# print(len(s))
# # print(max(s)) #error
# # print(min(s)) #error
# print(id(s))
# # print(sum(s)) #error



# set methods


s={1,2,3,4,5}
s1={4,5,6,7,8}
s2={7,8,9,10,11}

print(s.union(s1))
print(s.union(s1.union(s2)))

print(s.intersection(s1))
print(s.difference(s1))
print(s.symmetric_difference(s1))

