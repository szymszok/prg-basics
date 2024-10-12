# A program that displays your height both in cm and in feet and inches.
#

cm = 170
inches = cm / 2.54 
feet = inches // 12
inches_rem = inches % 12


print(f'I am {cm}cm tall,  {feet} feet and {inches_rem:.2f} inches')