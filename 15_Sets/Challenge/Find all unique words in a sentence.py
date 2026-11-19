# Find all unique words in a sentence.

sentence = "python is easy and python is powerful"

words = sentence.split()

result = [word for word in set(words) if words.count(word) == 1]

print(result)