def updateMaxWidth(numStr, maxWidth):
   currentLength = len(numStr)
   if maxWidth < currentLength:
      maxWidth = len(numStr)
   return maxWidth
         
def splitIntegers(row, maxWidth):
   isClean = True
   currentRow = []

   for index, numStr in enumerate(row.split()):
      try:
         numInt = int(numStr)
      except ValueError:
         print("Row includes a non-integer string. Do it again.")
         isClean = False
         break

      currentRow.append(numInt)
      maxWidth = updateMaxWidth(numStr, maxWidth)

   return isClean, maxWidth, currentRow
   
if '__main__' == __name__:
   rows = []
   maxWidth = 0
   
   while len(rows) < 5:
      row = input(f"Enter row of 5 integers: ")
      isClean, maxWidth, row = splitIntegers(row, maxWidth)
      if isClean:
         rows.append(row)
         
   formattedRows = []
   for row in rows:
      formattedRow = ["{:{maxWidth}}".format(num, maxWidth=maxWidth) for num in row]
      formattedRows.append(" ".join(formattedRow))
   
   print("\n".join(formattedRows))