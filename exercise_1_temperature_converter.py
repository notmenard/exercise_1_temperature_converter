# Displaying the introduction line
print(' Temperature Converter '.center(50, "-"))

# Ask the user to input a temperature.
temperature = float(input("\nEnter the temperature: "))

# Ask the user to select the conversion type.
print("\nConversions:")
print("0 for Celsius to Fahrenheit")
print("1 for Fahrenheit to Celsius")

conversion = input("\nSelect a conversion type: ")

# Performing the appropriate conversion and printing the result.
if conversion == '0':
    converted_temp = (temperature * 9 / 5) + 32
    print(f"\nThe temperature {temperature} °C to °F is: {round(converted_temp, 2)} °F.")

elif conversion == '1':
    converted_temp = (temperature - 32) * 5 / 9
    print(f"\nThe temperature {temperature} °F to °C is: {round(converted_temp,2)}")

else:
    print("\nInvalid character. Please try again.")
    