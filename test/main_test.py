import unittest
from dataclasses import is_dataclass
from loguru import logger
from main import Product


class TestProduct(unittest.TestCase):

    # testando se Product é uma dataclass
    def test_if_it_is_a_dataclass(self):
        logger.info("Testando se Product é uma dataclass")
        self.assertTrue(is_dataclass(Product))

    # incrementar estoque    
    def setUp(self): 
        self.product = Product(1, "teste", 10.0, 10)
        logger.info(f"Configurando o produto: {self.product}")

    def test_constructor(self):
        logger.info("Testando o construtor do Product")
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "teste")
    
    def test_increase_stock(self):
        logger.info("Testando o aumento de estoque")
        self.product.increase_stock(10)
        self.assertEqual(self.product.stock, 20)
    
    def test_decrease_stock(self):
        logger.info("Testando a redução de estoque")
        self.product.decrease_stock(10)
        self.assertEqual(self.product.stock, 0)
    
    def test_check_positive_number(self):
        
        with self.assertRaises(Exception) as assert_error:
            self.product.check_positive_number(-1)
        self.assertEqual(str(assert_error.exception), "Number must be positive")
        logger.info("Testando se o número é positivo")
    
    def test_check_negative_stock(self):
        
        with self.assertRaises(Exception) as assert_error:
            self.product.decrease_stock(11)
        self.assertEqual(assert_error.exception.args[0], "Stock must be greater than or equal to 0")
        #print(assert_error.exception.args[0])
        logger.info("Testando se o estoque é negativo")

if __name__ == '__main__':
    unittest.main()