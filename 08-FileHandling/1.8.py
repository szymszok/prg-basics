with open('pets.txt', 'r') as file:
    content = file.read()
    lines = content.split()
    sum = len(lines)
    print(sum)
    