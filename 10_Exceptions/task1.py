# Task 1

# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except 
# state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?


def oops():
    raise IndexError("Congratulations, you have been rewarded with an index error")

trystring = ("oh, what a lovely day to refer to index [194], which is totally not out of range")

def try_oops():
    try:
        print(trystring[194])
    except:
        oops() #as function of oops is to raise an error, if changed to key error in the function - it should raise it even if there's no key if try doesn't work

try_oops()