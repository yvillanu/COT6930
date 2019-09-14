import sys
sys.path.append('..')

import unittest
from RSA import *

sys.setrecursionlimit(5000)

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#


# Generate a pair of primes
#p,q = 61, 53
p,q = 982451653, 776531401


n = p * q


# Carmichael's totient funciton, which is the same as Euler's in this case.
l = lcm(p -1, q - 1)


#Choose e and compute d using the extended euclidean algorithm
#e = 17
e = 65537
d = inverse(e, l)


public_key = (n, e)
private_key = (n, d)

#m = 65

message = "abc123"


m = string2int(message)

c = rsa_encrypt(m, public_key)

m2 = rsa_decrypt(c, private_key)

message2 = int2string(m2)



if __name__ == '__main__':
    unittest.main()
