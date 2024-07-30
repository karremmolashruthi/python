s=input()
vowel="aeiou"
count=0
for c in s:
    if c in vowel and s.count(c)>1:
        print(c)
        break
        
        
        
