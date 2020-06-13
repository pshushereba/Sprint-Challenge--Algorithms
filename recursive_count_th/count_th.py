'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    substr_index = word.find('th')

    if substr_index == -1:
        return 0
    else:
        count += 1
    
    count += count_th(word[substr_index + 2:])

    return count

# U - Understand
# Input is a string
# need to count occurences of a substring. should return count
# need to use recursion.
# What if there are multiple instances of 'th'?
# Ignore uppercase instances

# P - Plan
# initiate a counter and set to 0
# Find 'th' in the word.
# increase the count variable
# .find() method will return the first index where the substring occurs.
# https://www.geeksforgeeks.org/python-string-find/
# figure out how to iterate through the string. Probably need to slice the string.
# probably need to keep track of the index where we find the first instance and then use it.
# need to figure out where to call the function recursively.

# E - Execute.

# count = 0
# substr_index = word.find('th)
# if substr_index == -1
#     return 0
# else count += 1
# count += count_th(word[substr_index+2:])
# return count