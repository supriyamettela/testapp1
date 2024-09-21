import unittest
from multiply import multiplication
class MultiplyTestCase(unittest.TestCase):

   def test_1(self):

       result = multiplication(3, 4)

       self.assertEqual(result, 12)

   def test_2(self):

       result = multiplication(3, -4)

       self.assertEqual(result, -12)

   def test_3(self):

       result = multiplication(-3, -4)

       self.assertEqual(result, 12)
       
   def test_4(self):

       result = multiplication(3, 0)

       self.assertEqual(result, 0)


   def test_5(self):

       result = multiplication(-3, 0)

       self.assertEqual(result,0)
       
   def test_6(self):

        result = multiplication(3, 1)

        self.assertEqual(result,3)
      
    

       
if __name__ == '__main__':
    unittest.main()
