fillings = [508,500,512,499,492,511,503,476,501,509,508,500,512,487,250]

    
filtr = lambda x: 500 - 500 * 0.02 < x < 500 + 500 * 0.02
filtered = list(filter(filtr, fillings))
incorrect = (len(fillings) - len(filtered)) * 10





print('Bottle capacity: 500ml')
print('Filling tolerance: 2%')
print(f'Filled bottles: {', '.join(map(str, fillings))}') 
print(f'Incorrectly filled: {incorrect}%')
print(filtered)
