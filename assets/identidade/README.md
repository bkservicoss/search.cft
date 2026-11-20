<p align="center"><img src="logo-search-cft.svg" alt="Search.CFT" width="360"></p>

# Identidade visual · família Search.CFT

**Marca de produto do Search.CRT, ferramenta de comparativo e busca de dados criada para o CRT-ES e preparada para o Sistema CFT/CRTs.**

## Sumário
1. [Conceito](#1-conceito)
2. [Família de nomes](#2-família-de-nomes)
3. [Arquivos](#3-arquivos)
4. [Cores](#4-cores)
5. [Tipografia](#5-tipografia)
6. [Uso correto](#6-uso-correto)
7. [Convivência com as marcas oficiais CFT/CRT](#7-convivência-com-as-marcas-oficiais-cftcrt)
8. [Como regenerar os arquivos](#8-como-regenerar-os-arquivos)

---

## 1. Conceito
O símbolo é uma **lupa com dois aros sobrepostos**. Cada aro é uma fonte de dados (uma planilha, uma lista); a **interseção em ciano** é o que o app encontra: o registro que aparece em mais de uma fonte. É literalmente o que o Comparativo de Dados faz.

## 2. Família de nomes
| Nome | Quando usar |
|---|---|
| **Search.CFT** | Marca-mãe e nome do repositório; uso nacional, no Sistema CFT/CRTs |
| **Search.CRT** | Nome do aplicativo instalado em um regional |
| **Search.CRT + assinatura de UF** | Edição de um regional (ex.: `ES · SISTEMA CFT/CRTs`) |

Regra de escrita: sempre `Search` + ponto + sigla em maiúsculas, sem espaço (`Search.CRT`, nunca `SearchCRT` ou `Search CRT`).

## 3. Arquivos
| Arquivo | Uso |
|---|---|
| `logo-search-cft.svg` / `-negativo.svg` | Marca-mãe (fundo claro / fundo escuro) |
| `logo-search-crt.svg` / `-negativo.svg` | Aplicativo |
| `logo-search-crt-es.svg` / `-negativo.svg` | Edição CRT-ES com assinatura |
| `simbolo.svg` / `simbolo-negativo.svg` | Só o símbolo, fundo transparente |
| `icone-app.svg`, `searchcrt.ico`, `icone-*.png` | Ícone do .exe, da janela e da aba do navegador |
| `logo-*.png` | Versões em imagem (3x) para documentos e apresentações |

Os textos dos logos estão convertidos em curvas: aparecem iguais em qualquer computador, sem precisar da fonte instalada.

## 4. Cores
| Nome | HEX | Papel |
|---|---|---|
| Azul Institucional | `#0B2545` | Fundo principal, texto do logo em fundo claro |
| Azul Profundo | `#13315C` | Painéis e cartões |
| Azul Médio | `#1F4E8C` | Botões, seleção, aros do símbolo |
| Ciano Busca | `#22B8CF` | Destaque, sigla do logo, interseção; texto só em fundo escuro |
| Ciano Texto | `#0B7285` | Links e destaques em texto sobre fundo claro |
| Ciano Claro | `#8FD8E6` | Texto secundário em fundo escuro |
| Verde Confere | `#2BB673` (escuro) · `#1E7F4F` (claro) | Resultado encontrado, sucesso, exportar |
| Âmbar Atenção | `#F2A541` (escuro) · `#9A5B00` (claro) | Avisos |
| Vermelho Alerta | `#FF8A8E` (escuro) · `#B4232A` (claro) | Erros, remover |
| Névoa | `#F4F7FB` | Fundo claro |
| Grafite | `#4A5668` | Texto secundário em fundo claro |

Contraste: todo texto atinge 4,5:1 no fundo indicado. O ciano `#22B8CF` sobre fundo claro fica em 2,2:1, então em fundo claro ele só aparece no logo e em formas, nunca em texto corrido.

## 5. Tipografia
| Uso | Fonte |
|---|---|
| Logo, web, documentos | **Inter** (gratuita, Google Fonts): Medium para "Search", ExtraBold para a sigla |
| App desktop (Windows) | **Segoe UI**, já presente no Windows |
| CPF, chaves, códigos | Fonte monoespaçada (Consolas / JetBrains Mono) |

## 6. Uso correto
- Respeitar uma área livre ao redor do logo igual à altura do ponto do ".".
- Tamanho mínimo: logo horizontal com 120 px de largura; abaixo disso, usar só o símbolo.
- Em fundo escuro, usar sempre a versão `-negativo`.
- Não mudar as cores do ciano, não esticar, não aplicar sombra, não trocar a fonte.

## 7. Convivência com as marcas oficiais CFT/CRT
Search.CRT é uma **marca de produto**, independente das marcas institucionais. Quando aparecer junto do logo do CFT ou de um CRT (tela de login, relatório, apresentação), a marca oficial vem à esquerda ou acima, separada por um fio vertical, seguindo o manual de marca do próprio conselho. Não usar o logo oficial sem autorização da assessoria de comunicação do conselho.

## 8. Como regenerar os arquivos
Os arquivos são gerados por `tools/gerar_identidade.py` (Python + fontTools + CairoSVG) a partir da paleta acima. Para mudar uma cor, edite os valores no topo do script, rode no Codespaces e substitua esta pasta.

<p align="center"><sub>Projeto privado · BK Serviços, Produção &amp; Comunicação</sub></p>
