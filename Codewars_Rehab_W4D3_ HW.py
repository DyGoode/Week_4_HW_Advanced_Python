"""
Problem 1
Disemvowel Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
"""

# Original solution
# Time: logarithmic O(log n)

def disemvowel(string_):
    no_vowels = []
    vowels = 'aeiouAEIOU'
    for x in string_:
        if x not in vowels:
            no_vowels.append(x)
    return ''.join(no_vowels)

# Optimized solution
# Time: Linear O(n)

def disemvowel2(string_2):
    vowels2 = 'aeiouAEIOU'
    return ''.join(filter(lambda x: x not in vowels2, string_2))



"""
Problem 2
Kooka-Counter
https://www.codewars.com/kata/58e8cad9fd89ea0c6c000258/train/python
"""
# Original solution
# Time: logarithmic O(log n) 
def kooka_counter(laughing):
    count = 0
    if laughing == "":
        return count
    x = ""
    for i in range(0, len(laughing), 2):
        if laughing[i] != x:
            count += 1
            x = laughing[i]
    return count

# Optimized solution
# Time: Linear O(n)
import re
def kooka_counter(laughing):
    return len(re.findall(r'(ha)+|(Ha)+',laughing))



"""
Problem 3
Disemvowel Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e
"""
# Original solution
# Time: Logarithmic O(log n)
def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
        if i not in vowels:
            new_string+= i 
    return new_string

# Optimized solution
# Time: Linear O(n)
def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    return ''.join(filter(lambda x: x not in vowels, string_))