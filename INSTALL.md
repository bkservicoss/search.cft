# Como rodar o Search.CRT (sem instalar nada no computador)

## Versão Windows (.exe)
1. No GitHub, abra o repositório **bkservicoss/search.cft** → aba **Actions**.
2. Clique em **Build Windows (.exe)** → **Run workflow** → **Run workflow**.
3. Quando ficar verde, abra a execução e baixe o artefato **Search.CRT-windows** (é um .zip com o `Search.CRT.exe`).

O .exe também é gerado sozinho a cada mudança no `main` em `searchcrt.py`, `searchcrt.spec` ou na identidade visual.

## Versão web (Streamlit) pelo navegador
1. No repositório: **Code** → aba **Codespaces** → **Create codespace on main**.
2. Espere instalar (o `.devcontainer` já roda o `pip install`).
3. No terminal do Codespace: `streamlit run searchcrt_streamlit.py`
4. A porta **8501** abre sozinha no navegador.

## Testes
No terminal do Codespace: `pytest tests/`
