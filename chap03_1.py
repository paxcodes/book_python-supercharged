from random import randint
from functools import reduce

if '__main__' == __name__:
   integers = [ randint(0,100) for i in range(randint(5,20))]
   print(integers)
   print(reduce(lambda x,y: x+y, integers) / len(integers))