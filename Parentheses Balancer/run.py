def assertTest(input, result):
    if valid_parentheses(input) == result:
        print(input + "," + str(result) +", Test has passed")
    else:
        print(input + "," + str(result) +", Test has failed")

def valid_parentheses(string):
    if string == "":
        return True
    arr = list(string)
    stack = []
    for x in arr:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if(len(stack)):
        return False
    else:
        return True

assertTest("(Ssadsadsadasd()", False)