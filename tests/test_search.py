import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))

    def test_case_insensitive(self):
        self.assertEqual(len(search_by_title(self.cart, "lion")), 1)

    def test_ignores_surrounding_spaces(self):
        self.assertEqual(len(search_by_title(self.cart, "  lion ")), 1)


if __name__ == "__main__":
    unittest.main()
