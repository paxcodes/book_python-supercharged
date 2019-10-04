from chap02_2 import stripFirstAndLast2characters

def test_stripFirstAndLast2characters():
   test_data = {
      "489023102": "90231",
      "hello": "l",
      "": "",
   }
   
   for key in test_data:
      result = stripFirstAndLast2characters(key)
      assert test_data[key] == result