def ackermann(m,n):
    #the legacy code for the actual ackermann function
    if m==0:
        ans = n+1
    elif n==0:
        ans = ackermann(m-1,1)
    else:
        ans = ackermann(m-1,ackermann(m,n-1))
    return ans

if __name__ == "__main__":
    print("Be careful with the values, the function grows beyond exponentially,")
    print("This function might not find the value in any reasonable amount of time")
    m = int(input("Enter the value of m: "))
    n = int(input("Enter the value of n: "))
    print(ackermann(m,n))
