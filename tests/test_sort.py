import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("B", "Animation", cost=20.0))
        self.cart.add_dvd(DigitalVideoDisc("a", "Animation", cost=30.0))
        self.cart.add_dvd(DigitalVideoDisc("C", "Animation", cost=10.0))

    def test_sort_by_title(self):
        titles = [d.title for d in self.cart.sort_by_title()]
        self.assertEqual(titles, ["a", "B", "C"])

    def test_sort_by_cost(self):
        costs = [d.cost for d in self.cart.sort_by_cost()]
        self.assertEqual(costs, [10.0, 20.0, 30.0])


if __name__ == "__main__":
    unittest.main()
