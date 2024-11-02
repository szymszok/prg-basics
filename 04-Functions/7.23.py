def f(password):
    if len(password) < 6:
        return False
    for char in password:
        if password.count(char) > 1:
            return False

print(f('ax15'))
print(f('book123'))
print(f('a2watser3'))
print(f('123455dfgdfg'))