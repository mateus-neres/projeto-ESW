from openpyxl import Workbook
from loguru import logger
import os

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