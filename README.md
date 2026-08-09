# Jogos_Py

## 🎮 Arcade Web em Python (Flask)

Este projeto é uma plataforma web interativa desenvolvida em Python (utilizando o micro-framework Flask) que reúne minijogos clássicos em uma única interface moderna e responsiva. O sistema combina renderização no servidor com manipulação de sessões HTTP para gerenciar o estado dos jogos dos usuários.

## 🕹️ Jogos Disponíveis

* __🎯 Adivinhe o Número (`adivinhe_num.html`):__ O jogador deve adivinhar um número secreto gerado pelo servidor. O estado da partida (número de tentativas, palpites anteriores e número alvo) é gerenciado via sessões do Flask (session).
---

* __✂️ Pedra, Papel e Tesoura (`ped_pap_tes.html`):__ O clássico jogo de Jokenpô contra a CPU, com validações instantâneas de rodadas e pontuação.
---

* __🪓 Jogo da Forca (`forca.html & jogar_forca.html`):__ (Em implementação) Módulo focado na adivinhação de palavras secretas por letras, integrando interface gráfica e lógica de erros/tentativas.

## 🛠️ Tecnologias Utilizadas

* __`Back-end:`__ Python 3, Flask (Rotas, Sessões e Renderização de Templates)

* __`Front-end:`__ HTML5, CSS3 (Estilização modular com `jogos.css` e `style.css`), JavaScript (Interações dinâmicas via `app.js`)

* __`Arquitetura Web:`__ Modularização de rotas (`routes.py`), funções auxiliares (`auxiliares.py`) e regras de negócio/lógica de cada jogo em arquivo dedicado (`logica_jogos.py`).

## 📂 Estrutura do Repositório

```
Plaintext

JOGOS_PY/
│
├── app/
│   ├── static/                  # Arquivos estáticos (CSS, JS e Mídia)
│   │   ├── css/
│   │   │   ├── jogos.css        # Estilização específica das telas de jogos
│   │   │   └── style.css        # Estilos globais e layout base
│   │   ├── imagens/             # Ativos visuais dos jogos
│   │   └── js/
│   │       └── app.js           # Scripts de suporte no Front-end
│   │
│   ├── templates/               # Views renderizadas pelo Flask (Jinja2)
│   │   ├── adivinhe_num.html    # Tela do jogo de Adivinhação
│   │   ├── base.html            # Template base de layout
│   │   ├── forca.html           # Tela principal do Jogo da Forca
│   │   ├── index.html           # Dashboard / Menu principal de jogos
│   │   ├── jogar_forca.html     # Loop/Interface ativa do Jogo da Forca
│   │   ├── navbar.html          # Componente de navegação reaproveitável
│   │   └── ped_pap_tes.html     # Tela do jogo Pedra, Papel e Tesoura
│   │
│   ├── __init__.py              # Inicialização e configuração do App Flask
│   ├── auxiliares.py            # Funções utilitárias e helpers
│   ├── logica_jogos.py          # Módulo com a lógica pura dos minijogos
│   └── routes.py                # Definição dos endpoints e gerenciamento de sessões
│
├── venv/                        # Ambiente virtual Python
├── .gitignore                   # Arquivos ignorados pelo Git
└── LICENSE                      # Licença do repositório
```

## ⚙️ Como Executar o Projeto

Pré-requisitos

Certifique-se de ter o Python 3.x instalado na sua máquina.

Bash

```bash
Bash

# 1. Clone este repositório

git clone https://github.com/Pedro-Ramon2608/Jogos_Py.git

# 2. Acesse a pasta do projeto

cd Jogos_Py

# 3. Crie e ative um ambiente virtual (opcional, mas recomendado)

python -m venv venv

# No Windows:

venv\Scripts\activate

# No Linux/Mac:

source venv/bin/activate

# 4. Instale o Flask

pip install flask

# 5. Execute a aplicação

python -m app

# Ou execute através do arquivo de inicialização configurado

Após executar, abra o navegador e acesse:

[http://127.0.0.1:5000](http://127.0.0.1:5000)
```
