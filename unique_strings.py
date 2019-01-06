import sys

def is_unique(string):
    unique_letters = set()
    for letter in arg_to_test:
        if(letter in unique_letters):
            return True
        else:
            unique_letters.add(letter)
    print("unique!")
    return False

arg_to_test = sys.argv[1]
is_unique(arg_to_test)

