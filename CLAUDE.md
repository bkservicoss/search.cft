# Search.CFT · instruções do projeto

O Search.CRT é um app de comparativo de fontes e busca localizada de dados cadastrais (Nome, CPF, Telefone, E-mail, Município), criado para o CRT-ES e preparado para o Sistema CFT/CRTs. Este repositório é a casa da família Search.CFT.

Projeto privado da BK Serviços, Produção & Comunicação.

## Como o dono trabalha
- Não instala nada no computador: tudo roda na nuvem (GitHub Actions para compilar, GitHub Codespaces para rodar e testar, hospedagem para manter no ar).
- Fala português do Brasil; respostas, commits, README e textos de interface em português.
- Prefere passo a passo curto, com o caminho exato dos menus (ex.: **Actions → Build Windows (.exe) → Run workflow**).
- Decisões a ajustar: perguntar em checklist com opções clicáveis.

## Mapa
| Caminho | O que é |
|---|---|
| `searchcrt.py` | App desktop (Tkinter). Motor: `extrair_*`, `is_cpf_valido`, `ler_tabelas`, `_gerar_chaves` |
| `searchcrt_streamlit.py` | App web (Streamlit), com o motor duplicado |
| `searchcrt.spec` | Build do .exe (PyInstaller), com ícone e exclusões |
| `auth_manager.py`, `database_manager.py`, `config_manager.py`, `config.ini` | Login, MongoDB e configuração: existem, mas **não estão ligados** aos apps |
| `assets/identidade/` | Logos, ícones e manual da marca |
| `tools/gerar_identidade.py` | Gera os arquivos da identidade |
| `tests/test_core.py` | Testes (só login e config; o motor ainda não tem teste) |
| `.devcontainer/` | Ambiente do Codespaces |
| `.github/workflows/build-windows.yml` | Build do .exe |

## Como rodar / compilar
- **.exe**: workflow `Build Windows (.exe)`. Dispara sozinho em push na `main` que mude `searchcrt.py`, `searchcrt.spec`, `assets/identidade/**` ou o próprio workflow; também pelo botão **Run workflow**. Artefato: `Search.CRT-windows`.
- **Web**: Codespace → `streamlit run searchcrt_streamlit.py` (porta 8501).
- **Testes**: Codespace → `pytest tests/`.
- Commits que só mexem em documentação: incluir `[skip ci]` na mensagem.

## Regras que não podem quebrar
- Planilhas são lidas **como texto** (`dtype=str`) por `ler_tabelas`; nunca voltar a ler CPF/telefone como número.
- CPF só conta se passar no dígito verificador; saída sempre `000.000.000-00`.
- Telefone normalizado sem +55 e sem zero do DDD (10 ou 11 dígitos).
- Nada de dados pessoais sai da máquina no app desktop: sem envio pela rede.
- Tkinter só é atualizado pela thread principal (`self.root.after`); o processamento pesado fica em thread separada.
- Dentro de `except`, copiar `str(e)` para uma variável antes de usar em `lambda`.
- Arquivos de identidade são carregados com `caminho_recurso()` para funcionar no .py e no .exe.
- Mudanças no motor devem ir para as duas versões (desktop e web) até o motor virar módulo único.

## Segurança e LGPD
- O app trata dados pessoais de autarquia federal: **nunca** versionar planilhas, exportações, logs ou `etc/users.json` (o `.gitignore` já bloqueia).
- Nunca versionar tokens, chaves, senhas ou `.env`. Segredos vão em GitHub Secrets ou variáveis de ambiente da hospedagem.
- Se o dono colar um token ou senha no chat: não usar, não repetir, orientar a gerar outro e salvar direto nos Secrets.
- Exemplos e testes só com dados fictícios (CPF gerado com dígito válido, nomes genéricos).

## Identidade visual
- Símbolo: lupa com dois aros sobrepostos; a interseção em ciano é o registro achado em mais de uma fonte.
- Cores: Azul Institucional `#0B2545`, Azul Profundo `#13315C`, Azul Médio `#1F4E8C`, Ciano Busca `#22B8CF`, Ciano Claro `#8FD8E6`, Verde Confere `#2BB673`, Vermelho Alerta `#FF8A8E` (fundo escuro).
- Fontes: Inter (logo, web, documentos); Segoe UI no app desktop.
- Nomes: `Search.CFT` (marca-mãe), `Search.CRT` (app), `Search.CRT · ES` (regional). Sempre com ponto, sem espaço.
- Não imitar nem usar as marcas oficiais do CFT/CRTs sem autorização. Manual completo: `assets/identidade/README.md`.

## README
Seguir o padrão dos repositórios da BK Serviços: logo centralizada, frase de apresentação em negrito, selos, Sumário numerado, seções em tabelas, estrutura do repositório em árvore, pendências com `- [ ]` e rodapé `Projeto privado · BK Serviços, Produção & Comunicação`. Toda mudança no repositório entra no README no mesmo trabalho.

## Repositórios novos
Sempre que o dono criar um repositório novo, perguntar se ele quer criar o `CLAUDE.md`.
