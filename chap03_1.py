from random import randint
from functools import reduce

if '__main__' == __name__:
   integers = [ randint(0,100) for i in range(randint(5,20))]
   mean = reduce(lambda x,y: x+y, integers) / len(integers)
   print(integers)
   print(mean)
   
   deviation = [ (mean-i)**2 for i in integers]
   print(deviation)