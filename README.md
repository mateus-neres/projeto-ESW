<div align="center">
  <img src="ufpb_logo.png" alt="Alt Text" width="100"/>

### UNIVERSIDADE FEDERAL DA PARAÍBA

### CAMPUS IV – CENTRO DE CIÊNCIAS APLICADAS E EDUCAÇÃO – RIO TINTO/PB

**Curso:** Licenciatura em Ciências da Computação – LCC

**Curso:** Bacharelado em Sistemas de Informação - BSI

**Componente Curricular:** Engenharia de Software – 8103151

**Prof.:** Luiz Sérgio Plácido da Silva
#
**Alunos:**

Mateus Neres Da Silva

Valeria Joyse Santos Nunes

John Wesley Da Silva Moreira Pinto

Gabriel dos Santos Lopes

Erick Fernandes De Farias Santos

#

Rio Tinto
 2024

</div>

#
<div align="center">

# Projeto de Engenharia de Software - Análise de Extratos Bancários

</div>






## Descrição
Este projeto foi desenvolvido para a disciplina de Engenharia de Software na Universidade Federal da Paraíba. O objetivo do projeto é criar uma ferramenta que leia extratos bancários mensais, extraia relatórios de gastos e rendimentos, e forneça uma análise detalhada através de dashboards interativos.
<div align="center">

## Funcionalidades

</div>


- Leitura de extratos bancários em diversos formatos (PDF).
- Extração de dados relevantes como despesas, receitas, saldos e categorias de gastos.
- Geração de relatórios detalhados sobre despesas e rendimentos.
- Criação de dashboards interativos para visualização e análise dos dados financeiros.
<div align="center">

## Tecnologias Utilizadas

</div>

- **Linguagem de Programação**: Python, Jupyter Notebook

- **Bibliotecas**: Pandas, Matplotlib, Seaborn, Plotly, Dash, loguru, openpyxl, os, tabula, PyPDF2

<div align="center">

## Estrutura do Projeto

</div>

PROJETO-ESW

├── modulo/

│   ├── modulo.py - Código principal do projeto

│   ├── lib_ESW.py - Arquivo contendo funções utilizadas no projeto.

│   ├── extratos/Extratos bancários para análise.

│   ├── relatorios/Relatórios gerados a partir dos extratos.

│   ├── dashboards/Dashboards criados para visualização - integração com power BI

├── teste

│   ├── analise_extratos.py - 

│   ├── geracao_relatorios.py - 


# 
<div align="center">

# Ciclo de Vida do Projeto
## Planejamento e Definição de Requisitos

</div>

### Objetivo:

- Entender as necessidades dos usuários e definir os requisitos funcionais e não funcionais do sistema.

### Atividades:

- Reuniões para levantar requisitos.
- Definição das funcionalidades principais (leitura de extratos, geração de relatórios, criação de dashboards).
- Estabelecimento de prazos e cronograma do projeto.

### Resultados:

- Documento de Requisitos do Software (DRS).
- Especificação das funcionalidades e tecnologias a serem usadas.

#
<div align="center">

## Design do 

</div>

### Objetivo:

- Arquitetar a solução e definir a estrutura do código e da aplicação.

### Atividades:

- Design da arquitetura do sistema.
- Definição da estrutura de pastas e módulos.
- Escolha de bibliotecas e ferramentas.

### Resultados:

- Diagrama de arquitetura do sistema.
- Estrutura inicial do projeto (como a organização das pastas e arquivos).
<div align="center">

# Desenvolvimento

</div>

### Objetivo: 

- Implementar as funcionalidades definidas nos requisitos.

### Atividades:

- **Codificação das funcionalidades principais:**

- - Módulo de leitura de extratos bancários.
- - Funções para extração e análise de dados.
- - Geração de relatórios.
- - Criação de dashboards.
- - Integração de bibliotecas externas.

### Resultados:

- Módulos de código prontos (modulo.py e lib_ESW.py).
- Funcionalidades implementadas e testadas de forma individual.
<div align="center">

# Testes

</div>

### Objetivo: 

- Garantir que o sistema funciona conforme o esperado e sem erros.

### Atividades:

- Testes unitários das funções.
- Testes de integração para garantir que os módulos funcionam juntos.
- Testes de sistema para verificar a funcionalidade completa.

### Resultados:

- Relatórios de testes.
- Correções de bugs identificados.

<div align="center">

# Implantação

</div>

### Objetivo: 

- Disponibilizar o sistema para os usuários finais.

### Atividades:

- Preparação do ambiente de execução (Jupyter Notebook, instalação de bibliotecas).
- Entrega do projeto para avaliação ou uso.

### Resultados:

- Sistema pronto para uso ou avaliação.
- Documentação do projeto final.
<div align="center">

# Manutenção

</div>

### Objetivo: 

