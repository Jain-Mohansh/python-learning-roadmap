# Count vowels in a string
a = "hello world"

count = 0
for ch in a:
    if ch in "aeiou":
        count += 1

print(count)
