categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

expensive = expenses.index(max(expenses))

most_expensive_category = categories[expensive]
most_expensive_amount = expenses[expensive]

print(f'The most expensive category is {most_expensive_category} with money spent {most_expensive_amount}')
