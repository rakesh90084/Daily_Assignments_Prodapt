import multiprocessing
start=2
stop=500
def findprime():
    for i in range(start,stop+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
                else:
                    print(i,end=" ") 
                    break   
def findpalindrome():
    for num in range(10, 500 + 1):
        temp = num
        reverse = 0
    
        while(temp > 0):
            Remainder = temp % 10
            reverse = (reverse * 10) + Remainder
            temp = temp //10

        if(num == reverse):
            print(num,end=" ")
            
if(__name__=="__main__"):
       

    p1=multiprocessing.Process(target=findprime)
    p2=multiprocessing.Process(target=findpalindrome)
    p1.start()
    p1.join()
    print("\n","Done printing prime numbers")
    p2.start()
    p2.join()
    print("\n","Done printing palindrome numbers")