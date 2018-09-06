"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError: #when you enter characters/invalid symbols
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError: #when trying to divide by zero
#     print("Cannot divide by zero!")
# print("Finished.")

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError: #when you enter characters/invalid symbols
    print("Numerator and denominator must be valid numbers!")
print("Finished.")