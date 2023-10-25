#coding=utf-8
import json
import pytest
import unittest
import pandas as pd
import src.CoinDeskTransformer.coindesk_transformer as coindesk_transformer

TEST_FILE_PATH = 'tests/CoinDeskTransformer/1698148495.json'

class TestCoinDeskTransformer(unittest.TestCase):    
               
    def test_path_exists(self):
        """Testando se o path existe"""

        error = 'Parâmetro path não informado.'
        with pytest.raises(Exception) as err:
            ret = coindesk_transformer.main()
        self.assertEqual(error, str(err.value))
    
    def test_coindesk_file_path_exists(self):
        """Testando se existe os paths usd, gbp e eur no retorno"""

        ret = coindesk_transformer.main(TEST_FILE_PATH)

        expected_keys = ['usd_file_path', 'gbp_file_path', 'eur_file_path']
        self.assertTrue(len(set(expected_keys) - set(ret)) == 0)
    

    def test_coindesk_transformer_result_usd(self):
        """Testa o resultado de usd"""
        ret = coindesk_transformer.main(TEST_FILE_PATH)
        
        mock_df = pd.read_csv('tests/CoinDeskTransformer/usd.csv')
        df = pd.read_csv(ret['usd_file_path'])
        self.assertIsNone(
            pd.testing.assert_frame_equal(mock_df, df)
        )
    

    def test_coindesk_transformer_result_eur(self):
        """Testa o resultado de eur"""
        ret = coindesk_transformer.main(TEST_FILE_PATH)
        
        mock_df = pd.read_csv('tests/CoinDeskTransformer/eur.csv')
        df = pd.read_csv(ret['eur_file_path'])
        self.assertIsNone(
            pd.testing.assert_frame_equal(mock_df, df)
        )
    

    def test_coindesk_transformer_result_gbp(self):
        """Testa o resultado de gbp"""
        ret = coindesk_transformer.main(TEST_FILE_PATH)
        
        mock_df = pd.read_csv('tests/CoinDeskTransformer/gbp.csv')
        df = pd.read_csv(ret['gbp_file_path'])
        self.assertIsNone(
            pd.testing.assert_frame_equal(mock_df, df)
        )


if __name__ == '__main__':
    unittest.main()