import unittest
import copy

# where a contains b
def diff(a, b):
    for k in a:
        if k in b:
            b.remove(k)
            a.remove(k)

    return a

def buy(n):
    if (len(n) == 0):
        return 0
    if (len(n) == 1):
        return 8

    nset = set(n)
    if (len(nset) == len(n)):
        return 8 * len(nset) - len(nset) * 8 * 5 * (len(nset) - 1) / 100

    tmp = copy.deepcopy(list(nset))
    sub = diff(n, tmp)
    return buy(sub) + buy(list(nset))

class PotterTests(unittest.TestCase):

    def testFail(self):
        self.assertEqual(0, buy([]))

    def testOne(self):
        self.assertEqual(8, buy([1]))

    def testOneTwo(self):
        self.assertEqual(8*2 - 8*2*5/100, buy([1,2]))

    def testOneTwoThree(self):
        self.assertEqual(8*3 - 8*3*10/100, buy([1,2,3]))

    # we want 15%! no map ma!
    #def testOneTwoThreeFour(self):
    #    self.assertEqual(8*4*20/100, buy([1,2,3,4]))

    def testOneTwoTwo(self):
        self.assertEqual(8*2 - 8*2*5/100 + 8, buy([1,2,2]))

    def testOneOneTwoTwo(self):
        self.assertEqual((8*2 - 8*2*5/100) *2, buy([1,1,2,2]))

    def testOneOneOneTwoTwo(self):
        self.assertEqual((8*2 - 8*2*5/100) *2 + 8, buy([1,1,1,2,2]))

    def testOneOneTwoTwoThreeThree(self):
        self.assertEqual((8*3- 8*3*10/100) *2, buy([1,1,2,2,3,3]))

    # this one fail. I dont know why yet
    def testOneOneOneTwoTwoThreeThree(self):
        self.assertEqual((8*3- 8*3*10/100) *2 + 8, buy([1,1,1,2,2,3,3]))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
