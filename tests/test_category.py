import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "Ron Clements", 90, 18.99))
        cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))
        result = search_by_category(cart, "animation")
        self.assertEqual([d.title for d in result], ["Aladdin"])


if __name__ == "__main__":
    unittest.main()
