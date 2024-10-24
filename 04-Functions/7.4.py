def many_letters(text):
    count = 0
    for char in text:
        if char == 'e':
            count += 1
    
    return count



sentence = input('Enter text here: ')
print(f'The number of letter "e": {many_letters(sentence)}')