import sys

def is_permutation(arg1, arg2):
    first_set = set(arg1)
    second_set = set(arg2)
    return first_set == second_set

def is_unique(arg_to_test):
    unique_letters = set()
    for letter in arg_to_test:
        if(letter in unique_letters):
            return True
        else:
            unique_letters.add(letter)
    return False

def replace_spaces(input_string):
    updated_string = ""
    for letter in input_string:
        if(letter == " "):
            letter = "%20"
        updated_string += letter
    return updated_string

def count_chars(input):
    counts = dict()
    for letter in input:
        if(letter in counts):
            counts[letter] += 1
        elif(letter.isalpha()):
            counts[letter] = 1
    count_string = ""
    for key, value in counts.items():
        count_string += str(key)
        count_string += str(value)
    if(len(count_string) > len(input)):
        return input
    else:
        return count_string
