from pdf_para_tabela import pdf_para_tabela
from tabela_para_excel import tabela_para_excel
from loguru import logger


try:
    tabela = pdf_para_tabela('arquivos_para_leitura', 'EXTRATOSICREDI.pdf')
    if tabela is not None:
        tabela_para_excel(tabela, 'arquivos_gerados', 'EXTRATOSICREDI.xlsx')
except Exception as e:
    logger.error(f'Erro ao executar o código principal: {e}')