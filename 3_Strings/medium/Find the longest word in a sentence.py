# Find the longest word in a sentence
a = "This is a beautiful sentence"

longest = max(a.split(), key=len)

print(longest)
