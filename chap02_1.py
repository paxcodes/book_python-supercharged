def countVowelsConsonants(string):
   vowelCount, consonantCount = 0, 0
   vowels = 'aeiou'
   consonants = 'bcdfghjklmnpqrstvwxyz'
   string = string.lower()
   
   for char in string:
      if char in vowels:
         vowelCount += 1
      elif char in consonants:
         consonantCount += 1
   
   return vowelCount, consonantCount

if '__main__' == __name__:
   string = input("\nEnter a string: ")
   vowels, consonants = countVowelsConsonants(string)
   print(f"Vowels: {vowels}")
   print(f"Consonants: {consonants}")