# Vision Assistant Pro

**Vision Assistant Pro** é um assistente de IA avançado e multimodal para o NVDA. Ele utiliza os modelos Gemini do Google para fornecer leitura de tela inteligente, tradução, ditado por voz e recursos de análise de documentos.

_Este complemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Instalação e Configuração

Vá para **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**.

- **Chave de API:** Obrigatória. O campo é mascarado por padrão por segurança (use “Mostrar chave de API” para visualizar). Obtenha uma chave gratuita no [Google AI Studio](https://aistudio.google.com/).
- **Modelo:** Escolha entre **Flash** (Mais rápido/Gratuito) ou **Pro** (Alta Inteligência), conforme suas necessidades.
- **URL de Proxy:** Opcional. Use se o Google estiver bloqueado na sua região. Você precisa de um endereço de servidor (URL) que receba suas solicitações e as encaminhe para a API Gemini.
  > **Nota:** Isto **não** é para proxies VPN/SOCKS padrão (como `127.0.0.1:1080`). Deve ser um endereço web (ex.: `https://meu-proxy-personalizado.com`) que atue como ponte para o Google.
- **Idiomas:** Defina os idiomas de Origem, Destino e Resposta da IA.
- **Troca Inteligente:** Troca automaticamente os idiomas se o texto de origem corresponder ao idioma de destino.
- **Saída Direta:** Ignora a janela de chat e anuncia a resposta diretamente por fala.
- **Integração com a Área de Transferência:** Copia automaticamente a resposta da IA para a área de transferência.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este complemento utiliza uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um bip).
2. Solte as teclas e, em seguida, pressione uma das seguintes teclas únicas:

| Tecla | Função | Descrição |
| --- | --- | --- |
| **T** | Tradutor Inteligente | Traduz o texto sob o cursor de navegação ou a seleção. |
| **Shift + T** | Tradutor da Área de Transferência | Traduz o conteúdo atualmente na área de transferência. |
| **R** | Refinador de Texto | Resumir, corrigir gramática, explicar ou executar **Prompts Personalizados**. |
| **V** | Visão de Objeto | Descreve o objeto atual do navegador. |
| **O** | Visão da Tela Inteira | Analisa todo o layout e conteúdo da tela. |
| **Shift + V** | Análise de Vídeo Online | Analisa vídeos do **YouTube**, **Instagram** ou **Twitter (X)** via URL. |
| **D** | Análise de Documentos | Converse com arquivos PDF/TXT/MD/PY. |
| **F** | OCR de Arquivo | OCR direto de arquivos de imagem/PDF/TIFF (TIFF multipágina suportado). |
| **A** | Transcrição de Áudio | Transcreve arquivos MP3/WAV/OGG. |
| **C** | Resolvedor de CAPTCHA | Captura e resolve CAPTCHAs automaticamente. |
| **S** | Ditado Inteligente | Converte fala em texto. Pressione para iniciar a gravação e novamente para parar/digitar. |
| **L** | Relatório de Status | Anuncia o status atual (ex.: “Enviando...”, “Ocioso”). |
| **U** | Verificação de Atualizações | Verifica no GitHub a versão mais recente. |
| **H** | Ajuda de Comandos | Exibe uma lista completa de todos os atalhos disponíveis e suas descrições dentro da camada de comandos. |

## 3. Prompts Personalizados e Variáveis

Crie comandos em Configurações: `Nome:Texto do Prompt` (separe com `|` ou novas linhas).

### Variáveis Disponíveis

| Variável         | Descrição                                              | Tipo de Entrada       |
|------------------|--------------------------------------------------------|-----------------------|
| `[selection]`    | Texto atualmente selecionado                           | Texto                 |
| `[clipboard]`    | Conteúdo da área de transferência                      | Texto                 |
| `[screen_obj]`   | Captura de tela do objeto de navegação                 | Imagem                |
| `[screen_full]`  | Captura de tela completa                               | Imagem                |
| `[file_ocr]`     | Selecionar imagem/PDF/TIFF (padrão: "Extrair texto")   | Imagem, PDF, TIFF     |
| `[file_read]`    | Selecionar documento de texto                          | TXT, Código, PDF      |
| `[file_audio]`   | Selecionar arquivo de áudio                            | MP3, WAV, OGG         |

### Exemplos de Prompts Personalizados

- **OCR Rápido:** `Meu OCR:[file_ocr]`
- **Traduzir Imagem:** `Traduzir Img:Extraia o texto desta imagem e traduza para persa. [file_ocr]`
- **Analisar Áudio:** `Resumir Áudio:Ouça esta gravação e resuma os pontos principais. [file_audio]`
- **Depurador de Código:** `Depurar:Encontre bugs neste código e explique-os: [selection]`

**Nota:** É necessária uma conexão ativa com a internet para todos os recursos de IA. TIFFs multipágina são processados automaticamente.

## Alterações da versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comandos para fornecer uma lista de fácil acesso de todos os atalhos e suas funções.
- **Análise de Vídeo Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também houve melhoria na detecção de URLs e na estabilidade para uma experiência mais confiável.
- **Contribuição ao Projeto:** Adicionada uma caixa de diálogo opcional de doação para usuários que desejam apoiar futuras atualizações e o crescimento contínuo do projeto.

