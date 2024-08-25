from loguru import logger
from openpyxl import Workbook
import os, sys
import tabula
import PyPDF2
import pandas as pd

os.chdir(os.path.dirname(__file__))
dir_atual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Recebe o nome do arquivo PDF e retorna uma lista de tabelas extraídas
def pdf_para_tabela(arquivo):
    logger.info('Iniciando a conversão do PDF para tabelas.')
    caminho_absoluto = os.path.join(dir_atual, arquivo)
    try:
        tabelas = tabula.read_pdf(caminho_absoluto, pages='all', stream=True, multiple_tables=True, encoding='ISO-8859-1')
        
        if not tabelas:
            logger.warning('Nenhuma tabela foi extraída do PDF.')
            return None
        
        logger.info('Conversão do PDF para tabelas concluída com sucesso.')
        return tabelas

    except Exception as e:
        logger.error(f'Erro ao converter PDF para tabelas: {e}')
        return None


# Recebe uma lista de tabelas, o diretório para salvar o arquivo Excel e o nome do arquivo, e cria um arquivo Excel
def tabela_para_excel(tabelas, arquivo):
    logger.info('Iniciando a conversão das tabelas para arquivo Excel.')
    caminho_absoluto = os.path.join(dir_atual, arquivo)
    try:
        if not tabelas:
            logger.warning('Nenhuma tabela foi fornecida.')
            return None
        
        workbook = Workbook()
        sheet = workbook.active
        
        for tabela in tabelas:
            linhas = tabela.values.tolist()

            for linha in linhas:
                if linha:
                    sheet.append(linha)
                else:
                    logger.warning('Linha vazia encontrada e ignorada.')

        workbook.save(caminho_absoluto)
        logger.info(f'Arquivo Excel salvo com sucesso em: {caminho_absoluto}')

    except Exception as e:
        logger.error(f'Erro ao salvar a tabela como Excel: {e}')


# Recebe o caminho e o nome do arquivo PDF e retorna o texto extraído do PDF
def ler_pdf(arquivo):
    logger.info('Iniciando a leitura do PDF.')
    caminho_absoluto = os.path.join(dir_atual, arquivo)

    try:
        with open(caminho_absoluto, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto = ''
            
            for pagina in range(len(leitor_pdf.pages)):
                texto += leitor_pdf.pages[pagina].extract_text()
        
        logger.info('Leitura do PDF concluída com sucesso.')
        return texto

    except Exception as e:
        logger.error(f'Erro ao ler o PDF: {e}')
        return None


# Cria um arquivo de texto a partir do conteúdo fornecido
def criar_txt(conteudo, arquivo):
    logger.info('Iniciando a criação do arquivo de texto.')
    caminho_absoluto = os.path.join(dir_atual, arquivo)
    try:
        with open(caminho_absoluto, 'w', encoding='utf-8') as arquivo_txt:
            arquivo_txt.write(conteudo)
        logger.info(f'Conteúdo escrito com sucesso no arquivo: {arquivo}')

    except Exception as e:
        logger.error(f'Erro ao criar o arquivo de texto: {e}')

# Ajusta o valor de acordo com o formato esperado
def ajustar_valor(valor):
    if pd.isna(valor):
        logger.info('Valor é NaN, retornando None.')
        return None
    
    valor_str = str(valor).strip()
    
    valor_str = valor_str.replace('.', '').replace(' ', '')
    
    if valor_str.endswith('D') or valor_str.endswith('C'):
        sufixo = valor_str[-1]
        valor_str = valor_str[:-1]
    else:
        sufixo = ''
    
    try:
        valor_ajustado = float(valor_str.replace(',', '.'))
        if sufixo == 'D':
            valor_ajustado = -valor_ajustado
        logger.info(f'Valor ajustado: {valor_ajustado}')
        return valor_ajustado
    except ValueError:
        logger.error(f'Valor inválido para conversão: {valor_str}')
        return None