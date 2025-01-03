medals = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]
win = lambda country: country['gold'] + country['silver'] + country['bronze']
filtered = filter(lambda country: win(country) > 10, medals)
print('COUNTRIES WITH AT LEAST 10 MEDALS: ')
for i in filtered:
    print(f'{i['country']}: {i['gold']},{i['silver']},{i['bronze']}')