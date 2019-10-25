from time import time 

def profile(func):
   def wrapper():
      start = time()
      print(func)
      returnValue = func()
      end = time()
      print('Time elapsed was', end-start)
      return returnValue
   return wrapper

@profile
def fast():
   print('\n'.join(['*' * 20] * 20))

@profile
def slow():
   for row in range(0,20):
      for column in range(0,20):
         print('*', end="")
      print()

if '__main__' == __name__:
   slow()
   fast()
   