- Garantir a longevidade do sistema e fazer melhorias contínuas.

### Atividades:

- Correções de bugs após a entrega.
- Atualizações de funcionalidades com base em feedbacks.
- Adição de novas funcionalidades (opcional).

### Resultados:

- Versões atualizadas do sistema.

#
<div align="center">

# Processo de Desenvolvimento

</div>

### Iteração Inicial

- Começar com uma iteração curta para implementar as funcionalidades básicas, como a leitura de extratos e extração de dados.
- Focar em um protótipo funcional que permita a leitura de diferentes formatos de arquivos e a geração de relatórios simples.

### Desenvolvimento Incremental

- Adicionar novas funcionalidades em cada iteração:
- Implementação de relatórios mais detalhados.
- Desenvolvimento de dashboards interativos.
- Cada iteração deve incluir a fase de testes e integração dos novos módulos com os existentes.

### Revisões e Feedbacks

- Realizar revisões periódicas com o professor ou colegas para obter feedback sobre o progresso.
- Ajustar o desenvolvimento conforme o feedback recebido para garantir que o sistema atenda às expectativas.

### Entrega Final

- Consolidar todas as funcionalidades desenvolvidas.
- Realizar testes finais e preparar a documentação do projeto.
- Entregar o projeto dentro do prazo estabelecido.
<div align="center">

# Documento de Requisitos de Software (SRS)

</div>

 ### 1. Introdução

 Este documento descreve os requisitos funcionais e não funcionais para o sistema de leitura e processamento de arquivos PDF, extração e categorização de dados financeiros, e geração de relatórios e dashboards interativos.

 #### 1.1- Prioridade dos Requisitos

**A cada requisito será atribuída uma prioridade. A descrição de cada uma segueabaixo:**

 - Essencial: é um requisito imprescindível. Sem ele, o sistema não funcionará.
 - Importante: é um requisito que deve ser implementado, mas, se não for, o sistema funcionará do mesmo jeito, mas de maneira insatisfatória.
  - Desejável: é um requisito que trará um diferencial adicional ao sistema. Por isso, pode ser deixado para ser implementado por último ou em próximas iterações.

 ### 2. Requisitos Funcionais

 #### 2.1 Leitura de arquivos PDF

- ❖ Descrição: O sistema deve ser capaz de ler arquivos PDF em diversos formatos e extrair o conteúdo textual e estruturado necessário para análise.

- ❖ Requisitos:

   - ➢ [RF001] Suporte a arquivos PDF com diferentes estruturas (texto, tabelas, imagens).
   - ➢ [RF002] Capacidade de lidar com PDFs com diferentes versões e codificações.

- ❖ Prioridade: Essencial

- ❖ Critérios de Aceitação:

  - ➢ O sistema deve ser capaz de ler e extrair texto de pelo menos 95% dos arquivos PDF fornecidos.
  - ➢ Osistema deve detectar e relatar qualquer falha ao tentar ler um PDF não suportado.

 #### 2.2 Extração e categorização de dados financeiros

- ❖ Descrição: O sistema deve extrair dados financeiros relevantes dos arquivos PDF ecategorizá-los de acordo com critérios predefinidos.

 - ❖ Requisitos:

  - ➢ [RF003] Identificação e extração de dados como receitas, despesas, lucros e outros indicadores financeiros.
  - ➢ [RF004] Categorização dos dados de acordo com categorias financeiras específicas (ex.: receitas de vendas, custos operacionais).

- ❖ Prioridade: Essencial

