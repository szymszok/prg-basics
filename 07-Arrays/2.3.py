# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities = 0
total = 0
week_expenses = []
for week in monthly_expenses:
    week_total = sum(week)
    week_expenses.append(week_total)

    food += week[0]
    transport += week[1]
    utilities += week[2]
    total += week_total
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)
print('Transport:', transport)
print('Utilities:', utilities)
print('Week 1:', week_expenses[0])
print('Week 2:', week_expenses[1])
print('Week 3:', week_expenses[2])
print('Week 4:', week_expenses[3])
print('---------------')
print('TOTAL:', total)