import  unittest
from data import Products

class Itemscheck(unittest.TestCase):
    
    def setUp(self):
        self.products = Products()

    def test_products(self):
        self.assertEqual(self.products, 50, msg='invalid balance')
    def test_productquantity(self):
        self.products.Quantity(60)
        self.assertEqual(self.products, 110, msg='invalid quantity')

