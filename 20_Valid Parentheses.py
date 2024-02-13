"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
"""
in ansii:
    "("= 40, "["= 91 , "{"= 123
    ")"= 41, "]"= 93 , "}"= 125
"""

s = "({{{{}}}})[]{}"
stack = []
pair = True
if len(s) <= 1:
    pair = False

for i in s:
    # if it's open brace add to stack
    if i == "(" or i == "[" or i == "{":
        stack.append(i)
    # if it's closed brace, check stack
    if i == ")" or i == "]" or i == "}":
        if len(stack) >= 1 and abs(ord(i) - ord(stack[-1])) <= 2:
            stack.pop()
        else:
            pair = False
if len(stack) != 0:
    pair = False
print(pair)
