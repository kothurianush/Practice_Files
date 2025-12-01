#Strings
#1.Indexing
b="hello, world!"
print(len(b))
print(b[7])
print(b[0],b[12])
#slicing
print(b[0:5])
print(b[:3])
print(b[6:])
print(b[0:13])
#negative indexing
print(b[-5:-1])
print(b[-3:])
#slicing by "step value"
s = "abcdefghij"
print(s[0:10:2])
print(s[::3])
#string reverse by step value
print(s[::-1])
#emptystring
print(s[5:2])
print(s[1:1])
#upper and lower
a=" Hey, Boomer! "
print(a.lower())
print(a.upper())
print(a.strip())
print(a.replace('H','B'))
print(a.split(","))
#concatination
a="Hey"
b="Siri!"
c=a+b
print(c)
#for gap purpose use " "
d=a+" "+b
print(d)