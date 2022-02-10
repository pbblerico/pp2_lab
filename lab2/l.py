stack, ans = [], True
for c in input():
    if c in '[{(':
        stack.append(c)
    if c in '])}' and len(stack) == 0:
        ans = False
        break
    if c == ']':
        if stack[-1] == '[':
            stack.pop()
        else:
            ans = False
            break
    if c == ')':
        if stack[-1] == '(':
            stack.pop()
        else:
            ans = False
            break
    if c == '}':
        if stack[-1] == '{':
            stack.pop()
        else:
            ans = False
            break
print('Yes' if ans and len(stack) == 0 else 'No')