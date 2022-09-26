class Samsung:
 "Parent/super class"
 def __init__(self):
  print("I am Samsung")

 def makeScreen(self):
  print("I make screen")

 def test(self):
  print("Screen test : OK")

class iPhone(Samsung):
  "Child/sub class"
  def __init__(self):
   print("I am iPhone")
   # super ().__init__()

  def a3chiphs(self):
   print("I make a3 bionic chips")

  def itest(self):
   print("a3 test : OK")
   # super mthod is used to borrow functionality in child method
   super ().test()

  # method overriding same method name with different functionality
  def makeScreen(self):
   print("I make screen : apple")

user = iPhone()

user.a3chiphs()
user.makeScreen()
user.itest()
user.makeScreen()