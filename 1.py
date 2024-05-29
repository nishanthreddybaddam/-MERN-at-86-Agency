''' 1. Given an expression string exp, write a program to examine whether the pairs and
the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.

Input exp = “[()]{}{[()()]()}”
Output Balanced
Explanation all the brackets are well-formed
Input exp = “[(])”
Output Not Balanced
Explanation 1 and 4 brackets are not balanced because
there is a closing ‘]’ before the closing ‘(‘     '''

def is_balanced(expression):
    # Dictionary to hold matching pairs of brackets
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    # Stack to keep track of opening brackets
    stack = []
    
    for char in expression:
        if char in matching_bracket.values():  # If it is an opening bracket
            stack.append(char)
        elif char in matching_bracket.keys():  # If it is a closing bracket
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "Not Balanced"
    
    return "Balanced" if not stack else "Not Balanced"

# Test cases
exp1 = "[()]{}{[()()]()}"
exp2 = "[(])"

print(is_balanced(exp1))  # Output: Balanced
print(is_balanced(exp2))  # Output: Not Balanced
