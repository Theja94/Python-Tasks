"""You are developing a program that analyzes weather data. Write
a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest
temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
"""

def analyse(inp):
    avg = sum(inp)/len(inp)
    high = max(inp)
    low = min(inp)
    return avg,high,low

if __name__ == "__main__":
    temperature_readings = [25, 28, 21, 24, 27]
    avg, high, low = analyse(temperature_readings)
    print(f"Average temperature: {avg} \nHighest Temperature: {high} \nLowest Temperature: {low}")
