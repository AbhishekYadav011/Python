def exactly3Divisors(N):
        # code here
    prime = [True for i in range(N+1)]
    prime[0] = prime[1] = False

    p=2 
    while (p*p<= N):
        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
            for i in range(p*p,N+1,p):
                prime[i] = False
        p +=1
            
    i = 0
    count = 0 
    while(i*i<=N):
        if (prime[i]):
            print(i*i, end=" ")
            count +=1
        i+=1
    return count      
      

if __name__ == '__main__':
     print(exactly3Divisors(6))