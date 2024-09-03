import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import numpy as np
from lib_ESW import tabela_para_excel, pdf_para_tabela, ajustar_valor
from openpyxl import load_workbook
import os

class TestPipeline(unittest.TestCase):

    @patch('lib_ESW.tabula.read_pdf')
    def test_pdf_para_tabela(self, mock_read_pdf):
        # Mockando a resposta do tabula.read_pdf
        mock_read_pdf.return_value = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        resultado = pdf_para_tabela('extrato.pdf')
        self.assertIsNotNone(resultado)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(list(resultado[0].columns), ['col1', 'col2'])

    @patch('lib_ESW.Workbook.save')
    def test_tabela_para_excel(self, mock_save):
        # Criando uma tabela de exemplo
        tabelas = [pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})]
        tabela_para_excel(tabelas, 'extrato.xlsx')
        mock_save.assert_called_once()

    def test_ajustar_valor(self):
        # Testando casos específicos de valores
        self.assertEqual(ajustar_valor('1.234,56'), 1234.56)
        self.assertEqual(ajustar_valor('1.234,56D'), -1234.56)
        self.assertEqual(ajustar_valor(float('NaN')), None)
        self.assertEqual(ajustar_valor('1234,56C'), 1234.56)

    @patch('lib_ESW.pdf_para_tabela')
    @patch('lib_ESW.tabela_para_excel')
    @patch('lib_ESW.pd.read_excel')
    def test_pipeline(self, mock_read_excel, mock_tabela_para_excel, mock_pdf_para_tabela):
        # Mockando as funções para simular o fluxo de trabalho completo

        # Mockando a extração de tabela
        mock_pdf_para_tabela.return_value = [pd.DataFrame({
            'Agência 3793-1': ['01/01/2020', '02/01/2020'],
            'Unnamed: 1': ['01/01/2020', '02/01/2020'],
            'Unnamed: 2': ['Histórico 1', 'Histórico 2'],
            'Unnamed: 3': ['Doc 1', 'Doc 2'],
            'Unnamed: 4': ['1.234,56', '2.345,67'],
            'Unnamed: 5': ['10.000,00', '12.000,00']
        })]

        # Mockando a leitura do Excel
        mock_read_excel.return_value = pd.DataFrame({
            'Dt. movimento': ['01/01/2020', '02/01/2020'],
            'Dt. balancete': ['01/01/2020', '02/01/2020'],
            'Histórico': ['Histórico 1', 'Histórico 2'],
            'Documento': ['Doc 1', 'Doc 2'],
            'Valor R$': ['1.234,56', '2.345,67'],
            'Saldo': ['10.000,00', '12.000,00']
        })

        # Executar o pipeline
        try:
            tabela = pdf_para_tabela('extrato.pdf')
            if tabela is not None:
                tabela_para_excel(tabela, 'extrato.xlsx')
        except Exception as e:
            logger.error(f'Erro ao executar o código principal: {e}')

        df = pd.read_excel('extrato.xlsx')

        df = df.rename(columns={
            'Agência 3793-1': 'Dt. movimento',
            'Unnamed: 1': 'Dt. balancete',
            'Unnamed: 2': 'Histórico',
            'Unnamed: 3': 'Documento',
            'Unnamed: 4': 'Valor R$',
            'Unnamed: 5': 'Saldo'
        })

        colunas_para_remover = ['Saldo', 'Dt. balancete', 'Documento']
        colunas_existentes = [col for col in colunas_para_remover if col in df.columns]
        df_cleaned = df.drop(columns=colunas_existentes)
        df_cleaned.replace(r'^\s*$', np.nan, regex=True, inplace=True)
        df_cleaned = df_cleaned.dropna(how='any')
        df_cleaned['Valor R$'] = df_cleaned['Valor R$'].apply(ajustar_valor)

        self.assertEqual(df_cleaned['Valor R$'].iloc[0], 1234.56)
        self.assertEqual(df_cleaned['Valor R$'].iloc[1], 2345.67)

if __name__ == '__main__':
    unittest.main()
