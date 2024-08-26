import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
import sys
import os
import math

# Adiciona o diretório pai ao sys.path para importar lib_ESW
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib_ESW import ajustar_valor, pdf_para_tabela, tabela_para_excel, ler_pdf, criar_txt

class TestLibESW(unittest.TestCase):

    def test_ajustar_valor(self):
        self.assertEqual(ajustar_valor('1.234,56'), 1234.56)
        self.assertEqual(ajustar_valor('1.234,56D'), -1234.56)
        self.assertEqual(ajustar_valor('1.234,56C'), 1234.56)
        self.assertTrue(math.isnan(ajustar_valor('NaN')))
        self.assertEqual(ajustar_valor('invalid'), None)

    @patch('lib_ESW.tabula.read_pdf')
    def test_pdf_para_tabela(self, mock_read_pdf):
        mock_read_pdf.return_value = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        tabelas = pdf_para_tabela('dummy.pdf')
        self.assertIsNotNone(tabelas)
        self.assertEqual(len(tabelas), 1)

        mock_read_pdf.side_effect = Exception('Erro ao ler PDF')
        tabelas = pdf_para_tabela('dummy.pdf')
        self.assertIsNone(tabelas)

    @patch('lib_ESW.Workbook')
    def test_tabela_para_excel(self, mock_workbook):
        mock_workbook_instance = mock_workbook.return_value
        mock_sheet = mock_workbook_instance.active

        tabelas = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        tabela_para_excel(tabelas, 'dummy.xlsx')
        mock_workbook_instance.save.assert_called_once_with(os.path.abspath('dummy.xlsx'))

        tabela_para_excel([], 'dummy.xlsx')
        mock_workbook_instance.save.assert_not_called()

    @patch('lib_ESW.open', new_callable=mock_open, read_data='dummy text')
    @patch('lib_ESW.PyPDF2.PdfReader')
    def test_ler_pdf(self, mock_pdf_reader, mock_open_file):
        mock_pdf_reader_instance = mock_pdf_reader.return_value
        mock_pdf_reader_instance.pages = [MagicMock(extract_text=lambda: 'page text')]

        texto = ler_pdf('dummy.pdf')
        self.assertEqual(texto, 'page text')

        mock_open_file.side_effect = Exception('Erro ao abrir PDF')
        texto = ler_pdf('dummy.pdf')
        self.assertIsNone(texto)

    @patch('lib_ESW.open', new_callable=mock_open)
    def test_criar_txt(self, mock_open_file):
        criar_txt('dummy content', 'dummy.txt')
        mock_open_file.assert_called_once_with(os.path.abspath('dummy.txt'), 'w', encoding='utf-8')
        mock_open_file().write.assert_called_once_with('dummy content')

if __name__ == '__main__':
    unittest.main()