
def evaluatePostfixExpression(expression):
  ops = expression.split()
  stack = []

  for value in ops:
     if value.isnumeric():
        stack.append(value)
     else:
        if len(stack) < 2:
           print("Invalid expression!")
           break
        
        if value not in '+-*/':
           print("Invalid operator: " + value)
           break
         
        secondOperand = str(stack.pop())
        firstOperand = str(stack.pop())
        value = eval(firstOperand + value + secondOperand)
        stack.append(value)

  return stack.pop()
