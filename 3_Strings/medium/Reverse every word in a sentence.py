# Reverse every word in a sentence
a = "This is a beautiful sentence"
result = " ".join(i[::-1] for i in a.split())
print(result)
