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

# **Projeto de Engenharia de Software - Análise de Extratos Bancários**

</div>

# **VISÃO DE NEGÓCIO**



## 1. Finalidade

Este documento tem o propósito de fornecer uma visão global acerca da solução a ser adotada na aplicação.

## 2. Descrição do Negócio
Este projeto foi desenvolvido para a disciplina de Engenharia de Software na Universidade Federal da Paraíba. O objetivo da solução é criar uma ferramenta que leia extratos bancários mensais, fornecendo relatórios detalhados através de dashboards interativos dos rendimentos e despesas utilizando como entrada extratos bancários de qualquer instituição, mas com o padrão de formato PDF.

## 3. Atividades e Processos de Negócio
<div align="center">

<img src="diagrama.png" alt="Alt Text" width="1000"/>

</div>

## 4. Oportunidade de Negócios
Considerando o desafio de integração entre os dados do fluxo bancários em diferentes de instituições financeiras, a pluralidade e maneiras particulares de expor os extratos bancários ao cliente, a nossa aplicação visa estabelecer um canal de análise base, para mesclar e fornecer as principais interações estatísticas através dashboards interativos independente da quantidade extratos bancários fornecidos e de sua instituição de origem.

<div align="center">

</div>

## 5. Funcionalidades

- Leitura de extratos bancários em diversos formatos (PDF).
- Extração de dados relevantes como despesas, receitas, saldos e categorias de gastos.
- Geração de relatórios detalhados sobre despesas e rendimentos.
- Criação de dashboards interativos para visualização e análise dos dados financeiros.

## 6. Tecnologias Utilizadas

- **Linguagem de Programação**: Python

- **Bibliotecas**: Pandas, Matplotlib, Seaborn, Plotly, Dash, loguru, openpyxl, os, tabula, PyPDF2

## 7. Estrutura do Projeto

PROJETO-ESW

      ├── modulo/
      |   |
      │   ├── modulo.py - Código principal do projeto
      |   |
      │   ├── lib_ESW.py - Arquivo contendo funções utilizadas no projeto.
      |   |
      │   ├── extrato.pdf - Base de dados.
      |   |
      │   ├── extrato.xlsx - Relatórios extraido do pdf para tratamento.
      |   |
      │   ├── ExtratoLimpo.xlsx - Relatório para entrega ao cliente e conecção com o Power BI
      |   |
      │   ├── logfile.txt - Logs para analise de funcionamento do sistema
      |   |
      │   ├── DashBoard - Dashboards criados para visualização - integração com power BI            
      |
      ├── teste
      |   |
      │   ├── lib_ESW.py
      |   |
      │   ├── test_lib.py


# 
<div align="center">

# **CICLO DE VIDA DO PROJETO**

</div>

## 1. Planejamento e Definição de Requisitos

### 1.1. Objetivo:

- Entender as necessidades dos usuários e definir os requisitos funcionais e não funcionais do sistema.

### 1.2. Atividades:

- Reuniões para levantar requisitos.
- Definição das funcionalidades principais (leitura de extratos, geração de relatórios, criação de dashboards).
- Estabelecimento de prazos e cronograma do projeto.

### 1.3. Resultados:

- Documento de Requisitos do Software (DRS).
- Especificação das funcionalidades e tecnologias a serem usadas.

## 2. Design do projeto

### 2.1. Objetivo:

- Arquitetar a solução e definir a estrutura do código e da aplicação.

### 2.2. Atividades:

- Design da arquitetura do sistema.
- Definição da estrutura de pastas e módulos.
- Escolha de bibliotecas e ferramentas.

### 2.3. Resultados:

- Diagrama de arquitetura do sistema.
- Estrutura inicial do projeto (como a organização das pastas e arquivos).

## 3. Desenvolvimento

### 3.1. Objetivo: 

- Implementar as funcionalidades definidas nos requisitos.

### 3.22 Atividades:

