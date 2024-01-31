def int_to_roman(num):
    # Define the Roman numeral symbols and their corresponding values
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    
    }
    result = ''

    # Iterate through the values in reverse order
    for value in sorted(roman_numerals.keys(), reverse=True):
        # Repeat the Roman numeral symbol as many times as needed
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result

def roman_to_int(roman):
    # Define the mapping of Roman numeral symbols to their corresponding values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    # Iterate through the Roman numeral string in reverse order
    for symbol in reversed(roman):
        value = roman_numerals[symbol]
        # If the current value is greater than the previous value, subtract it
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result

# Test the function
inp = input("Please enter the Roman numerals or the number you want to convert: ")

try:
    #Checking to see if the input is a number
    inp = int(inp)
except:
    #If it was not a number we assume a string
    inp = str(inp.upper())
finally:
    if type(inp) == str:
         print(roman_to_int(inp))
    else:
        print(int_to_roman(inp))

