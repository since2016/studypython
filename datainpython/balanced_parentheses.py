from stack import Stack

def balanced_parentheses(str1):
    stk = Stack(10)
    for s in str1:
        if s=='(':
            stk.push(s)
        elif s==')':
            if stk.is_empty():
                return False
            else:
                stk.pop()
    return stk.is_empty()


if __name__ == '__main__':
    strs = ["((()))","((())","(()))"]
    for str1 in strs:
        print("result: "+ str(balanced_parentheses(str1)))

