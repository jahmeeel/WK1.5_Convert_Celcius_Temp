'''
This Python program converts a temperature in Celsius to Fahrenheit. 
It takes an input in Celsius and outputs the temperature in Fahrenheit, rounded to two decimal places.
'''
'''
Understand the Problem:
- Write a Python program to convert a temperature in Celsius to Fahrenheit.
- Round the temperature to two decimal places.
- Print the temperature in Fahrenheit.
- The formula for converting Celsius to Fahrenheit is: (C * 9/5) + 32.

Inputs:
- Temperature in Celsius

Outputs:
- Temperature in Fahrenheit

Examples:
- Input: 30.0
- Output: 32.0

Plan:
- Prompt the user to enter a temperature in Celsius.
- Write a computation to convert the temperature in Celsius to Fahrenheit.
- Print the temperature in Fahrenheit.

Execute.

Review Notes:
- I tried to use the built-in function round() to round the temperature within an f-string, but it didn't work.
- Instead, I decided to put it outside of the f-string and just concatenate it with a comma.

'''

ask_celsius = float(input("Enter a temperature in Celsius: "))

fahrenheit = (ask_celsius * 9/5) + 32

print(f"The temperature in Fahrenheit is:", round(fahrenheit, 2))
