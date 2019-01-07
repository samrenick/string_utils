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

arg1 = sys.argv[1]
arg2 = sys.argv[2]
print(is_unique(arg1))
print(is_permutation(arg1, arg2))
