import unittest
from EncryptDecrypt import *
import random as rand
import string


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #self.assertEqual(decrypt("@YqyYE]d.SHq}C*D~", 0), "YyEdSqCD@qY].H}*~")

        for i in range(100):

            strng = ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(0,rand.randint(1,100),2))

            print '*'*10
            numb = 1 #rand.randint(0,100)

            print 'String: {}'.format(strng)
            print 'Encr: ' + encrypt(strng,numb)
            print 'Decr: ' + decrypt(encrypt(strng,numb),numb)

            self.assertEqual(decrypt(encrypt(strng,numb),numb), strng)

if __name__ == '__main__':
    unittest.main()
