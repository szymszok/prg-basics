import matplotlib.pyplot as plt

# Temperature data
temperatures = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}

# Extracting city names and their corresponding temperatures
cities = list(temperatures.keys())
temp_values = list(temperatures.values())

# Creating the bar chart
plt.bar(cities, temp_values, color='blue')

# Adding title and labels
plt.title('Temperatures Recorded in Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')

# Displaying the chart
plt.axhline(0, color='black', linewidth=0.8)  # Adding a horizontal line at y=0 for reference
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding grid lines for better readability
plt.show()