# Create a vowel-counting function
def count_vowel(a):
    vowel = 'AEIOUaeiou'
    count = 0
    if type(a) == str:
        for i in a:
            if i in vowel:
                count+=1
    return count

print(count_vowel('Mango'))