- **Codificação das funcionalidades principais:**

- - Módulo de leitura de extratos bancários.
- - Funções para extração e análise de dados.
- - Geração de relatórios.
- - Criação de dashboards.
- - Integração de bibliotecas externas.

### 3.3. Resultados:

- Módulos de código prontos (modulo.py e lib_ESW.py).
- Funcionalidades implementadas e testadas de forma individual.

## 4. Testes

### 4.1. Objetivo: 

- Garantir que o sistema funciona conforme o esperado e sem erros.

### 4.2. Atividades:

- Testes unitários das funções.
- Testes de integração para garantir que os módulos funcionam juntos.
- Testes de sistema para verificar a funcionalidade completa.

### 4.3. Resultados:

- Relatórios de testes.
- Correções de bugs identificados.

## 5. ImplantaçãoO

### 5.1. Objetivo: 

- Disponibilizar o sistema para os usuários finais.

### 5.2. Atividades:

- Preparação do ambiente de execução (Jupyter Notebook, instalação de bibliotecas).
- Entrega do projeto para avaliação ou uso.

### 5.3. Resultados:

- Sistema pronto para uso ou avaliação.
- Documentação do projeto final.

## 6. Manutenção

### 6.1. Objetivo: 

- Garantir a longevidade do sistema e fazer melhorias contínuas.

### 6.2. Atividades:

- Correções de bugs após a entrega.
- Atualizações de funcionalidades com base em feedbacks.
- Adição de novas funcionalidades (opcional).

### 6.3. Resultados:

- Versões atualizadas do sistema.

#
<div align="center">

# **PROCESSO DE DESENVOLVIMENTO**

</div>

## Metodologia de Desenvolvimento

- Começar com uma iteração curta para implementar as funcionalidades básicas, como a leitura de extratos e extração de dados.
- Focar em um protótipo funcional que permita a leitura de diferentes formatos de arquivos e a geração de relatórios simples.
- Adicionar novas funcionalidades em cada iteração:
- Implementação de relatórios mais detalhados.
- Desenvolvimento de dashboards interativos.
- Cada iteração deve incluir a fase de testes e integração dos novos módulos com os existentes.

## Revisões e Feedbacks

- Realizar revisões periódicas com o professor ou colegas para obter feedback sobre o progresso.
- Ajustar o desenvolvimento conforme o feedback recebido para garantir que o sistema atenda às expectativas.

## Entrega Final

- Consolidar todas as funcionalidades desenvolvidas.
- Realizar testes finais e preparar a documentação do projeto.
- Entregar o projeto dentro do prazo estabelecido.

#
<div align="center">

# **DOCUMENTAÇÃO DE REQUISITOS DE SOFTWARE (SRS)**

</div>

 ## Introdução

 Este documento descreve os requisitos funcionais e não funcionais para o sistema de leitura e processamento de arquivos PDF, extração e categorização de dados financeiros, e geração de relatórios e dashboards interativos.

 ### Prioridade dos Requisitos

A cada requisito será atribuída uma prioridade. A descrição de cada uma segueabaixo:**

 - Essencial: é um requisito imprescindível. Sem ele, o sistema não funcionará.
 - Importante: é um requisito que deve ser implementado, mas, se não for, o sistema funcionará do mesmo jeito, mas de maneira insatisfatória.
  - Desejável: é um requisito que trará um diferencial adicional ao sistema. Por isso, pode ser deixado para ser implementado por último ou em próximas iterações.

 ## Requisitos Funcionais

 ### Leitura de arquivos PDF

- ❖ Descrição: O sistema deve ser capaz de ler arquivos PDF em diversos formatos e extrair o conteúdo textual e estruturado necessário para análise.

- ❖ Requisitos:

   - ➢ [RF001] Suporte a arquivos PDF com diferentes estruturas (texto, tabelas, imagens).
   - ➢ [RF002] Capacidade de lidar com PDFs com diferentes versões e codificações.

