import unittest
from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"Disc {i}", "Animation", cost=1.0)
            self.assertTrue(cart.add_dvd(dvd))
        extra = DigitalVideoDisc("Disc extra", "Animation", cost=1.0)
        self.assertFalse(cart.add_dvd(extra))


if __name__ == "__main__":
    unittest.main()
