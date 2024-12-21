class IOString():

   def __init__(self):
      self.str1 = ""


   def get_String(self):
      self.str1 = input("Enter string : ")


   def upper_String(self):
      print("Result is :", self.str1.upper())

   def lower_String(self):
      print("Result is :", self.str1.lower())


str1 = IOString()

str1.get_String()
str1.upper_String()
str1.lower_String()
