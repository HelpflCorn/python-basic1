"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String"""
#

samplestring1 = "X"
samplestring_first = samplestring1[0:2]
samplestring_second = samplestring1[-2:len(samplestring1)]
samplestring_fixed = samplestring_first+samplestring_second

if len(samplestring1) >= 2:
    print(samplestring_fixed)
if len(samplestring1) < 2:
    print("Empty String")