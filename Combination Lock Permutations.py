import math

#Global variable
Wheel_Digits = 10

# Get the number of digits from the user
Input_Digits = int(input("Enter the number of digits on the combination lock: "))

# The number of n digit combinations possible if no digit is repeated.
combinations_no_repetition = math.perm(Wheel_Digits, Input_Digits)
print("Number of combinations with no digit repetition:\n", combinations_no_repetition)

# The number of n digit combinations possible if digits can be repeated.
combinations_with_repetition = math.pow(Wheel_Digits, Input_Digits)
print("Number of combinations with digit repetition:\n", combinations_with_repetition)

# The number of n digit combinations possible if successive digits must be different.
combinations_no_successive_repetition = math.perm(Wheel_Digits, Input_Digits) * math.factorial(Input_Digits)
print("Number of combinations with no successive digit repetition:\n", combinations_no_successive_repetition)
