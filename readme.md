# O Rifas no back

### Sumário
- [O que é?](#o-que-é)
- [Como funciona?](#como-funciona)
- [Como rodar?](#como-rodar)
- [Como contribuir?](#como-contribuir)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Autores](#autores)

## O que é?
O Rifas no back é uma API REST que tem como objetivo gerenciar rifas, sorteios e usuários. A API foi desenvolvida utilizando o microframework Flask consumindo dados de uma tabela Google Sheets. A API foi desenvolvida para ser consumida pelo [Rifas no front](https://github.com/MateusSantosMeuBem/o_rifas_back_front).

## Como funciona?
A API é composta por 2 endpoints:
- **/numbers**: endpoint reponsável por trazer uma lista do tipo:
    ```
    [
        {
            "number": "string",
            "sold": "string"
        }
    ]
    ```
    referente a todos os números da rifa.
- **/numbers/<seller_name>**: endpoint reponsável por trazer um json do tipo:
    ```
    {
        "contact": "string",
        "sold_numbers": 0,
        "avaiable_numbers": 0,
        "numbers": [
            {
            "number": "string",
            "sold": "string"
            }
        ],
        "seller_name": "string",
        "pix": "string"
    }
    ```
    referente a todos os números da rifa de um vendedor específico.

## Como rodar?
Para rodar a API é necessário ter o Python 3.9 ou superior instalado na máquina. Após isso, basta clonar o repositório, criar um ambiente virtual e instalar as dependências do projeto. Para isso, basta rodar os seguintes comandos:

Para clonar
```
git clone git@github.com:MateusSantosMeuBem/o_rifas_back_end.git
```
Para criar o ambiente virtual e instalar as dependências
```
cd o_rifas_back_end
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Faça uma cópia do arquivo `.env.example` e renomeie para `.env`. Após isso, adicione as credenciais da sua conta Google Sheets no arquivo .env. Como segue o exemplo:
```
SHEET_ID=chave_da_api
SHEET_NAME=id_da_planilha
```

Faça uma cópia do arquivo `o_rifas_back/src/sellers.example.json` e renomeie para `sellers.json`. Após isso, adicione os vendedores da rifa no arquivo `sellers.json`. Como segue o exemplo:
```
[
    "julia": {
        "first_number": 1,
        "last_number": 50,
        "pix": "11934543265",
        "contact": "emaildajulia@correio.com"
    }
]
````

Após isso, basta rodar o comando:
```
flask run
```

O projeto também está configurado para rodar utilizando o Docker.

Obs: Caso vá subir o projeto pra produção, não esqueça de verificar os arquivos `sellers.json` e `.env` no `.gitignore`.

## Como contribuir?
Para contribuir com o projeto, basta seguir os seguintes passos:
- Faça um fork do projeto
- Crie uma branch com a sua feature
- Faça um commit com suas mudanças
- Faça um push para a sua branch
- Abra um Pull Request

## Tecnologias utilizadas
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Docker](https://www.docker.com/)
- [Google Sheets](https://www.google.com/intl/pt-BR/sheets/about/)

## Autores
- [Elian Batista](https://github.com/Elian-beep)
- [Mateus Santos](https://github.com/MateusSantosMeuBem)

