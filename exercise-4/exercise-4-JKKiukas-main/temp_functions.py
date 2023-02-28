"""
There are two functions in this file. One converts a temperature from Fahrenheit to Celsius from user's input and
other classifies a temperature value in Celsius into one of four categories.

Parameters:
Both functions have parameters.

Returns:
First function returns a float value and second function returns An integer.
"""


# Define the function to convert Fahrenheit to Celsius
def fahr_to_celsius(temp_fahrenheit):
    """
    This function converts a temperature from Fahrenheit to Celsius from user's input.

    Parameters:
    temp_fahrenheit (float): A temperature in Fahrenheit.

    Returns:
    float: The temperature converted to Celsius.
    """
    # Convert temperature from Fahrenheit to Celsius
    converted_temp = (temp_fahrenheit - 32) * 5 / 9
    return converted_temp


# Ask the user to input a temperature in Fahrenheit
temp_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert the temperature from Fahrenheit to Celsius and print the result
converted_temp = fahr_to_celsius(temp_fahrenheit)

print(f"{temp_fahrenheit}° Fahrenheit is {converted_temp}° Celsius")


def temp_classifier(temp_celsius):
    """
    This function classifies a temperature value in Celsius into one of four categories (0-3)
    based on the following criteria:
    - 0: temperatures below -2 Celsius
    - 1: temperatures equal or warmer than -2, but less than +2 Celsius
    - 2: temperatures equal or warmer than +2, but less than +15 Celsius
    - 3: temperatures equal or warmer than +15 Celsius

    Parameters:
    temp_celsius (float): A temperature value in Celsius

    Returns:
    int: An integer representing the temperature classification (0-3)
    """

    # Check what is the temperature classification
    if temp_celsius < -2:
        return 0
    elif temp_celsius < 2:
        return 1
    elif temp_celsius < 15:
        return 2
    else:
        return 3


# Get user input
temp_celsius = float(input("Enter a temperature in Celsius: "))

# Classify a temperature which user gave
classification = temp_classifier(temp_celsius)
print(f"A temperature of {temp_celsius} degrees Celsius is classified as {classification}")
