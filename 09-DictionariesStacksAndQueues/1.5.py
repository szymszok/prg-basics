countries = [
{"name":"Poland", "population":38000000},
{'name':'Japan', 'population':12500000},
{'name':'Canada', 'population':39000000},
{'name':'Indonesia', 'population':277500000},
{'name':'Brazil', 'population':215400000}
]


for country in countries:
    name = country['name']
    pop = country['population']
    print(f'{name} has population of {pop} people')