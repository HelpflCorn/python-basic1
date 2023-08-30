# Task 1

# Primes

NUMBERS = [2,
   1099726899285419,
   1570341764013157, 
   1637027521802551,  
   1880450821379411,  
   1893530391196711,  
   2447109360961063,  
   3,  
   2772290760589219,  
   3033700317376073,  
   4350190374376723,
   4350190491008389,  
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5]


from multiprocessing import Process
import threading
import time


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
def list_prime_check(list):
    start_time = time.time()
    for num in list:
        print(num, is_prime(num))
    end_time = time.time()
    print(end_time-start_time)
    
    

# if __name__ == "__main__": #it took 23 seconds
#     st = time.time()
#     p1 = Process(target=list_prime_check(NUMBERS[:8]))
#     p2 = Process(target=list_prime_check(NUMBERS[8:]))
#     p1.start()
#     p2.start()
#     p1.join
#     p2.join
#     e = time.time()
#     print(e-st)
    
# if __name__ =="__main__": #18 seconds (ᵒ̤̑ ₀̑ ᵒ̤̑) 
#     st = time.time()
#     t1 = threading.Thread(target=list_prime_check(NUMBERS[:8]))
#     t2 = threading.Thread(target=list_prime_check(NUMBERS[8:]))
#     t1.start()
#     t2.start()
#     t1.join
#     t2.join
#     e = time.time()
#     print(e-st)

list_prime_check(NUMBERS) #32.96 seconds 


