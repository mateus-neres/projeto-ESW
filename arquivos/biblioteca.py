from loguru import logger
from openpyxl import Workbook
import os
import tabula
import PyPDF2

# Recebe o diretório e o nome do arquivo PDF e retorna uma tabela
def pdf_para_tabela(caminho_pdf, nome_pdf):
    logger.info('Iniciando a conversão do PDF para tabela.')
    caminho_completo = os.path.join(caminho_pdf, nome_pdf)
    
    try:
        tabelas_extraidas = tabula.read_pdf(caminho_completo, pages='all', stream=True, multiple_tables=True, encoding='ISO-8859-1')
        
        if not tabelas_extraidas:
            logger.warning('Nenhuma tabela foi extraída do PDF.')
            return None
        
        logger.info('Conversão do PDF para tabela concluída com sucesso.')
        return tabelas_extraidas

    except Exception as e:
        logger.error(f'Erro ao converter PDF para tabela: {e}')
        return None


# Recebe a tabela de dados, o diretório para salvar o arquivo Excel e o nome do arquivo, e cria um arquivo Excel
def tabela_para_excel(tabelas, caminho_para_salvar_excel, nome_arquivo_excel):
    logger.info('Iniciando a conversão da tabela para arquivo Excel.')
    caminho_completo = os.path.join(caminho_para_salvar_excel, nome_arquivo_excel)
    try:
        if not tabelas:
            logger.warning('Nenhuma tabela foi fornecida.')
            return None
        
    
        pasta_de_trabalho = Workbook()
        planilha_ativa = pasta_de_trabalho.active
        
        for tabela in tabelas:
            linhas = tabela.values.tolist()

            for linha in linhas:
                if linha:
                    planilha_ativa.append(linha)
                else:
                    logger.warning('Linha vazia encontrada e ignorada.')

        pasta_de_trabalho.save(caminho_completo)
        logger.info(f'Arquivo Excel salvo com sucesso em: {caminho_completo}')

    except Exception as e:
        logger.error(f'Erro ao salvar a tabela como Excel: {e}')


# Recebe o caminho e nome do arquivo PDF e retorna o texto do PDF
def ler_pdf(caminho_pdf, nome_pdf):
    logger.info('Iniciando a leitura do PDF.')
    caminho_completo = os.path.join(caminho_pdf, nome_pdf)
    try:
        with open(caminho_completo, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            texto = ''
            
            for pagina in range(len(leitor_pdf.pages)):
                texto += leitor_pdf.pages[pagina].extract_text()
        
        logger.info('Leitura do PDF concluída com sucesso.')
        return texto

    except Exception as e:
        logger.error(f'Erro ao ler o PDF: {e}')
        return None


# Cria um arquivo de texto a partir do texto fornecido
def criar_txt(texto, nome_arquivo_txt):
    logger.info('Iniciando a criação do arquivo de texto.')
    try:
        with open(nome_arquivo_txt, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
        logger.info(f'Texto escrito com sucesso no arquivo: {nome_arquivo_txt}')

    except Exception as e:
        logger.error(f'Erro ao criar o arquivo de texto: {e}')
