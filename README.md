# 🐍 Exercícios de Programação Orientada a Objetos com Python

Este repositório contém exercícios práticos de Programação Orientada a Objetos (POO) utilizando Python.

O objetivo do projeto é praticar desde conceitos básicos até estruturas mais profissionais de desenvolvimento de software.

---

# 🚀 Tecnologias Utilizadas

- Python 3.x
- UV
- Poe the Poet

---

# 📦 Gestão de Ambiente e Dependências

O projeto utiliza:

```bash
uv
```

para:

- gestão de dependências
- criação de ambiente virtual
- sincronização de pacotes
- execução de scripts

Documentação oficial:

[UV Python Package Manager](https://docs.astral.sh/uv/?utm_source=chatgpt.com)

---

# 🛠 Dependências de Desenvolvimento

Instalação do Poe the Poet:

```bash
uv add --dev poethepoet
```

Documentação oficial:

[Poe the Poet](https://poethepoet.natn.io/?utm_source=chatgpt.com)

---

# ⚙️ Configuração do Projeto

## Criar ambiente virtual

```bash
uv venv
```

---

## Ativar ambiente virtual

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## Instalar dependências

```bash
uv sync
```

---

# 🧰 Tarefas Configuradas no pyproject.toml

```toml
[tool.poe.tasks]
uvrm = "uv run main.py"
```

---

# ▶️ Executar Projeto Principal

```bash
poe uvrm
```

ou

```bash
uv run main.py
```

---

# 📂 Organização do Projeto

O projeto possui um ficheiro principal `main.py` localizado na raiz.

Os exercícios serão organizados em pastas separadas dentro do projeto.

Cada exercício seguirá o padrão:

```text
ex01
ex02
ex03
...
```

O ficheiro `main.py` será responsável por chamar os exercícios através de um menu interativo.

---

# 🗂 Estrutura Atual do Projeto

```text
.
├── .venv/
├── .gitignore
├── .python-version
├── Lista de Exercícios – Programação Orientada a Objetos com Python.pdf
├── main.py
├── pyproject.toml
├── README.md
├── uv.lock
│
├── ex01/
│   ├── main.py
│   ├── classes.py
│   └── README.md
│
├── ex02/
│   ├── main.py
│   ├── conta.py
│   └── README.md
│
├── ex03/
│   ├── main.py
│   ├── biblioteca.py
│   └── README.md
│
└── ...
```

---

# 🧭 Funcionamento do Menu Principal

O ficheiro `main.py` da raiz será utilizado para:

- listar exercícios disponíveis
- chamar exercícios
- navegar entre módulos
- centralizar execução do projeto

---

# ▶️ Exemplo de Menu

```text
=========== MENU ===========
1 - Exercício 01
2 - Exercício 02
3 - Exercício 03
0 - Sair
============================

Escolha uma opção:
```

---

# 📚 Exercícios Planeados

## 🟢 Básico

- [ ] ex01 - Classe Pessoa
- [ ] ex02 - Conta Bancária
- [ ] ex03 - Biblioteca
- [ ] ex04 - Veículos

---

## 🟡 Intermediário

- [ ] ex05 - Sistema Escolar
- [ ] ex06 - Carrinho de Compras
- [ ] ex07 - Encapsulamento
- [ ] ex08 - Classes Abstratas
- [ ] ex09 - Funcionários

---

## 🔴 Avançado

- [ ] ex10 - Métodos Especiais
- [ ] ex11 - Sistema de Login
- [ ] ex12 - Inventário
- [ ] ex13 - Infraestrutura de TI
- [ ] ex14 - Backup Manager
- [ ] ex15 - Mini ERP
- [ ] ex16 - Sistema de Monitoramento

---

# 🧠 Conceitos Praticados

Durante os exercícios serão praticados:

- Classes
- Objetos
- Métodos
- Encapsulamento
- Herança
- Polimorfismo
- Abstração
- Composição
- Properties
- Decorators
- Métodos especiais
- Organização modular
- Tratamento de exceções
- Persistência de dados
- Arquitetura de software

---

# 💡 Objetivo da Estrutura

A estrutura foi organizada desta forma para praticar:

- modularização
- separação de responsabilidades
- arquitetura de projetos
- reutilização de código
- manutenção de aplicações
- escalabilidade

---

# 📖 Conceitos Para Pesquisar

- `__init__`
- `self`
- `super()`
- `@property`
- `ABC`
- `@abstractmethod`
- `__str__`
- `__repr__`
- composição vs herança
- SOLID
- MVC
- `__init__.py`
- imports em Python

---

# 🚀 Evolução Futura

Futuramente o projeto poderá evoluir para:

- API REST
- Django
- Flask
- PostgreSQL
- Docker
- CLI profissional
- arquitetura em camadas

---

# 🎯 Objetivo Final

Ao concluir os exercícios o objetivo será:

- dominar Programação Orientada a Objetos
- modelar sistemas reais
- desenvolver aplicações organizadas
- aplicar boas práticas de software
- estruturar projetos profissionais em Python

---

# 🧑‍💻 Autor

José de Almeida

---

# 📜 Licença

Projeto desenvolvido para fins educacionais.