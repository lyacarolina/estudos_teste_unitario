#coding=utf-8
import src.CoinDeskExtractor.coindesk_extractor as coindesk_extractor
import unittest

class TestCoinDeskExtractor(unittest.TestCase):    
               
  def test_coindesk_api_return(self):  
    ret = coindesk_extractor.main()
    self.assertTrue(ret['status_code'], 200)          

if __name__ == '__main__':
    unittest.main() 