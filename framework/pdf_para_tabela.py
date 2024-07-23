import os
import tabula
from loguru import logger

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
    

