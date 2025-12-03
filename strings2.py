#vowelcounter
s=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for ch in s:
    if ch in vowels:
        count+=1
print(count)

#reverse string
s="Python"
rev=" "
for ch in s:
    rev=ch+rev
print(rev)

#palindrome
n="madam"
rev=""
for ch in n:
    rev=ch+rev
if n==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")