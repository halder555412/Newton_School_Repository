'''

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag=0
        # Pick element from arr if it match with target value
        for index in range(len(nums)):
        	# picking element match with targe that means target reach its desire position. So, return index
            if nums[index]==target:
                flag=1
                return index
            # Picking element greater than target that means target reach its desire index.So,return index
            elif nums[index]>target:
                flag=1
                return index
            else:
                continue
        # Target element is greater than all arr elemens.So,insert at last position 
        if flag==0:
            return len(nums)

# Time Complexity = O(n)
# Space Complexity = O(1)

