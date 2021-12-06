<p align="center">
  <a href="https://www.denox.com.br/" rel="noopener">
 <img width=200px height=200px src="https://svgur.com/i/cZz.svg" alt="logo"></a>
</p>

<div align="center">

[![Status](https://img.shields.io/badge/status-ativo-success.svg)]()
[![LinkedIn](https://img.shields.io/badge/platform-linkedin-blue.svg)](https://www.linkedin.com/in/icaroparanhos/)
</div>

---

## 📝 Tabela de conteúdos

- [Sobre](#about)
- [Requisitos para rodar o projeto](#developmentrequirements)
- [Instalação](#installation)
- [Rotas da API](#routesapi)
- [Observações](#comments)

## 🧐 Sobre <a name="about"></a>

Projeto desenvolvido como parte de um processo seletivo da empresa [Denox](https://www.denox.com.br/). Nesse projeto foi desenvolvido uma API usando [Tornado](https://www.tornadoweb.org/en/stable/) onde tem a função de calcular a distância percorrida, o tempo em movimento, o tempo parado e os centroides das posições paradas de um veiculo rastreado.

## 📝 Requisitos para rodar o projeto <a name="developmentrequirements"></a>

- Python3
- Docker
- Docker Compose

## 💭 Instalação <a name="installation"></a>

1.Instale o Docker seguindo o tutorial a seguir:
https://docs.docker.com/engine/install/ubuntu/

2.Instale o Docker Compose seguindo o tutorial a seguir: https://docs.docker.com/compose/install/

3.Clone este repositório usando o seguinte comando:
```terminal
$ git clone git@github.com:smookeydev/denox-api.git
```
4.Acesse a pasta do projeto em seu terminal:
```terminal
$ cd denox-api
```
5.Rode o comando de instalação das bibliotecas utilizada no projeto.
```terminal
$ pip3 install -r requirements.txt
```

6.Copie o arquivo de configuração de exemplo para um arquivo de configuração real:
```terminal
$ cp .env.example .env
```
7.Troque os valores existentes no arquivo de configuração, os valores são:
  * **DB_HOST**: Endereço IPV4 a ser utilizado para conexão do banco de dados. (Opcional)
  * **DB_PORT**: Porta que será usada para o banco de dados. (Opcional)
  * **DB_NAME**: Nome do banco de dados. (Opcional)
  * **DB_USER**: Usuário do banco de dados. (Obrigatório)
  * **DB_PASS**: Senha do usuário do banco de dados. (Obrigatório)

8.Inicie o banco de dados rodando o seguinte comando:
```terminal
$ make up
```
9.Inicie a API rodando o seguinte comando:
```terminal
$ python3 main.py
```

## 📲 Rotas da API <a name="routesapi"></a>

| Método  | Rota | Argumentos |
| ------------- | ------------- | ------------- |
| POST | /api/calcula_metricas  |  { "serial": "", "datahora_inicio": "", "datahora_fim": "" }  |
| GET | /api/retorna_metricas |  |

---

## 🔰 Observações <a name="comments"></a>

- Comentei grande parte do código, para fácil entendimento de quem for analisar.

- Efetuei um pequeno tratamento no banco de dados, já que todos os dados estavam formatados como string.

- Nesse repositorio existe um arquivo chamado denox-api.json, que é um documento exportado do [Insomnia](https://insomnia.rest/download) com as rotas da API e dados de exemplo.