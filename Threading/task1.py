# Task 1

# A shared counter

# Make a class called Counter, and make it a subclass of the Thread class in the Threading module. 
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000. 
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and
# for each time increments the value of the counter by 1. Create 2 instances of the thread and start them, then join 
# them and check the result of the counter, it should be 200.000, right? Run it a couple of times and consider some 
# different reasons why you get the answer that you get. 



import threading

counter = 0
rounds = 100000

class Counter(threading.Thread):
    def run(self):
        global counter, rounds
        for i in range(rounds):
            counter += 1

thread1 = Counter()
thread2 = Counter()


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final counter value:", counter) # the result is 200000 as each instance that was ran had been joined