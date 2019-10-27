from math import sqrt

def generatePerfectSquares(limit):
   i=1
   while i <= sqrt(limit):
      perfectSquare = i**2
      print(perfectSquare)
      yield perfectSquare
      i += 1

def checkIfPerfectSquare(value):
   value = int(value)
   return value in generatePerfectSquares(value)

if '__main__' == __name__:
   while True:
      value = input("Enter number: ")
      if value == 'q': break
      print("Is perfect square? " + str(checkIfPerfectSquare(value)))
      