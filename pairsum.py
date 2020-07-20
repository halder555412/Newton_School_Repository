#You are given an array A of size N, and you are also given a sum. 
#You need to find if two numbers in A exists such that their sum is equal to the given sum. 
#If yes, print 1, else print 0.

def hasArrayTwoCandidates(A, arr_size, sum):  
    A.sort() #sort the array
    l = 0
    r = arr_size-1 
    # traverse the array for the two elements 
    while l<r: 
        #if sum found return 1
        if (A[l] + A[r] == sum): 
            return 1
        #if sum of lower bound elements and upper bound elements less than the required sum then increase lower bound index by 1
        elif (A[l] + A[r] < sum): 
            l += 1
        #if sum of lower bound elements and upper bound elements greater than required sum then decrease upper bound index by 1
        else: 
            r = r-1
    return 0
       
n,s=map(int,input().split()) #taking  input array size and sum
arr=list(map(int,input().split())) #taking input array
if (hasArrayTwoCandidates(arr,n,s)): #function call
    print(1) #pair found in the array
else: 
    print(0) #pair not found in the array

    
'''
Sample Input
10 14
1 2 3 4 5 6 7 8 9 10

Sample Output
1

Explanation 
10 + 4 = 14,  so pair exists

Sample Input
5 9
1 2 3 4 5 

Sample Output 
1
'''
