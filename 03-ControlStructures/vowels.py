###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
count = 0
# Count vowels in the text
while count < len(text):
    if text[count] in vowels:
        vowel_count += 1
    count += 1

print(f"The number of vowels in the text is: {vowel_count}")
