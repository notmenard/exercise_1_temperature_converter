# Displaying the introduction line
print(' Temperature Converter '.center(50, "-"))

# Ask the user to input a temperature.
temperature = float(input("\nEnter the temperature: "))

# Ask the user to select the conversion type.
print("\nConversions:")
print("0 for Celsius to Fahrenheit")
print("1 for Fahrenheit to Celsius")

conversion = input("\nSelect a conversion type: ")
