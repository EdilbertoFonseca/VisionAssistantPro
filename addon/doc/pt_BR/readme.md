# Vision Assistant Pro

**Vision Assistant Pro** é um assistente de IA avançado e multimodal para o NVDA. Ele utiliza os modelos Gemini do Google para oferecer recursos inteligentes de leitura de tela, tradução, ditado por voz e análise de documentos.

_Este add-on foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Instalação e Configuração

Acesse **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**.

- **Chave de API:** Obrigatória. O campo é mascarado por padrão por motivos de segurança (use “Mostrar chave de API” para visualizar). Obtenha uma chave gratuita no [Google AI Studio](https://aistudio.google.com/).
- **Modelo:** Escolha entre os modelos **Flash** (mais rápido/gratuito) ou **Pro** (alta inteligência), de acordo com suas necessidades.
- **URL de Proxy:** Opcional. Use esta opção se o Google estiver bloqueado em sua região. É necessário um endereço de servidor (URL) que receba suas requisições e as encaminhe para a API do Gemini.  
  > **Nota:** Isto **não** é para proxies VPN/SOCKS padrão (como `127.0.0.1:1080`). Deve ser um endereço web (ex.: `https://meu-proxy-personalizado.com`) que atue como ponte para o Google.
- **Idiomas:** Defina os idiomas de origem, destino e resposta da IA.
- **Troca Inteligente:** Alterna automaticamente os idiomas se o texto de origem corresponder ao idioma de destino.
- **Saída Direta:** Ignora a janela de chat e anuncia a resposta diretamente por voz.
- **Integração com a Área de Transferência:** Copia automaticamente a resposta da IA para a área de transferência.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este add-on utiliza uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (tecla mestra) para ativar a camada (você ouvirá um bipe).
2. Solte as teclas e, em seguida, pressione uma das teclas abaixo:

| Tecla         | Função                    | Descrição                                                                 |
|---------------|---------------------------|---------------------------------------------------------------------------|
| **T**         | Tradutor Inteligente      | Traduz o texto sob o cursor de navegação ou a seleção atual.              |
| **Shift + T** | Tradutor da Área de Transferência | Traduz o conteúdo atualmente presente na área de transferência. |
| **R**         | Refinador de Texto        | Resume, corrige gramática, explica ou executa **Prompts Personalizados**.|
| **V**         | Visão de Objeto           | Descreve o objeto atual sob o cursor de navegação.                        |
| **O**         | Visão de Tela Inteira     | Analisa todo o layout e conteúdo da tela.                                 |
| **Shift + V** | Análise de Vídeo Online   | Analisa vídeos do **YouTube**, **Instagram** ou **Twitter (X)** via URL. |
| **D**         | Análise de Documentos     | Conversa com arquivos PDF/TXT/MD/PY.                                      |
| **F**         | OCR de Arquivo            | OCR direto de arquivos de imagem/PDF/TIFF (TIFF multipágina suportado).  |
| **A**         | Transcrição de Áudio      | Transcreve arquivos MP3/WAV/OGG.                                          |
| **C**         | Solucionador de CAPTCHA   | Captura e resolve CAPTCHAs automaticamente.                              |
| **S**         | Ditado Inteligente        | Converte fala em texto. Pressione para iniciar e novamente para parar.   |
| **L**         | Relatório de Status       | Anuncia o status atual (ex.: “Enviando…”, “Ocioso”).                      |
| **U**         | Verificação de Atualizações | Verifica no GitHub se há uma nova versão.                               |
| **H**         | Ajuda de Comandos         | Exibe uma lista completa de todos os atalhos disponíveis e suas descrições dentro da camada de comandos. |

## 3. Prompts Personalizados e Variáveis

Crie comandos em Configurações no formato: `Nome:Texto do Prompt` (separados por `|` ou por novas linhas).

### Variáveis Disponíveis

| Variável        | Descrição                                      | Tipo de Entrada      |
|-----------------|------------------------------------------------|----------------------|
| `[selection]`   | Texto atualmente selecionado                   | Texto                |
| `[clipboard]`   | Conteúdo da área de transferência              | Texto                |
| `[screen_obj]`  | Captura de tela do objeto de navegação         | Imagem               |
| `[screen_full]` | Captura de tela completa                       | Imagem               |
| `[file_ocr]`    | Selecionar imagem/PDF/TIFF (padrão: “Extrair texto”) | Imagem, PDF, TIFF |
| `[file_read]`   | Selecionar documento de texto                  | TXT, Código, PDF     |
| `[file_audio]`  | Selecionar arquivo de áudio                    | MP3, WAV, OGG        |

### Exemplos de Prompts Personalizados

- **OCR Rápido:** `Meu OCR:[file_ocr]`
- **Traduzir Imagem:** `Traduzir Imagem:Extraia o texto desta imagem e traduza para persa. [file_ocr]`
- **Analisar Áudio:** `Resumir Áudio:Ouça esta gravação e resuma os pontos principais. [file_audio]`
- **Depurador de Código:** `Depurar:Encontre erros neste código e explique-os: [selection]`

**Nota:** É necessária uma conexão ativa com a internet para todas as funcionalidades de IA. Arquivos TIFF multipágina são processados automaticamente.

## Alterações da versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) na Camada de Comandos para fornecer uma lista de fácil acesso com todos os atalhos e suas funções.
- **Análise de Vídeos Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também foram feitas melhorias na detecção de URLs e na estabilidade, proporcionando uma experiência mais confiável.
- **Contribuição para o Projeto:** Adicionada uma caixa de diálogo opcional de doação para usuários que desejam apoiar as futuras atualizações do projeto e seu crescimento contínuo.

## Alterações da versão 3.5.0

- **Camada de Comandos:** Introduzido o sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra.
- **Análise de Vídeos Online:** Adicionada a funcionalidade de analisar vídeos do YouTube e Instagram diretamente por meio de uma URL.

## Alterações da versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar o diálogo de chat e ouvir as respostas da IA diretamente por voz.
- **Integração com a Área de Transferência:** Nova opção para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações da versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **persa** e **vietnamita**.
- **Modelos de IA Expandidos:** Reorganização da lista de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`).
- **Estabilidade do Ditado:** Melhorias significativas no Ditado Inteligente, ignorando áudios menores que 1 segundo.
- **Manipulação de Arquivos:** Corrigido um problema ao enviar arquivos com nomes que não estavam em inglês.
- **Otimização de Prompts:** Melhorias na lógica de tradução e estruturação dos resultados de visão.

## Alterações da versão 2.9

- Adicionadas traduções para francês e turco.
- **Visualização Formatada:** Botão “Visualizar Formatado” para exibir o conteúdo com estilos adequados.
- **Configuração de Markdown:** Opção “Limpar Markdown no Chat”.
- **Gerenciamento de Diálogos:** Correções de foco e múltiplas aberturas de janelas.
- **Melhorias de UX:** Padronização de títulos de diálogos e redução de anúncios redundantes.

## Alterações da versão 2.8

- Adicionada tradução para italiano.
- **Relatório de Status:** Novo comando para anunciar o status atual do add-on.
- **Exportação HTML:** Resultados agora podem ser salvos como HTML formatado.
- **Interface de Configurações:** Layout aprimorado com melhor acessibilidade.
- **Novos Modelos:** Suporte a gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado suporte ao nepalês.
- **Ditado:** Melhorias na detecção de silêncio.
- Limpeza de código.

## Alterações da versão 2.7

- Migração da estrutura do projeto para o modelo oficial de add-ons da NV Access.
- Implementada lógica de repetição automática para erros HTTP 429.
- Otimização dos prompts de tradução.
- Tradução russa atualizada.

## Alterações da versão 2.6

- Adicionado suporte ao idioma russo.
- Mensagens de erro mais descritivas sobre conectividade.
- Idioma de destino padrão alterado para inglês.

## Alterações da versão 2.5

- Adicionado comando nativo de OCR de arquivos.
- Botão “Salvar Chat” nos diálogos de resultado.
- Suporte completo à localização (i18n).
- Migração dos sons para o módulo nativo de tons do NVDA.
- Correção de falha ao traduzir textos com chaves.

## Alterações da versão 2.1.1

- Corrigido um problema onde a variável `[file_ocr]` não funcionava corretamente em prompts personalizados.

## Alterações da versão 2.1

- Padronização de todos os atalhos para NVDA+Control+Shift.

## Alterações da versão 2.0

- Sistema de atualização automática integrado.
- Cache inteligente de traduções.
- Memória de conversas nos diálogos de chat.
- Comando dedicado de tradução da área de transferência.
- Correção de falhas causadas por caracteres especiais.

## Alterações da versão 1.5

- Suporte a mais de 20 novos idiomas.
- Diálogo interativo de refinamento de texto.
- Ditado inteligente nativo.
- Correções de falhas em aplicativos específicos.

## Alterações da versão 1.0

- Lançamento inicial.
