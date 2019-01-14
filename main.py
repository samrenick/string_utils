from utils import *

try:
    arg1 = sys.argv[1]
except:
    print("Please use two arguments")
    arg1 = ""
try:
    arg2 = sys.argv[2]
except:
    print("Please use two arguments")
    arg2 = ""

print(is_unique(arg1))
print(is_permutation(arg1, arg2))
print("input: " + arg1)
print(arg2)
print("output: " + replace_spaces(arg1))
print(count_chars(arg1))
