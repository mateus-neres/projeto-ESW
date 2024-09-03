# Importa funções necessárias do módulo lib_ESW
import os
from lib_ESW import pdf_para_tabela, tabela_para_excel, ler_pdf, criar_txt, ajustar_valor

#Teste de extração de tabelas do PDF.
def teste_pdf_para_tabela():
    print("Teste pdf_para_tabela")
    tabelas = pdf_para_tabela('extrato.pdf')  # Chama a função para extrair
    if tabelas is not None:
        print(f"Tabelas extraídas: {len(tabelas)}")  # Quantidade de tabelas extraidas
    else:
        print("Nenhuma tabela foi extraída.")

# teste de criação de um arquivo Excel a partir das tabelas extraídas.
def teste_tabela_para_excel():
    print("Teste tabela_para_excel")
    tabelas = pdf_para_tabela('extrato.pdf')  
    if tabelas:
        tabela_para_excel(tabelas, 'teste_excel.xlsx')  # Salva as tabelas em um arquivo Excel
        if os.path.exists('teste_excel.xlsx'):
            print("Arquivo Excel criado.")  
        else:
            print("Falha ao criar a planilha.") 
    else:
        print("Não foi possível criar o arquivo Excel porque nenhuma tabela foi extraída.")  

#Teste de leitura de texto a partir do PDF
def teste_ler_pdf():
    print("Teste ler_pdf")
    texto = ler_pdf('extrato.pdf')  
    if texto:
        print(f"Texto lido com sucesso.")
    else:
        print("Falha ao ler o PDF.")  

# Função para testar a criação de um arquivo de texto
def teste_criar_txt():
    print("Teste criar_txt")
    criar_txt("Conteudo do teste txt.", 'teste.txt')
    if os.path.exists('teste.txt'):
        with open('teste.txt', 'r') as arquivo: 
            conteudo = arquivo.read() 
        print(f"Conteúdo do arquivo de texto: {conteudo}") 
    else:
        print("Falha ao criar o arquivo de texto.") 

# Função para testar a função ajustar_valor
def testar_ajustar_valor():
    print("Teste ajustar_valor")
    valores = ["1.234,56D", "789,00", "1 234,56C", "234,00C", "1.450,00D"]  
    resultados = [ajustar_valor(valor) for valor in valores] 
    print(f"Resultados dos valores ajustados: {resultados}")

# Bloco principal para executar os testes
if __name__ == "__main__":
    teste_pdf_para_tabela()
    teste_tabela_para_excel()  
    teste_ler_pdf() 
    teste_criar_txt()  
    testar_ajustar_valor()  
