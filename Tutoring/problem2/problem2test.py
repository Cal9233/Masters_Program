from problem2 import Itibag
import unittest
from random import shuffle
from typing import Self, Any


class TestData:
    id: int
    buffer: list[int]
    def __init__(self, id: int):
        self.id = id
    def __hash__(self):
        return hash(self.id)
    def __lt__(self, other: Self):
        return self.id < other.id
    def __le__(self, other: Self):
        return self.id <= other.id
    def __gt__(self, other: Self):
        return self.id > other.id
    def __ge__(self, other: Self):
        return self.id >= other.id
    def __eq__(self, other: Any):
        if isinstance(other, TestData):
            return self.id == other.id
        else:
            return False
    def __str__(self):
        return str(self.id)
    def __repr__(self):
        return repr(self.id)




class TestProblem2(unittest.TestCase):

    def generate_testdata(self, n: int) -> list[TestData]:
        return [TestData(i) for i in range(0, n)]
    
    def generate_randlist(self, n: int):
        rlist = list(range(0, n))
        shuffle(rlist)
        return rlist

    def test_insert(self):

        data = self.generate_testdata(100)

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
    
    def test_remove_one(self):

        data = self.generate_testdata(10)
        target = data[7]

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        result = bag.remove(target)
        self.assertEqual(target, result)

        key = -1
        for d in bag:
            self.assertLess(key, d.id)
            key = d.id
    
    def test_remove_all(self):

        data = self.generate_testdata(100)

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        order = self.generate_randlist(100)

        count = 1
        for i in order:
            item = bag.remove(data[i])
            self.assertEqual(item, data[i])
            self.assertEqual(len(bag), 100-count)
            count += 1
        
        for d in bag:
            self.assertTrue(False)
    
    def test_remove_nothing(self):

        data = self.generate_testdata(10)
        extra = TestData(1000)

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        result = bag.remove(extra)
        self.assertIsNone(result)
        self.assertEqual(len(bag), 10)
    
    def test_clear(self):

        data = self.generate_testdata(100)

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        bag.clear()

        self.assertEqual(len(bag), 0)

        for d in bag:
            self.assertTrue(False)
    
    def test_iterate(self):

        data = self.generate_testdata(100)
        shuffle(data)
        order = [d.id for d in data]

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        i = 0
        for item in bag:
            self.assertEqual(item.id, order[i])
            i += 1
    
    def test_reverse(self):
        data = self.generate_testdata(100)
        shuffle(data)
        order = [d.id for d in reversed(data)]

        bag: Itibag[TestData] = Itibag()

        for d in data:
            bag.add(d)
        
        i = 0
        for item in reversed(bag):
            self.assertEqual(item.id, order[i])
            i += 1

    def test_len(self):
        data = self.generate_testdata(100)
        bag: Itibag[TestData] = Itibag()
        for d in data:
            bag.add(d)
        
        self.assertEqual(len(bag), 100)
    
    def test_full_str(self):
        data = self.generate_testdata(10)
        bag: Itibag[TestData] = Itibag()
        lis: list[TestData] = []
        for d in data:
            bag.add(d)
            lis.append(d)
        self.assertEqual(str(bag), str(lis))
    
    def test_empty_str(self):
        bag: Itibag[TestData] = Itibag()
        lis: list[TestData] = []
        self.assertEqual(str(bag), str(lis))
    
    def test_single_str(self):
        bag: Itibag[TestData] = Itibag()
        lis: list[TestData] = []
        item = TestData(7)
        bag.add(item)
        lis.append(item)
        self.assertEqual(str(bag), str(lis))
    
    def test_duplicates(self):

        data = TestData(1)
        bag: Itibag[TestData] = Itibag()

        bag.add(data)
        bag.add(data)

        self.assertEqual(len(bag), 1)