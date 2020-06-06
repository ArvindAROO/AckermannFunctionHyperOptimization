def ackermann(m,n):
    #opening the file to check for values
    file = open('ack_vals.txt','r')
    values = file.read()

    for line in values.split('\n'):
        #each line has the parameters and their corresponding result
        line_arr = line.split(' ')
        #converted into array of numbers
        if line != '':
            #there is a chance that a line might be skipped, so we skip that here
            print(line_arr)
            if int(line_arr[0]) == m and int(line_arr[1]) == n:
                #if they have the required values
                #ans will be found out here itself
                ans = int(line_arr[2])
                file.close()
                #closing the file and returning the answer
                return ans
    #if the answer was not found, we need to find it manually
    file.close()
    #this is the true Ackermann function
    if m==0:
        ans = n+1
    elif n==0:
        ans = ackermann(m-1,1)
    else:
        ans = ackermann(m-1,ackermann(m,n-1))
    #By the time it reaches here, it would have calculated
    #the value, so we add to the file for future calculations
    file = open('ack_vals.txt','a')
    file.write(str(m)+' '+str(n)+' '+str(ans)+'\n')
    file.close()
    return ans
if __name__ == '__main__':
    print("Be careful with the values, the function grows beyond exponentially,")
    print("This function might not find the value in any reasonable amount of time")
    m = int(input("Enter the value of m: "))
    n = int(input("Enter the value of n: "))
    print(ackermann(m,n))
