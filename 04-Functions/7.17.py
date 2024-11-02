def check(palindrome):
    if palindrome == palindrome[::-1]:
        is_true = True
    else:
        is_true = False
    return is_true
sentence = input('Enter sentence: ')
print(check(sentence))

