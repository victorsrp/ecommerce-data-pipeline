# Ecommerce Data Pipeline  

## Descrição  
Projeto de pipeline de dados para e-commerce. O objetivo é extrair, transformar e carregar dados de diferentes fontes, armazenando-os de forma organizada e testável.  

Este repositório contém a **estrutura inicial** do projeto, incluindo pastas, scripts skeleton, testes iniciais e documentação básica.  

---

## Estrutura do Projeto  
```
ecommerce-data-pipeline/
│
├── data/
│ ├── raw/ # Dados brutos
│ └── processed/ # Dados processados
│
├── scripts/ # Scripts Python para processamento de dados
│ └── generate_and_upload.py
│
├── tests/ # Testes unitários
│ └── test_generate.py
│
├── docs/ # Documentação adicional
├── requirements.txt # Dependências Python
├── README.md
└── .gitignore
```
---

## Setup do Ambiente  

1. Crie e ative o ambiente virtual:  

**Windows (Git Bash / WSL / Linux):**
```bash
python -m venv venv
source venv/Scripts/activate

Instale as dependências:
pip install -r requirements.txt
```  
---

## Dependências principais  

-pandas → manipulação de dados  
-boto3 → integração com AWS S3  
-faker → geração de dados fictícios para testes  

---

## Controle de Versão  

Este projeto segue Conventional Commits:  
-chore: → tarefas de manutenção e setup  
-feat: → novas funcionalidades  
-fix: → correção de bugs  
-docs: → alterações na documentação  
-refactor: → refatoração de código  

---

## Próximos Passos

Desenvolver os scripts de ingestão e processamento de dados  
Implementar testes unitários completos  
Criar pipeline automatizada (ETL/ELT)  

---

## Licença  

Projeto licenciado sob a MIT License