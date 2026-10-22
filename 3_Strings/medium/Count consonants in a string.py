# Count consonants in a string
a = 'Hello, World!'
vowel = 'aeiou'
count = 0

for i in a:
    if i not in vowel:
        count+=1
print(count)