def oops():
    raise IndexError("Congratulations, you have been rewarded with an index error")

trystring = "oh, what a lovely day"

def try_oops():
    try:
        print("oh, what a lovely day to refer to index [194]")
        print(trystring[194])
    except:
        oops()

try_oops()