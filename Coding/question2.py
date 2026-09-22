s=input("Enter String:")

l=0
chars=set()
longest=""

for i in range(len(s)):
    while s[i] in chars:
        chars.remove(s[l])
        l+=1
    
    chars.add(s[i])
    
    if i-l+1>len(longest):
        longest=s[l:i+1]
        
print(longest)