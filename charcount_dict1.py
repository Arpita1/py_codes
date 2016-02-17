#!/usr/bin/env python3
sentence = (input("Enter any sentence: "))
count = {}
for char in sentence:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)

