'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:1

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example:2

Input: [-2,-1,-3,-4,-1,-2,-1,-5,-4]
Output: -1
Explanation: [-1] has the largest sum = -1.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	#Initialize maximum as max_=0 and next maximum as max_next=0 
        max_,max_next=0,0
        #Check nums array that it contains any positive integer or not.If not then return maximum element from nums as maximum subarray otherwise break from the loop.  
        Negetive_check=0
    	# [-3,-4,-5,-7,-1,-10]
    	# output:-1 because -1 is maximum element
        for i in nums:
            if i>0:
                Negetive_check=1
                break
            else:
                continue
        if Negetive_check==0:
            return max(nums)
        for i in nums:
        	#Pick a element from the arr and add it with the max_next and check max_next  is greater than max_ or not.
            max_next=max_next+i
            #If max_next>max_ then update max_=max_next 
            if max_next>max_:
                max_=max_next
            #If max_next is not greater than max_  then check max_next less than 0  or not if yes then update max_next=0
            elif max_next<0:
                max_next=0
            else:
                continue
        # Return the sum of maximum subarray
        return max_
'''
#Time Complexity=O(n)
#Space Complexity=O(1)
        
        
