sentence = input("Enter sentence: ")

vowel = 0
consonant = 0

for char in sentence:
    if char in "aeiouAEIOU":
        vowel += 1
    elif char.isalpha():
        consonant += 1

print("Vowels:", vowel)
print("Consonants:", consonant)


unique_characters = set()

for char in sentence:
    if char != " ":
        unique_characters.add(char)

print("Unique characters:", unique_characters)
print("Number of unique characters:", len(unique_characters))


frequency = {}

for char in sentence:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("\nCharacters occurring more than once:")

for char in frequency:
    if frequency[char] > 1:
        print(char, ":", frequency[char])


reversed_text = ""
index = 0

while index < len(sentence):
    reversed_text = sentence[index] + reversed_text
    index += 1

print("\nReversed sentence:", reversed_text)


print("First five characters:", sentence[:5])
print("Last five characters:", sentence[-5:])