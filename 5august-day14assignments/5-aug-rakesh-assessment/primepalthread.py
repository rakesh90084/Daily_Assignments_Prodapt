import threading
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
       

    t1=threading.Thread(target=findprime)
    t2=threading.Thread(target=findpalindrome)
    t1.start()
    t1.join()
    print("\n","Done printing prime numbers")
    t2.start()
    t2.join()
    print("\n","Done printing palindrome numbers")