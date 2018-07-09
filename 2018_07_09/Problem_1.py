#Problem 1
# 1. On the python website, find a builtin module.
# Describe and show examples of some of the useful functions
# in the module and how they might be utilized by us.

# re -- regular expressions
# https://docs.python.org/3.6/library/re.html#module-re

import re

# Useful in parsing strings

my_string = 'This is my string which contains words and numbers like 123'

# Can be used to search for a substring within your string

new_string = re.search('words', my_string)
new_string.group()
print(new_string.group())

# Start and end in the string

start = new_string.start()
end = new_string.end()
print(my_string[start:end])

# Match ambiguous strings next two words after 'my'

new_string = re.search('my \w+ \w+', my_string)
print(new_string.group())

# Find all words which end in 's' in a string

s = re.findall('\w+s', my_string)
print(s)

# Replace characters with new characters

new_string = re.sub(' ', '\n' , my_string)
new_string
print(new_string)

# Count occurences of substitutions

new_string = re.subn(' ', '\n' , my_string)
new_string
print(new_string[1])
