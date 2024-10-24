# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
from keyboard import  *


# Reads employee's data from keyboard
first_name = input_string('Enter name: ')
last_name = input_string('Enter surname: ')
age = input_integer('Enter age: ')
salary = input_real('Enter salary: ')
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname:', last_name)
print('Age:', age)
if is_salary_hidden == True:
    print('Salary')
else:
    print(salary)