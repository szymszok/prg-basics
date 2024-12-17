speed = ['48','47','54','50','42','68','39','46']

is_over = list(filter(lambda x:int(x) > 50,speed))

print(f'Speed to high: {is_over}')