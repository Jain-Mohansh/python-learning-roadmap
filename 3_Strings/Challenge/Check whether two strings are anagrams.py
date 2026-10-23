# Check whether two strings are anagrams
a = "Dormitory"
b = "Dirty room"

a = a.replace(" ", "").lower()
b = b.replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")
