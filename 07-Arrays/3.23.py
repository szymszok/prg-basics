import MyText
text = 'An apple a day keeps the doctor away'
print(f'Text: {text}')
print(f'Number of words: {MyText.length(text)}')
print(f'Words from the longest: {MyText.ordered(text)}')
print(f'Word ordered alphabetically: {MyText.alpha(text)}')