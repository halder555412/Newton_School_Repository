'''

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Constraints:

* haystack and needle consist only of lowercase English characters.

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	# neddle is empty so return 0
        if needle=="":
            return 0
        flag=0
        # Use string slicing and check with needle string
        for index in range(len(haystack)-len(needle)+1):
        	# haystack="hello",needle="ll"
        	# haystack[index:len(needle)+index]
        	# index=0, haystack[0:2+0]=="he"
        	# index=1, haystack[1:2+1]=="el"
        	# index=2, haystack[2:2+2]=="ll" which is equals to needle, so return 2
            if haystack[index:len(needle)+index]==needle:
                flag=1
                return index
        # needle is not part of haystack
        if flag==0:
            return -1
#Time Complexity=O(N)
#Space Complexity=O(1)
        