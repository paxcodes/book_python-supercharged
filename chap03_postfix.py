
def evaluatePostfixExpression(expression):
  ops = expression.split()
  stack = []

  for value in ops:
     if value.isnumeric():
        stack.append(value)
     else:
        secondOperand = str(stack.pop())
        firstOperand = str(stack.pop())
        value = eval(firstOperand + value + secondOperand)
        stack.append(value)

  return stack.pop()
