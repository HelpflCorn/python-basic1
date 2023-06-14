samplestring1 = "asdasd"
samplestring_first = samplestring1[0:2]
samplestring_second = samplestring1[-3:len(samplestring1)]
samplestring_fixed = samplestring_first+samplestring_second

if len(samplestring_fixed) > 2:
    print(samplestring_fixed)
if len(samplestring1) < 2:
    print("Empty String")
