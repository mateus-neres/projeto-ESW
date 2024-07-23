import re
from PyPDF2 import PdfReader
from tabulate import tabulate

datas = []
descricoes = []
documentos = []
valores = []
saldos = []

# Lista para armazenar as linhas com quebra de página
linhas_com_quebra_de_pagina = []

def extrato_sicredi():
    # Inicializando a variável texto_lido
    texto_lido = ""

    # Abrindo um arquivo PDF existente
    with open("EXTRATOSICREDI.pdf", "rb") as input_pdf:
        mes = ""
        valor = 0.0
        # Criando um objeto PdfFileReader
        pdf_reader = PdfReader(input_pdf)

        # Obtendo o número de páginas do arquivo PDF
        num_pages = len(pdf_reader.pages)

        # Lendo o texto de cada página
        for page_number in range(num_pages):
            # Verificando se é uma nova página e adicionando quebra de linha se necessário
            if page_number > 0:
                linhas_com_quebra_de_pagina.append('\n')
            
            # Adicionando o número da página à lista
            #linhas_com_quebra_de_pagina.append(f'Texto da página {page_number + 1}:')

            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            # print(text)
            linhas_com_quebra_de_pagina.append(text)

    # Imprimindo as linhas com quebra de página
    for linha in linhas_com_quebra_de_pagina:
        texto_lido += linha

   
    saldo_aterior = texto_lido.strip().split("\n")[5].split(" ")[2]

    inicio = texto_lido.find(saldo_aterior)
    recorte = len(saldo_aterior) + inicio
    print(recorte)

    linhas_formatadas = []
    fim = texto_lido.find("Saldo da conta (Saldo em 01/03/2024)")
    #print(texto_lido)
    #print(recorte)
    #print(texto_lido[recorte:fim])

    for linha in texto_lido[recorte:fim].strip().split("\n"):
        linhas_formatadas.append(linha.split())

    for linha_formatada in linhas_formatadas:
        if linha_formatada:
            # datas.append(linha_formatada[0])
            # descricoes.append(linha_formatada[1:-3])
            # valores.append(linha_formatada[-2])
            # documentos.append(linha_formatada[-3])

            data = linha_formatada[-2]
            data2 = linha_formatada[0]
            #print(data)

            tirar_ponto = data.replace(".", "")
            data_corrigido = tirar_ponto.replace(",", ".")
            
            #print(type(data))
            #Valores com saldo negativo
            #print(valor)
            try:
                # linha_tabela = [['Mes',data2]]
                # mes, valor = linha_tabela
                data = float(data_corrigido)
                #print("Valor")

                if data < 0:
                    valor = float(data)
                    #print(30*"-")
                    #print(f"Data: {mes:^6} - Valor: {valor:>13,.2f}")
                    #print("Valor")
                    print('\n')
                    print(tabulate([['Mes',"Valor"],[data2,data]], headers="firstrow"))
                    #print(tabulate(linha_tabela))
            except:
                pass
            #print(data)
            #print(tabulate(linhas_formatadas, headers=['Data', 'Descrição 1', 'Descrição 2', 'Descrição 3', 'Descrição 4', 'Descrição 5', 'Descrição 6', 'Descrição 7', 'Descrição 8', 'Valor 1', 'Valor 2']))
    #print(valor)

#   Solucao para transformar a lista de listas em uma lista de strings da descricao
    for linha in linhas_formatadas:
        texto = ' '.join(linha[1:-3])
         #data = linha[0]
        
        #print(texto) 
# fim da solucao
        
