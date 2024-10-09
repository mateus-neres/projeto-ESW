from lib_ESW import tabela_para_excel, pdf_para_tabela, ajustar_valor, caminho_absoluto_arquivo
from openpyxl import Workbook, load_workbook
from loguru import logger
import logging
import os
import pandas as pd
import numpy as np

############################### Gerenciamento de  Log ###############################
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())

logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG)

if not os.path.exists(caminho_absoluto_arquivo('./log_file')):
    os.makedirs(caminho_absoluto_arquivo('./log_file'))

log_file = os.path.join(caminho_absoluto_arquivo('./log_file'), 'log.txt')

logger.add(log_file, format="{time} {level} {file}:{line} {message}", level="DEBUG")
#####################################################################################

try:
    # Extraindo dados do PDF e convertendo para Excel

    tabelas = pdf_para_tabela(caminho_absoluto_arquivo('extrato.pdf'))
    if tabelas is not None:
        tabela_para_excel(tabelas, caminho_absoluto_arquivo('extrato.xlsx'))
    
    # Carregar DataFrame
    df = pd.read_excel(caminho_absoluto_arquivo('extrato.xlsx'), engine='openpyxl')

    # Renomear colunas de acordo com os nomes corretos
    df = df.rename(columns={
        'Agência 3793-1': 'Dt. movimento',
        'Unnamed: 1': 'Dt. balancete',
        'Unnamed: 2': 'Histórico',
        'Unnamed: 3': 'Documento',
        'Unnamed: 4': 'Valor R$',
        'Unnamed: 5': 'Saldo',
    })

    # TODO tratar os dados antes de excluir as colunas.

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

    df_cleaned.to_excel(caminho_absoluto_arquivo("ExtratoLimpo.xlsx"), index=False)
    logger.info(f'Arquivo Excel limpo salvo com sucesso em: {caminho_absoluto_arquivo("ExtratoLimpo.xlsx")}')

except Exception as e:
    logger.error(f'Erro ao executar o código principal: {e}')
