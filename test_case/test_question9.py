import unittest
from test_case.question2 import searchbar,utilites
from test_case.question3 import menubar

t1=unittest.TestLoader().loadTestsFromTestCase(searchbar(),utilites())
t2=unittest.TestLoader().loadTestsFromTestCase(menubar())
s1=unittest.TestSuite([t1,t2])#the suit should be group data item it will not execute single module
unittest.TextTestRunner.run(s1)


"""
if "__name__"=="__main__":
unitest.main(htmlTestRunner=htmlTestRunner.html,path=r"")



"""