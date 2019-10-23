from math import ceil
import bisect

def getMedian(nums):
   """
   Get median of nums.
   
   Args:
      List of numbers.
   
   Rturn:
      The median.
   """
   nums.sort()
   listLength = len(nums)
   mid = ceil(listLength / 2)
   if listLength % 2:
      median = nums[mid]
   else:
      median = (nums[mid] + nums[mid-1]) / 2
      
   return median
   
   
if '__main__' == __name__:
   nums = []
   while True:
      num = input("Add a number to your list. If done, enter 'q': ")
      if 'q' == num:
         break
      bisect.insort(nums, float(num))

   print(getMedian(nums))