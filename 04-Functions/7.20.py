def nth_prime(n):
    """Zwraca n-tą liczbę pierwszą."""
    count = 0  # Liczba znalezionych liczb pierwszych
    candidate = 1  # Zaczynamy od liczby 1

    while count < n:
        candidate += 1  # Sprawdzamy następną liczbę
        is_prime = True  # Zakładamy, że liczba jest pierwsza

        # Sprawdzamy, czy candidate jest liczbą pierwszą
        if candidate > 1:
            for i in range(2, int(candidate**0.5) + 1):
                if candidate % i == 0:
                    is_prime = False  # Znaleziono dzielnik, więc nie jest pierwsza
                    break

            if is_prime:
                count += 1  # Zwiększamy licznik, jeśli znaleziono liczbę pierwszą

    return candidate

# Przykład użycia:
print(nth_prime(1))  
print(nth_prime(5))  
