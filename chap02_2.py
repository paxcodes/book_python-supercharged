def stripFirstAndLast2characters(string):
   return string[2:-2]

if '__main__' == __name__:
   string = input("\nEnter a string: ")
   result = stripFirstAndLast2characters(string)
   print(f"Result: {result}")
   