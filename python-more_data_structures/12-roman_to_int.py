#!/usr/bin/python3
def roman_to_int(roman_number):
    if not isinstance(roman_number, str) or roman_number is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_value = 0

    for i in range(len(roman_number)):
        if i > 0 and roman_dict[roman_number[i]] > roman_dict[roman_number[i - 1]]:
            int_value += roman_dict[roman_number[i]] - 2 * roman_dict[roman_number[i - 1]]
        else:
            int_value += roman_dict[roman_number[i]]

    return int_value
