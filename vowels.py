s=input("enter the string:")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
for char in s:
    if char not in vowels:
        result = result + char

print("\nAfter removing Vowels: ", result)