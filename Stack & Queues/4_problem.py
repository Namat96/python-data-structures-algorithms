#.....Parentheses Balancing (RSA Key Parsing)........
def is_balanced(expression):
    stack = []
    bracket = {")": "(", "]":"[", "}":"{"}
    for char in expression:
        if char in bracket.values():
            stack.append(char)
        elif char in bracket.keys():
            if not stack or stack.pop() != bracket[char]:
                return False
    return len(stack) == 0
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
             






































































