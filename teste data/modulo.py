from lib_ESW import tabela_para_excel, pdf_para_tabela, ajustar_valor
from loguru import logger
import os,sys
import pandas as pd
import numpy as np

# Definindo o diretório atual
os.chdir(os.path.dirname(__file__))
dir_atual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Configurações do Pandas para exibir todas as colunas e linhas
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# Geração de logs
logger.add('logfile.txt', format="{time} {level} {file} {message}", level="INFO")

# Extraindo dados do PDF e convertendo para Excel
try:
    tabela = pdf_para_tabela('extrato.pdf')
    if tabela is not None:
        tabela_para_excel(tabela, 'extrato.xlsx')
except Exception as e:
    logger.error(f'Erro ao executar o código principal: {e}')

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
colunas_existentes = [col for col in colunas_para_remover if col in df.columns]

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