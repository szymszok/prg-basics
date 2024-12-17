# takes two numbers from keyboard
n1 = int(input('Podaj pierwsza liczbę: '))
n2 = int(input('Podaj drugą liczbę:  '))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean is {result}")