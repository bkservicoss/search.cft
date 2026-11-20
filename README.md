<p align="center"><img src="assets/identidade/logo-search-cft.svg" alt="Search.CFT" width="420"></p>

<p align="center"><b>Comparativo de fontes e busca localizada de dados cadastrais, criado para o CRT-ES e preparado para o Sistema CFT/CRTs.</b></p>
<p align="center">Python · Tkinter (desktop Windows) · Streamlit (web) · pandas</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-22B8CF?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/vers%C3%A3o-0.9%20(piloto%20CRT--ES)-1F4E8C?style=flat-square" alt="versão">
  <img src="https://img.shields.io/badge/Python-3.10%2B-0B2545?style=flat-square&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/plataforma-Windows%20%7C%20Web-13315C?style=flat-square" alt="plataforma">
  <img src="https://img.shields.io/badge/uso-privado-2BB673?style=flat-square" alt="uso privado">
</p>

---

## Sumário
1. [Visão geral](#1-visão-geral)
2. [Família Search.CFT e identidade visual](#2-família-searchcft-e-identidade-visual)
3. [Estado do projeto](#3-estado-do-projeto)
4. [Como usar (sem instalar nada)](#4-como-usar-sem-instalar-nada)
5. [Configuração](#5-configuração)
6. [Estrutura do repositório](#6-estrutura-do-repositório)
7. [Segurança e LGPD](#7-segurança-e-lgpd)
8. [Pendências](#8-pendências)

---

## 1. Visão geral
| Funcionalidade | O que faz |
|---|---|
| **Comparativo de Dados** | Cruza 2 ou mais arquivos e mostra quem aparece em pelo menos N fontes, por Nome, CPF, Telefone e/ou E-mail (combináveis). Exporta `.zip` com TXT, CSV e XLSX |
| **Busca Localizada** | Procura um Nome, CPF, Telefone, E-mail ou Município em todas as abas de uma planilha e exporta as linhas encontradas |
| **Normalização** | Remove acentos e símbolos de nomes, valida dígitos verificadores do CPF, padroniza telefone (tira +55 e zero do DDD) e e-mail em minúsculas |

| Versão | Arquivo | Situação |
|---|---|---|
| Desktop Windows | `searchcrt.py` (+ `searchcrt.spec`) | Funcional, em uso no piloto CRT-ES |
| Web | `searchcrt_streamlit.py` | Funcional, sem login, com aba de histórico |

## 2. Família Search.CFT e identidade visual
| Nome | Uso |
|---|---|
| **Search.CFT** | Marca-mãe e este repositório (escopo nacional, Sistema CFT/CRTs) |
| **Search.CRT** | O aplicativo instalado em cada regional |
| **Search.CRT · ES** | Edição do piloto no CRT-ES |

<p>
  <img src="assets/identidade/logo-search-crt.svg" alt="Search.CRT" height="48">&nbsp;&nbsp;
  <img src="assets/identidade/icone-app.svg" alt="ícone" height="48">
</p>

Símbolo: lupa com dois aros sobrepostos; a interseção em ciano é o registro encontrado em mais de uma fonte. Cores principais: Azul Institucional `#0B2545`, Ciano Busca `#22B8CF`, Verde Confere `#2BB673`. Manual completo, arquivos e regras de uso em [`assets/identidade/`](assets/identidade/README.md).

## 3. Estado do projeto
Panorama em 20/11/2026.

| Área | Situação | Observação |
|---|---|---|
| Motor de comparação e busca | 🟢 Pronto | Regras de CPF, telefone, e-mail e nome funcionando nas duas versões |
| App desktop | 🟢 Funcional | Identidade aplicada; 5 bugs corrigidos; build agora pelo GitHub Actions |
| App web | 🟢 Funcional | Identidade aplicada; roda no Codespaces |
| Identidade visual | 🟢 Pronto | Logos, ícone, paleta e manual em `assets/identidade/` |
| Build do .exe | 🟡 Novo | Workflow criado; precisa da 1ª execução para confirmar |
| Login (`auth_manager.py`) | 🟠 Não ligado | Existe, mas nenhum app usa; senha com SHA-256 sem sal |
| Banco (`database_manager.py`) | 🟠 Não ligado | MongoDB previsto, nenhum app grava nada |
| Configuração (`config.ini`) | 🟠 Não ligado | Os apps não leem o arquivo |
| Testes | 🔴 Parcial | 6 de 9 passam; os 3 de login falham (usuário de teste não é apagado entre testes). O motor de busca não tem teste |
| Multi-regional (CFT/CRTs) | ⚪ Não iniciado | Hoje é 1 instalação por máquina, sem separação por regional |

**Bugs corrigidos no app desktop (20/11/2026)**
| Bug | Correção |
|---|---|
| `.csv` aceito na seleção, mas ignorado no Comparativo | CSV lido de verdade (separador detectado sozinho); formato desconhecido agora gera aviso |
| Erro na Busca Localizada não mostrava mensagem | Mensagem guardada antes de sair do `except` |
| CPF em célula numérica do Excel perdia o zero à esquerda | Planilhas lidas como texto e CPF recomposto com 11 dígitos nas colunas "CPF" |
| Em `.txt`, a linha inteira virava "nome" | Nome extraído do trecho com 2+ palavras sem números |
| "Remover" tirava só o primeiro selecionado | Lista aceita seleção múltipla e remove todos |

Busca Localizada também passou a aceitar `.csv` e `.ods`. Na versão web, o CPF com zero à esquerda e o nome em `.txt` ainda seguem o comportamento antigo.

## 4. Como usar (sem instalar nada)
| O quê | Caminho |
|---|---|
| Baixar o `.exe` | **Actions** → **Build Windows (.exe)** → **Run workflow** → baixar o artefato **Search.CRT-windows** |
| Rodar a versão web | **Code** → **Codespaces** → **Create codespace on main** → no terminal: `streamlit run searchcrt_streamlit.py` |
| Rodar os testes | No terminal do Codespace: `pytest tests/` |

Detalhes em [INSTALL.md](INSTALL.md).

## 5. Configuração
| Item | Onde | Observação |
|---|---|---|
| Cores, ícone, logo | `assets/identidade/` | Os dois apps leem daqui |
| Build do Windows | `searchcrt.spec` | Inclui o ícone e exclui bibliotecas que o app não usa |
| Ambiente do Codespaces | `.devcontainer/devcontainer.json` | Python 3.12, instala `requirements.txt`, abre a porta 8501 |
| Usuários do login | `etc/users.json` (fora do Git) | Modelo em `etc/users.example.json`; nenhuma senha padrão |
| Parâmetros gerais | `config.ini` | Ainda não lido pelos apps |

## 6. Estrutura do repositório
```
search.cft/
├── CLAUDE.md                  # Instruções do projeto para o Claude
├── searchcrt.py               # App desktop (Tkinter)
├── searchcrt_streamlit.py     # App web (Streamlit)
├── searchcrt.spec             # Build do .exe (PyInstaller)
├── auth_manager.py            # Login local (não ligado)
├── database_manager.py        # MongoDB (não ligado)
├── config_manager.py          # Leitura do config.ini (não ligado)
├── config.ini
├── requirements.txt
├── setup.py
├── INSTALL.md
├── assets/identidade/         # Logos, ícones, manual da marca
├── tools/gerar_identidade.py  # Gera os arquivos da identidade
├── etc/                       # users.example.json
├── exports/ · logs/           # Saídas locais (fora do Git)
├── tests/test_core.py
├── .devcontainer/
└── .github/workflows/build-windows.yml
```

## 7. Segurança e LGPD
O app trata **dados pessoais** (nome, CPF, telefone, e-mail) de profissionais registrados em autarquia federal, então a LGPD se aplica.

| Regra | Situação |
|---|---|
| Nenhuma planilha, exportação ou log vai para o Git | ✅ `.gitignore` bloqueia `.xlsx`, `.xls`, `.csv`, `.ods`, `exports/`, `logs/` |
| Nenhuma senha ou usuário padrão no repositório | ✅ `etc/users.json` removido do Git; senhas antigas citadas na documentação foram retiradas |
| Segredos (Mongo, chaves) em GitHub Secrets ou variável de ambiente | ✅ Regra adotada; `config.ini` não deve receber senha |
| Repositório privado | ✅ Privado desde 20/11/2026 |
| Senhas com hash forte (bcrypt/argon2) | ⚠️ Pendente, se o login for ligado |
| Processamento só local (nada sai da máquina) | ✅ No desktop; na versão web, depende de onde for hospedada |

## 8. Pendências
- [x] Tornar o repositório privado
- [ ] Conferir o histórico do Git, que ainda guarda o antigo `etc/users.json` (senha padrão fraca, sem dado real)
- [ ] Rodar o workflow **Build Windows (.exe)** pela primeira vez e testar o `.exe` no CRT-ES
- [x] Corrigir os 5 bugs do app desktop
- [ ] Levar as mesmas correções (CPF como texto, nome em TXT) para a versão web
- [ ] Corrigir os testes de login e criar testes do motor (CPF, telefone, e-mail, comparativo)
- [ ] Juntar o motor num módulo único (`motor.py`) usado pelas duas versões, em vez de código duplicado
- [ ] Decidir se login, banco e `config.ini` entram no produto ou saem do repositório
- [ ] Definir o modelo para o Sistema CFT/CRTs: 1 instalação por regional ou versão web central com separação por CRT
- [ ] Validar com a comunicação do CFT/CRT-ES a convivência da marca Search.CRT com as marcas oficiais

<p align="center"><sub>Projeto privado · BK Serviços, Produção &amp; Comunicação</sub></p>
