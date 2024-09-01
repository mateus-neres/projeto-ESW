import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open, MagicMock
import os
import sys
import pandas as pd
from lib_ESW import LibEsw

class TestLibEsw(unittest.TestCase):
    def setUp(self):
        self.lib_esw = LibEsw()
        self.test_pdf = "test.pdf"
        self.test_excel = "test.xlsx"
        self.test_txt = "test.txt"
        self.test_content = "This is a test content."
        self.test_table = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    @patch('tabula.read_pdf')
    def test_pdf_para_tabela(self, mock_read_pdf):
        mock_read_pdf.return_value = [self.test_table]
        result = self.lib_esw.pdf_para_tabela(self.test_pdf)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertTrue(mock_read_pdf.called)

    @patch('openpyxl.Workbook.save')
    def test_tabela_para_excel(self, mock_save):
        self.lib_esw.tabela_para_excel([self.test_table], self.test_excel)
        self.assertTrue(mock_save.called)

    #@patch('PyPDF2.PdfReader')
    #def test_ler_pdf(self, mock_pdf_reader):
      #  mock_pdf_reader.return_value.pages = [MagicMock(extract_text=MagicMock(return_value="Page 1 text")),
       #                                       MagicMock(extract_text=MagicMock(return_value="Page 2 text"))]
     #   result = self.lib_esw.ler_pdf(self.test_pdf)
        #self.assertIsNotNone(result)
        #self.assertIn("Page 1 text", result)
        #self.assertIn("Page 2 text", result)
    
    


    def test_ler_pdf(self):
        caminho_pdf = '/home/erick/Documents/ProjetoEngenharia/projeto-ESW/test/test.pdf'
        resultado = LibEsw.ler_pdf(caminho_pdf)
        self.assertIsNotNone(resultado)
        #self.assertIn("Texto esperado", resultado)

    @patch('builtins.open', new_callable=mock_open)
    def test_criar_txt(self, mock_file):
        self.lib_esw.criar_txt(self.test_content, self.test_txt)
        mock_file.assert_called_with(os.path.join(self.lib_esw.dir_atual, self.test_txt), 'w', encoding='utf-8')
        mock_file().write.assert_called_once_with(self.test_content)

    def test_ajustar_valor(self):
        self.assertEqual(self.lib_esw.ajustar_valor("1.234,56"), 1234.56)
        self.assertEqual(self.lib_esw.ajustar_valor("1.234,56D"), -1234.56)
        self.assertEqual(self.lib_esw.ajustar_valor("1.234,56C"), 1234.56)
        self.assertIsNone(self.lib_esw.ajustar_valor("invalid"))
        self.assertIsNone(self.lib_esw.ajustar_valor(pd.NA))

if __name__ == '__main__':
    unittest.main()