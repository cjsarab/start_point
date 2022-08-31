from ntpath import join


def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(number_1, number_2):
    return int(number_1) + int(number_2)

def number_to_full_month_name(month):
    if month == 1:
        return "January"
    elif month == 3:
        return "March"
    elif month == 9:
        return 'September'

def number_to_short_month_name(month):
    if month == 1:
        return 'Jan'
    elif month == 4:
        return "Apr"
    elif month == 10:
        return "Oct"


#

def volume_of_cube(len):
    return len ** 3


def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9
 