from loguru import logger
from openpyxl import Workbook
import os
import sys
import tabula
import PyPDF2
import pandas as pd
import numpy as np

# Definindo o diretório atual
os.chdir(os.path.dirname(__file__))
dir_atual = os.path.dirname(os.path.abspath(sys.argv[0]))

# Configuração de logs
logger.add('logfile.txt', format="{time} {level} {file} {message}", level="INFO")

# Função para extrair tabelas de um PDF
def pdf_para_tabela(arquivo_pdf):
    logger.info('Iniciando a conversão do PDF para tabelas.')
    caminho_absoluto = os.path.join(dir_atual, arquivo_pdf)
    
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

# Função para salvar tabelas em um arquivo Excel
def tabela_para_excel(tabelas, arquivo_excel):
    logger.info('Iniciando a conversão das tabelas para arquivo Excel.')
    caminho_absoluto = os.path.join(dir_atual, arquivo_excel)
    
    try:
        if not tabelas:
            logger.warning('Nenhuma tabela foi fornecida.')
            return
        
        workbook = Workbook()
        sheet = workbook.active
        
        for tabela in tabelas:
            for linha in tabela.values.tolist():
                if linha:
                    sheet.append(linha)
                else:
                    logger.warning('Linha vazia encontrada e ignorada.')
        
        workbook.save(caminho_absoluto)
        logger.info(f'Arquivo Excel salvo com sucesso em: {caminho_absoluto}')
    
    except Exception as e:
        logger.error(f'Erro ao salvar a tabela como Excel: {e}')

# Função para extrair texto de um PDF
def ler_pdf(arquivo_pdf):
    logger.info('Iniciando a leitura do PDF.')
    caminho_absoluto = os.path.join(dir_atual, arquivo_pdf)
    
    try:
        with open(caminho_absoluto, 'rb') as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)
            texto = ''
            
            for pagina in range(len(leitor_pdf.pages)):
                texto += leitor_pdf.pages[pagina].extract_text()
        
        logger.info('Leitura do PDF concluída com sucesso.')
        return texto
    
    except Exception as e:
        logger.error(f'Erro ao ler o PDF: {e}')
        return None

# Função para criar um arquivo de texto
def criar_txt(conteudo, arquivo_txt):
    logger.info('Iniciando a criação do arquivo de texto.')
    caminho_absoluto = os.path.join(dir_atual, arquivo_txt)
    
    try:
        with open(caminho_absoluto, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
        logger.info(f'Conteúdo escrito com sucesso no arquivo: {caminho_absoluto}')
    
    except Exception as e:
        logger.error(f'Erro ao criar o arquivo de texto: {e}')

# Função para ajustar valores monetários
def ajustar_valor(valor):
    if pd.isna(valor):
        logger.info('Valor é NaN, retornando None.')
        return None
    
    valor_str = str(valor).strip().replace('.', '').replace(' ', '')
    
    sufixo = ''
    if valor_str.endswith('D') or valor_str.endswith('C'):
        sufixo = valor_str[-1]
        valor_str = valor_str[:-1]
    
    try:
        valor_ajustado = float(valor_str.replace(',', '.'))
        if sufixo == 'D':
            valor_ajustado = -valor_ajustado
        logger.info(f'Valor ajustado: {valor_ajustado}')
        return valor_ajustado
    
    except ValueError:
        logger.error(f'Valor inválido para conversão: {valor_str}')
        return None

