#!/usr/bin/env python3
a_array = [2,8,9,48,8,22,-12,2]
new_set = set()
for num in a_array:
    if num > 5:
        new_set.add(num+2)
print(a_array)
print(new_set)
