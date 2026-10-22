# Find the shortest word in a sentence
a = "This is a beautiful sentence"

longest = min(a.split(), key=len)

print(longest)
