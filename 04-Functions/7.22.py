def f(name):
    acronym = "" 
    in_word = False  # Flaga wskazująca, czy jesteśmy w słowie

    for char in name:  # Iterujemy przez każdy znak w tekście
        if char != ' ':  # Jeśli znak nie jest spacją
            if not in_word:  # Jeśli nie byliśmy w słowie
                acronym += char  # Dodajemy pierwszą literę słowa
                in_word = True  # Ustawiamy flagę, że jesteśmy w słowie
        else:
            in_word = False  # Resetujemy flagę, gdy napotkamy spację

    return acronym  # Zwracamy akronim

# Przykład użycia:
print(f("National Aeronautics and Space Administration"))  # Wypisze: NASA
print(f("As Soon As Possible"))  # Wypisze: ASAP
print(f("For Your Information"))  # Wypisze: FYI
print(f("Hello World"))  # Wypisze: HW