- ❖ Critérios de Aceitação:

  - ➢ Os dados extraídos devem corresponder a pelo menos 98% das informações financeiras presentes nos PDFs.
  - ➢ Ascategorias devem estar alinhadas com as categorias predefinidas e ser ajustáveis conforme necessário.

 #### 2.3 Geração de relatórios financeiros detalhados

 - ❖ Descrição: O sistema deve gerar relatórios detalhados baseados nos dados financeiros extraídos e categorizados.

 - ❖ Requisitos:

   - ➢ [RF005] Relatórios devem incluir gráficos, tabelas e análises detalhadas.
   - ➢ [RF006] Relatórios devem ser exportados em formatos comuns (PDF, Excel, etc.).

 - ❖ Prioridade: Essencial

 - ❖ Critérios de Aceitação:

   - ➢ Os relatórios devem ser gerados com precisão e devem estar formatados corretamente.
   - ➢ Osistema deve permitir exportação em todos os formatos suportados sem perda de dados.

 #### 2.4 Criação de dashboards interativos

 - ❖ Descrição: O sistema deve criar dashboards interativos que permitam a visualização e análise dos dados financeiros extraídos.

 - ❖ Requisitos:

   - ➢ [RF007] Os Dashboards devem incluir gráficos interativos, filtros e opções de drill-down.
   - ➢ [RF008] Dashboards devem ser atualizados automaticamente com novos dados.

 - ❖ Prioridade: Importante

 - ❖ Critérios de Aceitação:

   - ➢ Dashboards devem ser responsivos e permitir a interação fluida com os dados.
   - ➢ Os dados exibidos nos dashboards devem estar atualizados e precisos.

 ### 3. Requisitos Não Funcionais

 #### 3.1 Desempenho eficiente na leitura e processamento dos 

 - ❖ Descrição: O sistema deve processar arquivos PDF de forma eficiente, sem a especificação de tempo ou tamanho de arquivo.

 - ❖ Requisitos:

   - ➢ [NF001] O sistema deve suportar a leitura e processamento simultâneo de múltiplos arquivos PDF.

 - ❖ Prioridade: Essencial

 - ❖ Critérios de Aceitação:

   - ➢ Osistema deve manter desempenho consistente sob carga elevada.

 #### 3.2 Interface intuitiva para geração e visualização de relatórios

 - ❖ Descrição: O sistema deve ter uma interface de usuário intuitiva que facilite a geração e visualização de relatórios e dashboards.

 - ❖ Requisitos:

   - ➢ [NF003] A interface deve ser fácil de usar e navegar.
   - ➢ [NF004] As funcionalidades principais devem ser acessíveis em no máximo três cliques.

 - ❖ Prioridade: Importante

 - ❖ Critérios de Aceitação:

   - ➢ Usuários devem ser capazes de gerar e visualizar relatórios e dashboards com facilidade.

   - ➢ Feedback dos usuários deve indicar uma alta taxa de satisfação com a interface.

 #### 3.3 Compatibilidade com ferramentas de visualização de dados como Power BI ou Looker Studio

 - ❖ Descrição: O sistema deve ser compatível com ferramentas de visualização de dados como Power BI e Looker Studio.

 - ❖ Requisitos:

   - ➢ [NF005] Exportação de dados deve ser compatível com formatos suportados por essas ferramentas.
   - ➢ [NF006] Deve haver integração ou opções de exportação direta para essas ferramentas.

 - ❖ Prioridade: Importante

 - ❖ Critérios de Aceitação:

   - ➢ Dados exportados devem ser corretamente importados e visualizados nas ferramentas mencionadas.

   - ➢ Aintegração deve funcionar sem erros significativos. Resumo Financeiro

# Entradas (Receitas)

 - ❖ 06/11/2018- Recebimento de ICMS

   - ➢ Valor: R$ 3.372.304,31
   - ➢ Categoria: 
   
 - ❖ 06/11/2018- Crédito FPM

   - ➢ Valor: R$ 300.000,00
   - ➢ Categoria: Receita

 - ❖ 06/11/2018- Crédito FPE

   - ➢ Valor: R$ 450.000,00
   - ➢ Categoria: Receita Saídas (Despesas)

 - ❖ 07/11/2018- Pagamento de Fornecedores

   - ➢ Valor: R$ 1.000.000,00
   - ➢ Categoria: 
   
 - ❖ 07/11/2018- Transferência para Contas Diversas

   - ➢ Valor: R$ 500.000,00
   - ➢ Categoria: Diversos

 - ❖ 08/11/2018- Pagamento de Folha de Pagamento

   - ➢ Valor: R$ 850.000,00
   - ➢ Categoria: Salários Saldos

 - ● Saldo Inicial em 06/11/2018: R$ 0,00
 - ● Entradas Totais: R$ 4.122.304,31
 - ● Saídas Totais: R$ 2.350.000,00
 - ● Saldo Final em 08/11/2018: R$ 1.772.304,31 Categorias de Gastos

 - ❖ Receitas

   - ➢ FPM
   - ➢ FPE
   - ➢ ICMS

 - ❖ Despesas

   - ➢ Diversos (Pagamento de fornecedores e transferências)
   - ➢ Salários (Folha de pagamento) Observações

 - ● Todas as transações estão datadas de novembro de 2018.
 - ● Asreceitas são principalmente de repasses de ICMS, FPM e FPE.
 - ● Asdespesas incluem pagamentos a fornecedores, transferências diversas, e folha de pagamento.

 Este relatório foi gerado com base nos dados disponíveis no extrato. Caso deseje informações mais detalhadas ou alguma modificação, sinta-se à vontade para pedir! Geração de Relatórios Detalhados Objetivo: Fornecer uma visão simples e clara dos valores pagos e recebidos.
<div align="center">

 # Estrutura da Tabela

</div>

 - ● Colunas:

 1. NomedaTransação: Descrição básica (ex.: "Recebimento de ICMS").
 2. Tipo: Entrada ou Saída.
 3. Valor: Valor monetário da transação.
 4. Descrição: Breve descrição do que foi pago ou recebido (opcional).