- ❖ Prioridade: Essencial

- ❖ Critérios de Aceitação:

  - ➢ O sistema deve ser capaz de ler e extrair texto de pelo menos 95% dos arquivos PDF fornecidos.
  - ➢ Os istema deve detectar e relatar qualquer falha ao tentar ler um PDF não suportado.

 ### Extração e categorização de dados financeiros

- ❖ Descrição: O sistema deve extrair dados financeiros relevantes dos arquivos PDF ecategorizá-los de acordo com critérios predefinidos.

 - ❖ Requisitos:

  - ➢ [RF003] Identificação e extração de dados como receitas, despesas, lucros e outros indicadores financeiros.
  - ➢ [RF004] Categorização dos dados de acordo com categorias financeiras específicas (ex.: receitas de vendas, custos operacionais).

- ❖ Prioridade: Essencial

- ❖ Critérios de Aceitação:

  - ➢ Os dados extraídos devem corresponder a pelo menos 98% das informações financeiras presentes nos PDFs.
  - ➢ Ascategorias devem estar alinhadas com as categorias predefinidas e ser ajustáveis conforme necessário.

 ### Geração de relatórios financeiros detalhados

 - ❖ Descrição: O sistema deve gerar relatórios detalhados baseados nos dados financeiros extraídos e categorizados.

 - ❖ Requisitos:

   - ➢ [RF005] Relatórios devem incluir gráficos, tabelas e análises detalhadas.
   - ➢ [RF006] Relatórios devem ser exportados em formatos comuns (PDF, Excel, etc.).

 - ❖ Prioridade: Essencial

 - ❖ Critérios de Aceitação:

   - ➢ Os relatórios devem ser gerados com precisão e devem estar formatados corretamente.
   - ➢ Os istema deve permitir exportação em todos os formatos suportados sem perda de dados.

 ### Criação de dashboards interativos

 - ❖ Descrição: O sistema deve criar dashboards interativos que permitam a visualização e análise dos dados financeiros extraídos.

 - ❖ Requisitos:

   - ➢ [RF007] Os Dashboards devem incluir gráficos interativos, filtros e opções de drill-down.
   - ➢ [RF008] Dashboards devem ser atualizados automaticamente com novos dados.

 - ❖ Prioridade: Importante

 - ❖ Critérios de Aceitação:

   - ➢ Dashboards devem ser responsivos e permitir a interação fluida com os dados.
   - ➢ Os dados exibidos nos dashboards devem estar atualizados e precisos.
#

<div align="center">

# **2° ENTREGA**

</div>


 ## Requisitos Não Funcionais


                                  +---------------------------------------------------------+     
                                  | 1. Desempenho na Leitura e Processamento de Arquivos PDF|
                                  +---------------------------------------------------------+
                                                |                                   |                       
                                  +-----------[NF001]-----------+   +-------------[NF002]-------------+
                                  |   O sistema deve suportar   |   |   Eficiência sem especificação  |
                                  | a leitura e processamento   |   | de tempo ou tamanho.            |
                                  | simultâneo de múltiplos     |   |                                 |
                                  | arquivos PDF.               |   |                                 |
                                  +-----------------------------+   +---------------------------------+
                                                  |       
                                  +---------------------------------+
                                  |   Critério: Desempenho          |
                                  | consistente sob carga elevada.  |
                                  +---------------------------------+
#

                                  +-----------------------------------------------------------+
                                  | 2. Interface Intuitiva para Relatórios e Dashboards       |
                                  +-----------------------------------------------------------+
                                                |                                   |                       
                                  +-----------[NF003]-----------+   +-------------[NF004]-------------+
                                  |   A interface deve ser      |   |   Funcionalidades principais    |
                                  | fácil de usar e navegar.    |   | acessíveis em no máximo três    |
                                  |                             |   | cliques.                        |
                                  +-----------------------------+   +---------------------------------+
                                                |                                  |
                            +------------------------------------+   +------------------------------------+
                            |   Critério: Geração e visualização |   |   Critério: Alta satisfação dos    |
                            | de relatórios com facilidade.      |   | usuários com a interface.          |
                            +------------------------------------+   +------------------------------------+