## Alterações da versão 3.5.0

- **Camada de Comandos:** Introduzido um sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido de `T`.
- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e Instagram diretamente fornecendo uma URL.

## Alterações da versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar o diálogo de chat e ouvir as respostas da IA diretamente por fala, proporcionando uma experiência mais rápida e fluida.
- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações da versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os usuários a distinguir entre modelos gratuitos e com limite de uso (pagos). Adicionado suporte ao **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Estabilidade do Ditado Inteligente significativamente melhorada. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, evitando alucinações da IA e erros vazios.
- **Manipulação de Arquivos:** Corrigido um problema em que o envio de arquivos com nomes não ingleses falhava.
- **Otimização de Prompts:** Melhorada a lógica de tradução e estruturados os resultados de Visão.

## Alterações da versão 2.9

- **Adicionadas traduções para Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão “Ver Formatado” nos diálogos de chat para visualizar a conversa com estilo adequado (Títulos, Negrito, Código) em uma janela navegável padrão.
- **Configuração de Markdown:** Adicionada uma nova opção “Limpar Markdown no Chat” nas Configurações. Desmarcando-a, os usuários podem ver a sintaxe Markdown bruta (ex.: `**`, `#`) na janela de chat.
- **Gerenciamento de Diálogos:** Corrigido um problema em que as janelas “Refinar Texto” ou de chat abriam várias vezes ou não focavam corretamente.
- **Melhorias de UX:** Padronizados os títulos dos diálogos de arquivo para “Abrir” e removidos anúncios de fala redundantes (ex.: “Abrindo menu...”) para uma experiência mais fluida.

## Alterações da versão 2.8

- Adicionada tradução para Italiano.
- **Relatório de Status:** Adicionado um novo comando (`NVDA+Control+Shift+I`) para anunciar o status atual do complemento (ex.: “Enviando...”, “Analisando...”).
- **Exportação HTML:** O botão “Salvar Conteúdo” nos diálogos de resultado agora salva a saída como um arquivo HTML formatado, preservando estilos como títulos e texto em negrito.
- **Interface de Configurações:** Melhorado o layout do painel de Configurações com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte a `gemini-flash-latest` e `gemini-flash-lite-latest`.
- **Idiomas:** Adicionado Nepali aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um bug crítico em que os comandos “Refinar Texto” falhavam se o idioma da interface do NVDA não fosse inglês.
- **Ditado:** Melhorada a detecção de silêncio para evitar saída incorreta de texto quando nenhuma fala é inserida.
- **Configurações de Atualização:** “Verificar atualizações ao iniciar” agora vem desativado por padrão para cumprir as políticas da Loja de Complementos.
- Limpeza de código.

## Alterações da versão 2.7

- Estrutura do projeto migrada para o modelo oficial de Complementos da NV Access para melhor conformidade com padrões.
- Implementada lógica de nova tentativa automática para erros HTTP 429 (Limite de Taxa) para garantir confiabilidade durante alto tráfego.
- Prompts de tradução otimizados para maior precisão e melhor tratamento da lógica de “Troca Inteligente”.
- Tradução russa atualizada.

## Alterações da versão 2.6

- Adicionado suporte à tradução russa (Obrigado ao nvda-ru).
- Mensagens de erro atualizadas para fornecer feedback mais descritivo sobre conectividade.
- Idioma de destino padrão alterado para Inglês.

## Alterações da versão 2.5

- Adicionado comando nativo de OCR de arquivo (`NVDA+Control+Shift+F`).
- Adicionado botão “Salvar Chat” nos diálogos de resultado.
- Implementado suporte completo à localização (i18n).
- Feedback de áudio migrado para o módulo nativo de tons do NVDA.
- Alterado para a API de Arquivos Gemini para melhor manipulação de arquivos PDF e de áudio.
- Corrigida falha ao traduzir texto contendo chaves `{}`.

## Alterações da versão 2.1.1

- Corrigido um problema em que a variável `[file_ocr]` não funcionava corretamente dentro de Prompts Personalizados.

## Alterações da versão 2.1

- Padronizados todos os atalhos para usar `NVDA+Control+Shift` a fim de eliminar conflitos com o layout Laptop do NVDA e atalhos do sistema.

## Alterações da versão 2.0

- Implementado sistema interno de Atualização Automática.
- Adicionado Cache Inteligente de Tradução para recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar resultados de forma contextual nos diálogos de chat.
- Adicionado comando dedicado de tradução da área de transferência (`NVDA+Control+Shift+Y`).
- Prompts de IA otimizados para impor estritamente a saída no idioma de destino.
- Corrigida falha causada por caracteres especiais no texto de entrada.

## Alterações da versão 1.5

- Adicionado suporte para mais de 20 novos idiomas.
- Implementado Diálogo Interativo de Refinamento para perguntas de acompanhamento.
- Adicionado recurso nativo de Ditado Inteligente.
- Adicionada a categoria “Vision Assistant” ao diálogo de Gestos de Entrada do NVDA.
- Corrigidas falhas COMError em aplicativos específicos como Firefox e Word.
- Adicionado mecanismo automático de nova tentativa para erros de servidor.

## Alterações da versão 1.0

- Lançamento inicial.