def extrato_bb():
    texto_lido = ""
    texto_editado = ""
    contador = 0
    
    #valores_processados = []


    # Abrindo um arquivo PDF existente
    with open("BANCOBB-FEVEREIRO.pdf", "rb") as input_pdf:
        # Criando um objeto PdfFileReader
        pdf_reader = PdfReader(input_pdf)

        # Obtendo o número de páginas do arquivo PDF
        num_pages = len(pdf_reader.pages)

        # Lendo o texto de cada página
        for page_number in range(num_pages):
            # Verificando se é uma nova página e adicionando quebra de linha se necessário
            if page_number > 0:
                linhas_com_quebra_de_pagina.append('\n')
            
            # Adicionando o número da página à lista
            #linhas_com_quebra_de_pagina.append(f'Texto da página {page_number + 1}:')

            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            #print(text+"\n")
            linhas_com_quebra_de_pagina.append(text)
        
        # Imprimindo as linhas com quebra de página
    for linha in linhas_com_quebra_de_pagina:
        for line in linha.split('\n'):
            #print(line)
            texto_lido += line + '\n'
        #print(texto_lido)
    
    inicio = texto_lido.find("Saldo") + len("Saldo") # 270
    fim = texto_lido.find("------------------------------------------------")
    #print(texto_lido[inicio:fim])
    linhas = texto_lido[inicio:fim].splitlines()

# Iterando sobre cada linha
    # Imprimindo o cabeçalho
    print("Dt. balancete\tDt. movimento\tAg. origem\tLote\tHistórico\tDocumento\tValor R$\tSaldo")
    valores_processados = []
# Iterando sobre cada linha
    for linha in linhas:
        # Separando os valores na linha por espaços em branco
        valores = linha.split()
        # Inicializando uma lista para armazenar os valores processados
       
        # Iterando sobre cada valor na linha
        for valor in valores:
            # Tentando converter o valor para float
            try:
                float_valor = float(valor.replace(".", "").replace(",", "."))
                # Se a conversão for bem-sucedida, adicione o valor formatado à lista
                valores_processados.append("{:.2f}".format(float_valor))
            except ValueError:
                # Se a conversão falhar, adicione o valor original à lista
                valores_processados.append(valor)
            # Imprimindo os valores processados separados por tabulação
        print("\t".join(valores_processados))
        #contador += 1
        #print(valores_processados[contador])
        texto_editado += str("\t".join(valores_processados))
                
        #(valores_processados)
    #print(valores_processados)
    #print(texto_lido.find("Saldo"))
    #print(texto_lido[270:])


def extrato_bn():
    texto_lido = ""
    texto_editado = ""
    contador = 0
    
    #valores_processados = []


    # Abrindo um arquivo PDF existente
    with open("ExtratoContaCorrenteBNB (2).pdf", "rb") as input_pdf:
        # Criando um objeto PdfFileReader
        pdf_reader = PdfReader(input_pdf)

        # Obtendo o número de páginas do arquivo PDF
        num_pages = len(pdf_reader.pages)

        # Lendo o texto de cada página
        for page_number in range(num_pages):
            # Verificando se é uma nova página e adicionando quebra de linha se necessário
            if page_number > 0:
                linhas_com_quebra_de_pagina.append('\n')
            
            # Adicionando o número da página à lista
            #linhas_com_quebra_de_pagina.append(f'Texto da página {page_number + 1}:')

            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            recorte = text.find("Saldo R$") + len("Saldo R$")

            recorte_fim = text.find("Detalhamento do Saldo")
            #print(recorte_fim)
            #contador += recorte_fim

            

            #print(text[recorte:recorte_fim])
            
            linhas_com_quebra_de_pagina.append(text[recorte:recorte_fim])
        #print(contador)
        # Imprimindo as linhas com quebra de página
    for linha in linhas_com_quebra_de_pagina:
        for line in linha.split('\n'):
            print(line)
            texto_lido += line + '\n'
       # print(texto_lido)
    
    # inicio = texto_lido.find("Saldo") + len("Saldo") # 270
    # fim = texto_lido.find("------------------------------------------------")
    # #print(texto_lido[inicio:fim])
    # linhas = texto_lido[inicio:fim].splitlines()


#extrato_bb()
extrato_sicredi()
#extrato_bn()

# Fazer um filtro de data
#Pega os valores e implemeta automaticamente por data.
# Transformar extrato em pdf para excel
# Criar uma api para fazer a conversão de pdf para excel
# Google colab - so que tiver extração de dados

