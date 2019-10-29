def collectHex():
   isLast = False
   nums = []
   while True:
      value = input("Enter a hexadecimal number: ")
      if '' == value:
         break
      
      if 'q' == value:
         isLast = True
         break
      
      try:
         value = int(value, 16)
      except ValueError:
         print("Not a hexadecimal.")
         continue
   
      nums.append(value)
   
   return nums, isLast
   
if '__main__' == __name__:
   while True:
      nums, isLast = collectHex()
      print("Sum: 0x%X" % sum(nums))
      
      if isLast:
         break
         
      