#

                                  +---------------------------------------------------------------+
                                  | 3. Compatibilidade com Ferramentas de Visualização de Dados   |
                                  +---------------------------------------------------------------+
                                                |                                    |
                                  +-----------[NF005]-----------+   +-------------[NF006]-------------+
                                  |   Exportação compatível     |   |   Integração ou exportação      |
                                  | com Power BI, Looker Studio.|   | direta sem erros significativos.|
                                  |                             |   |                                 |
                                  +-----------------------------+   +---------------------------------+
                                                |                                  |
                            +------------------------------------+   +------------------------------------+
                            |   Critério: Dados corretamente     |   |   Critério: Funcionamento sem      |
                            | importados nas ferramentas.        |   | erros significativos.              |
                            +------------------------------------+   +------------------------------------+
#
<div align="center">

 # **PLANEJAMENTO DE TESTES**

</div>


                                                        +-------------------------+
                                                        |  Planejamento de Testes |
                                                        +-------------------------+
                                                                    |
                                                          +----------+----------+
                                                          |                     |
                                                      +--v--+         +--------v--+----+      
                                                      |Fluxo|         |Tecnologia Usada|
                                                      +-----+         +----------------+
                                                        |                      |
                                                        v                      v
                                                +----------------+      +--------------------------+
                                                | Identificar    |      | Ferramenta de Automação  |
                                                | Requisitos     |      | de Testes                |
                                                +----------------+      +--------------------------+
                                                          |                       |
                                                  +-------v----------+   +--------------------+
                                                  | Definir Critérios|   | Framework de Teste:|
                                                  | de Aceitação     |   | unittest           |
                                                  +------------------+   +--------------------+
                                                          |                 |
                                                  +-------v-------+     +---------------------+
                                                  | Criar Casos   |     | Sistema de Controle |
                                                  | de Teste      |     | de Versão: GitHub   |
                                                  +---------------+     +---------------------+
                                                          |             
                                                  +-------v--------+     
                                                  | Executar Testes|     
                                                  +----------------+    
                                                          |             
                                                  +-------v-------+
                                                  | Registrar     |
                                                  | Resultados    |
                                                  +---------------+
                                                          |
                                                  +------v---------+
                                                  |   Resultados   |
                                                  +----------------+
                                                          |
                                                  +------v----------------------------+
                                                  | Resultados Esperados vs Reais     |
                                                  +-----------------------------------+
                                                          |
                                                  +------v----------------------------+
                                                  | Registro de Defeitos              |
                                                  +-----------------------------------+
                                                          |
                                                  +------v----------------------------+
                                                  | Relatório de Execução de Testes   |
                                                  +-----------------------------------+
<div align="center">

[Modelo de testes](test_lib.py) 

[Base de teste](lib_ESW.py)

[Logs de testes](logfile.txt)

</div>

#
<div align="center">

# **INTERFACE COM POWER BI**
[Click aqui para abrir o DashBoard](https://app.powerbi.com/view?r=eyJrIjoiYTM0ODdlN2UtNzgwMC00NjA2LWEzY2UtZmI0YmRiNWI4OTM2IiwidCI6ImJmN2UwZjYwLTVhMjktNDk4Ny1iNzA5LWYxYWIyODhmNjM4NSJ9)
## Conectar-se a dados no Power BI – documentação



A documentação do Power BI fornece informações de especialistas para conectar-se a dados com ferramentas como gateways aplicativos de modelo e atualização de dados.

[Conectar-se a dados no Power BI – documentação](power-bi-connect-data.pdf)
#
</div>