
# This is a coding test to both see if you know what a palindrome is and how to 
# parse the data using re

def is_palindrome(s):
    # Convert string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

test_p = "A man, a plan, a canal, Panama!"
test_p2 = "Not a palindrome"
test_p3 = "racecar"
print(is_palindrome(test_p))
print(is_palindrome(test_p2))

#Explanation of [::-1]

# In Python, the colon (:) is used in slicing notation to specify the start, stop, and step indices for selecting a range of items from a sequence like a list, tuple, or string. Here's how it works:

# Basic Notation: The basic slicing syntax is [start:stop:step], where:
# start: The index where the slicing starts (inclusive).
# stop: The index where the slicing ends (exclusive).
# step: The increment between each index. It determines how many items are skipped between each index.
# Default Values: If any of the parameters are omitted, Python uses default values:
# If start is not provided, it defaults to the beginning of the sequence.
# If stop is not provided, it defaults to the end of the sequence.
# If step is not provided, it defaults to 1.
# Examples:
# s[1:5]: Selects items from index 1 to 4 (5th index is not included).
# s[::2]: Selects every second item from the entire sequence.
# s[::-1]: Reverses the sequence.
# Usage: The colon is essential for specifying slicing operations in Python, providing flexibility in accessing and manipulating data structures efficiently.