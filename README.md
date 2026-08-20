# BarberPy

Sistema web de **agendamento para barbearia**, desenvolvido com **Python e Django** como projeto de estudos em desenvolvimento web.

A aplicação foi criada com o objetivo de praticar o desenvolvimento de sistemas utilizando Django, trabalhando com autenticação de usuários, modelos relacionais, formulários, templates, operações CRUD e gerenciamento de agendamentos.

> ⚠️ **Status:** projeto descontinuado. O desenvolvimento foi interrompido antes da conclusão de todas as funcionalidades planejadas.

---

## 📚 Sobre o projeto

O BarberPy foi idealizado como uma plataforma para gerenciamento de agendamentos de uma barbearia.

A proposta era permitir que o usuário percorresse um fluxo semelhante a:

```text
Login
  ↓
Seleção da unidade
  ↓
Seleção do serviço
  ↓
Seleção do barbeiro
  ↓
Seleção da data
  ↓
Agendamento
  ↓
Visualização dos agendamentos
  ↓
Cancelamento
```

O projeto utiliza o padrão arquitetural do Django, separando funcionalidades em aplicações específicas.

---

# 🎯 Objetivo

O principal objetivo do projeto foi praticar o desenvolvimento de uma aplicação web utilizando Django e consolidar conceitos como:

* Python;
* Django;
* Model-View-Template;
* ORM do Django;
* Modelos e relacionamentos;
* Views;
* Templates;
* Formulários;
* Autenticação;
* CRUD;
* Banco de dados SQLite;
* Estrutura modular de aplicações Django;
* Organização de arquivos estáticos.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia       | Utilização                                  |
| ---------------- | ------------------------------------------- |
| Python           | Linguagem principal                         |
| Django           | Framework web                               |
| SQLite           | Banco de dados utilizado no desenvolvimento |
| HTML             | Estrutura das páginas                       |
| CSS              | Estilização                                 |
| Django Templates | Renderização das páginas                    |
| Django ORM       | Persistência e consultas ao banco           |
| Git              | Versionamento                               |

O repositório possui `requirements.txt`, `manage.py`, banco SQLite e aplicações Django separadas por domínio.

---

# 🏗️ Estrutura do projeto

A estrutura atual do repositório é organizada em aplicações Django:

```text id="7g4w9m"
BarberPy/
│
├── agendamentos/
│   ├── ...
│   └──
│
├── usuarios/
│   ├── ...
│   └──
│
├── core/
│   ├── ...
│   └──
│
├── config/
│   ├── ...
│   └──
│
├── static/
│   └── css/
│
├── templates/
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── .gitignore
```

O repositório atualmente contém os módulos `agendamentos`, `usuarios` e `core`, além das configurações do projeto, templates e arquivos estáticos.

---

# 🧩 Organização da aplicação

## `usuarios`

Aplicação responsável pelas funcionalidades relacionadas aos usuários.

O módulo foi criado para concentrar recursos relacionados à autenticação e ao acesso dos usuários ao sistema.

O fluxo de utilização do sistema parte da identificação do usuário antes do acesso às funcionalidades de agendamento.

---

## `agendamentos`

Aplicação responsável pelo domínio principal do projeto: os agendamentos.

A proposta desse módulo é centralizar as informações relacionadas à:

* Unidade;
* Serviço;
* Barbeiro;
* Data;
* Horário;
* Agendamento;
* Consulta dos agendamentos;
* Cancelamento.

---

## `core`

Módulo utilizado para funcionalidades e estruturas compartilhadas pelo projeto.

A separação desse código em um módulo próprio permite evitar que funcionalidades comuns fiquem diretamente acopladas às aplicações específicas.

---

# 🗄️ Banco de dados

Durante o desenvolvimento foi utilizado **SQLite**, através do arquivo:

```text id="xjymq2"
db.sqlite3
```

O Django ORM é responsável pela comunicação entre os modelos da aplicação e o banco de dados.

O SQLite foi utilizado como solução simples para o ambiente de desenvolvimento, sem necessidade de configurar um servidor de banco de dados externo.

---

# 🔄 Django ORM

Uma das principais funcionalidades praticadas no projeto foi o **Object-Relational Mapping (ORM) do Django**.

Através do ORM, os modelos Python representam as estruturas persistidas no banco de dados.

O fluxo pode ser representado como:

```text id="tq6f0b"
Model Django
     ↓
Django ORM
     ↓
SQLite
```

Isso permite realizar operações de criação, consulta, atualização e exclusão utilizando as abstrações fornecidas pelo Django.

---

# 📅 Fluxo de agendamento

A principal funcionalidade planejada para o sistema é o gerenciamento de agendamentos.

O fluxo pensado para o usuário é:

### 1. Autenticação

O usuário acessa o sistema através da tela de login.

### 2. Unidade

Após o acesso, o usuário seleciona a unidade da barbearia desejada.

