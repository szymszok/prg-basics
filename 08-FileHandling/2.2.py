# Writes Seven Wonders of the World to a file
#
seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
arr_sort = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
    for item in arr_sort:
        file.write(f'{item}\n')