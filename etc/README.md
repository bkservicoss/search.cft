# etc/ · configuração local

| Arquivo | O que é |
|---|---|
| `users.example.json` | Modelo vazio do cadastro de usuários do módulo de login (`auth_manager.py`) |
| `users.json` | Cadastro real. **Não vai para o repositório** (está no `.gitignore`) |

Para usar o login: copie `users.example.json` para `users.json` e crie os usuários pelo `auth_manager.create_user(...)`. Nenhuma senha padrão é distribuída com o projeto.

> O módulo de login ainda não está ligado aos apps (ver Pendências no README principal).
