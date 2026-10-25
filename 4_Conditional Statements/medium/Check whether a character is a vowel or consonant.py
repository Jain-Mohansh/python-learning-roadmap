# Check whether a character is a vowel or consonant
a = input('Enter the character : ')
vowel = 'aeiouAEIOU'
if a in vowel:
    print(f'{a} is a vowel.')
if a.isalpha():
    print(f'{a} is a consonant')
else:
    print(f'{a} is nethier vowel nor consonant')