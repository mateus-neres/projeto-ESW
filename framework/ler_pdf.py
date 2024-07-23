import PyPDF2
from loguru import logger
import os

# Recebe caminho e nome do arquivo em pdf e retorna o texto do pdf recebi
def ler_pdf(diretorio_pdf, nome_pdf):
    logger.info('Chamanda da função ler_pdf')
    try:
        diretorio = diretorio_pdf
        nome = nome_pdf
        diretorio_nome = os.path.join(diretorio, nome)
        with open(diretorio_nome, 'rb') as pdf_lido:
            leitor_pdf = PyPDF2.PdfReader(pdf_lido)
            texto = ''
            for pagina in range(len(leitor_pdf.pages)):
                texto += leitor_pdf.pages[pagina].extract_text()
        return texto
    except Exception as e:
        logger.error(f'Error ao chamar a função ler_pdf: {e}')