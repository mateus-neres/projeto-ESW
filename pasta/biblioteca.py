from loguru import logger
from openpyxl import Workbook
import os
import tabula
import PyPDF2

# Recebe o direotiro e o nome do aquivo.pdf e retorna uma tabela
def pdf_para_tabela(diretorio_pdf, nome_pdf):
    logger.info('Convertendo PDF para tabela. Função pdf_para_tabela')
    
    diretorio = diretorio_pdf
    nome = nome_pdf 
    diretorio_nome = os.path.join(diretorio, nome)
    
    try:
        extrair_tabela_do_pdf = tabula.read_pdf(diretorio_nome, pages='all', stream=True, multiple_tables=True,encoding='ISO-8859-1')

        if extrair_tabela_do_pdf is None:
            logger.warning('Nenhuma tabela extraida do PDF')
            return None
        
        logger.info('Conversão do PDF para tabela concluída com sucesso')
        return extrair_tabela_do_pdf

    except Exception as e:
        logger.error(f'Erro ao inicializar a conversão de PDF para tabela. Função pdf_para_tabela: {e}')
        return None
    


# Recebe a tabela de dados, diretorio para salvar o arquivo xlsx, e o nome do arquivo, e cria um arquivo xlsx com as variaveis recebidas
def tabela_para_excel(tabela, diretorio_para_salvar_excel, nome_arquivo_para_salvar):
    logger.info('Convertendo tabela para arquivo xlsx. Função tabela_para_excel')
    try:

        if tabela is None:
            logger.warning('Nenhuma tabela foi fornecida')
            return None

        diretorio_nome = os.path.join(diretorio_para_salvar_excel, nome_arquivo_para_salvar)
        
        pasta_de_trabalho = Workbook()
        planilha_de_trabalho = pasta_de_trabalho.active
        
        for bloco_de_dados in tabela:
            linhas = bloco_de_dados.values.tolist()

            for  linha in linhas:
                if linha is not None:
                    planilha_de_trabalho.append(linha)
                else:
                    logger.error('O valor da linha é vazio')

        pasta_de_trabalho.save(diretorio_nome)
        logger.info('Conversão de tabela para xlsx realizada com sucesso')
        logger.info(f'Arquivo xlsx salvo com sucesso em : {diretorio_nome}')

    except Exception as e:
        logger.error(f'Erro inicializar a conversão da tabela para xlsx. Função tabela_para_excel: {e}')

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


# testando funções

try:
    tabela = pdf_para_tabela('arquivos_para_leitura', 'EXTRATOSICREDI.pdf')
    if tabela is not None:
        tabela_para_excel(tabela, 'arquivos_gerados', 'EXTRATOSICREDI.xlsx')
except Exception as e:
    logger.error(f'Erro ao executar o código principal: {e}')