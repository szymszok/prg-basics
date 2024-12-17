sentence = 'I completely agree with you'

sentence_splited = sentence.split()

result = list(map(lambda x: len(x),sentence_splited ))

print(result)