### 3. Serviço

Em seguida, seleciona o serviço que deseja realizar.

### 4. Barbeiro

O sistema apresenta os barbeiros disponíveis para o serviço selecionado.

### 5. Data

O usuário escolhe a data desejada.

### 6. Agendamento

Com as informações selecionadas, o agendamento é criado.

### 7. Gerenciamento

O usuário pode visualizar seus agendamentos e, quando disponível, realizar o cancelamento.

---

# 🖥️ Interface

A aplicação utiliza:

```text id="hqu2x1"
Django Templates
      +
HTML
      +
CSS
```

Os templates são armazenados no diretório:

```text id="jd4j7f"
templates/
```

e os arquivos CSS estão organizados em:

```text id="3i9m7d"
static/css/
```

Essa estrutura segue o modelo tradicional de aplicações web renderizadas pelo Django.

---

# ⚙️ Como executar

## Pré-requisitos

Tenha instalado:

* Python;
* pip;
* Git.

---

## 1. Clone o repositório

```bash id="r7m2cy"
git clone https://github.com/gustavoconce/BarberPy.git
```

Entre na pasta:

```bash id="2w6n8c"
cd BarberPy
```

---

## 2. Crie um ambiente virtual

### Windows

```bash id="f5r9za"
python -m venv venv
```

Ative:

```bash id="zv3gk8"
venv\Scripts\activate
```

### Linux / macOS

```bash id="0a2l2h"
python3 -m venv venv
```

Ative:

```bash id="7a8f9m"
source venv/bin/activate
```

---

## 3. Instale as dependências

```bash id="2s3x8j"
pip install -r requirements.txt
```

---

## 4. Execute as migrações

```bash id="5h2b7f"
python manage.py migrate
```

---

## 5. Inicie o servidor

```bash id="9k6s3p"
python manage.py runserver
```

A aplicação estará disponível em:

```text id="g0c8y1"
http://127.0.0.1:8000/
```

---

# 🧪 Status atual

O projeto encontra-se **descontinuado**.

O desenvolvimento foi interrompido antes da implementação completa de todas as funcionalidades planejadas.

### Implementado / iniciado

* [x] Estrutura inicial do projeto Django
* [x] Separação em aplicações Django
* [x] Configuração do banco SQLite
* [x] Estrutura de usuários
* [x] Estrutura de agendamentos
* [x] Templates HTML
* [x] Arquivos CSS
* [x] Configuração inicial do ORM

### Não concluído

* [ ] Finalização completa do fluxo de agendamento
* [ ] Integração completa entre unidade, serviço e barbeiro
* [ ] Gerenciamento completo dos horários disponíveis
* [ ] Finalização das regras de negócio
* [ ] Testes automatizados
* [ ] Deploy
* [ ] Documentação completa da aplicação

---

# 📚 Conceitos praticados

Durante o desenvolvimento foram trabalhados conceitos como:

* Python;
* Django;
* Django ORM;
* Models;
* Views;
* Templates;
* URL Routing;
* Forms;
* Autenticação;
* CRUD;
* SQLite;
* Relacionamentos entre modelos;
* Arquivos estáticos;
* Estrutura modular de aplicações Django.

---

# 🚧 Possíveis evoluções

Caso o desenvolvimento seja retomado, algumas evoluções naturais seriam:

* [ ] Finalizar o fluxo de agendamento;
* [ ] Criar painel administrativo;
* [ ] Gerenciar unidades;
* [ ] Gerenciar serviços;
* [ ] Gerenciar barbeiros;
* [ ] Controle de disponibilidade;
* [ ] Impedir conflitos de horários;
* [ ] Histórico de agendamentos;
* [ ] Cancelamento de agendamentos;
* [ ] Melhorar autenticação e autorização;
* [ ] Adicionar testes automatizados;
* [ ] Migrar para PostgreSQL;
* [ ] Criar API REST com Django REST Framework;
* [ ] Containerizar com Docker;
* [ ] Realizar deploy.

---

# 🎓 Contexto do projeto

O BarberPy foi desenvolvido como projeto de estudos para praticar **Python e Django**, utilizando um problema realista — gerenciamento de uma barbearia — como domínio da aplicação.

Apesar de não ter sido finalizado, o projeto representa uma etapa importante de aprendizado sobre desenvolvimento web com Django e organização de aplicações utilizando o padrão MVT.

---

# 📌 Status

**Projeto descontinuado / estudo**

O código permanece disponível no GitHub como registro do desenvolvimento e dos conceitos estudados.

---

# 👨‍💻 Autor

**Gustavo Conceição**

Graduado em Sistemas de Informação pela FIAP, com interesse em desenvolvimento backend e construção de aplicações web utilizando Python, Django, Java e Spring Boot.

[GitHub](https://github.com/gustavoconce)

[LinkedIn](https://www.linkedin.com/in/gustavoconce/)
