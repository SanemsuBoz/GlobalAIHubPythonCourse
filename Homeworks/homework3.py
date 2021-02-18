def prime_first():
    for num in range(0, 500):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)  
                    
def prime_second():
    for num in range(500, 1000):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num) 

prime_first()                   
prime_second()