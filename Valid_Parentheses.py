'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
    	# Initialize a empty stack
        stack=[]
        for index in range(len(s)):
        	# for opening braces like (,{,[  will push character into the stack
            if s[index]=="(" or s[index]=="{" or s[index]=="[":
                stack.append(s[index])
            else:
            	# stack is empty
                if len(stack)==0:
                    return  False
                else:
                	# for closing braces like ),},] we will pop from the stack
                	# Can only pop if stack top contain (,{,[ for ),},] respectively
                    if s[index]==")" and stack[len(stack)-1]=="(":
                        stack.pop(len(stack)-1)
                    elif s[index]=="}" and stack[len(stack)-1]=="{":
                        stack.pop(len(stack)-1)
                    elif s[index]=="]" and stack[len(stack)-1]=="[":
                        stack.pop(len(stack)-1)
                    # Can't pop if stack top does not contain (,{,[ for ),},] respectively
                    # So that is not a valid parentheses.So,return false
                    else:
                        return False 
        # If stack is empty after poping all elements then return true
        if len(stack)==0:
            return True
        # If stack is not empty after poping all elements then return false
        else:
            return False

#Time Complexity=O(N)
#Space Complexity=O(1)
                    
                    