# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file) as file:
    content = file.read()


# regular expression pattern
# for amounts
pattern = r'€(\d+)'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, content)

# calculate the total purchases
summ = 0
for amount in amounts:
   summ += int(amount)

# print result
print(f'Total money spent in €: {summ}')
