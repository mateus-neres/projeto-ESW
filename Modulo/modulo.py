from lib_ESW import tabela_para_excel, pdf_para_tabela, ajustar_valor
from loguru import logger
import os,sys
import pandas as pd
import numpy as np

# Definindo o diretório atual
os.chdir(os.path.dirname(__file__))
dir_atual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Código principal
if __name__ == "__main__":
    try:
        # Extraindo dados do PDF e convertendo para Excel
        tabelas = pdf_para_tabela('extrato.pdf')
        if tabelas is not None:
            tabela_para_excel(tabelas, 'extrato.xlsx')
        
        # Carregar DataFrame
        df = pd.read_excel('extrato.xlsx')

        # Renomear colunas de acordo com os nomes corretos
        df = df.rename(columns={
            'Agência 3793-1': 'Dt. movimento',
            'Unnamed: 1': 'Dt. balancete',
            'Unnamed: 2': 'Histórico',
            'Unnamed: 3': 'Documento',
            'Unnamed: 4': 'Valor R$',
            'Unnamed: 5': 'Saldo'
        })

        # Verificar se as colunas a serem removidas existem no DataFrame
        colunas_para_remover = ['Saldo', 'Dt. balancete', 'Documento']
        colunas_existentes = []

        for coluna in colunas_para_remover:
            if coluna in df.columns:
                colunas_existentes.append(coluna)

        # Remover colunas desnecessárias
        df_cleaned = df.drop(columns=colunas_existentes)

        # Substituir strings vazias e espaços por NaN
        df_cleaned.replace(r'^\s*$', np.nan, regex=True, inplace=True)

        # Remover linhas com qualquer valor NaN
        df_cleaned = df_cleaned.dropna(how='any')

        # Aplicar a função ao DataFrame e atualizar a coluna 'Valor R$'
        df_cleaned['Valor R$'] = df_cleaned['Valor R$'].apply(ajustar_valor)

        # Salvar o DataFrame limpo em um novo arquivo Excel
        caminho_absoluto = os.path.join(dir_atual, "ExtratoLimpo.xlsx")
        df_cleaned.to_excel(caminho_absoluto, index=False)
        logger.info(f'Arquivo Excel limpo salvo com sucesso em: {caminho_absoluto}')

    except Exception as e:
        logger.error(f'Erro ao executar o código principal: {e}')


a = input()