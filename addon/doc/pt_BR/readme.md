# Documentação do Vision Assistant Pro

<!-- DOWNLOAD_COUNT_START --> Total Downloads: 61,000+ <!-- DOWNLOAD_COUNT_END -->

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Ele utiliza mecanismos de IA de classe mundial para fornecer leitura de tela inteligente, tradução, ditado por voz e análise de documentos.

_Este complemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Instalação e Configuração

Acesse **Menu do NVDA > Preferências > Configurações > Vision Assistant Pro**. A caixa de diálogo de configurações está organizada em 8 guias acessíveis: **Conexão**, **Comportamento da IA**, **Idiomas de Tradução**, **Leitor de Documentos**, **Vídeo**, **CAPTCHA**, **Prompts** e **Avançado**.

### 1.1 Guia Conexão

- **Provedor:** Selecione o seu serviço de IA preferido. Os provedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** e **Personalizado** (servidores compatíveis com OpenAI como Ollama, LM Studio, Jan.ai ou KoboldCPP).
- **Chave de API:** Insira uma ou várias chaves de API (separadas por vírgulas ou quebras de linha) para rotação automática.
- **Buscar Modelos:** Pressione este botão após inserir sua chave de API para baixar a lista de modelos disponíveis mais recente do provedor.
- **Modelo de IA:** Selecione o modelo principal usado para chat geral e análise.
- **Configurações do Provedor Personalizado:** Configure pontos de extremidade (endpoints) locais ou personalizados. Inclui **Configurar IA Local** (configuração em um clique para Ollama, LM Studio, Jan.ai ou KoboldCPP) e **Configuração Avançada do Ponto de Extremidade**.
- **Roteamento Avançado de Modelos (Específico por Tarefa):** Opcionalmente, selecione modelos dedicados nos menus suspensos para tarefas de OCR, STT, TTS, Operador de IA, Vídeo e Assistente Ao Vivo.
- **Opções de Conexão e Saída:** Configure a URL do Proxy, verificações de atualização na inicialização, Limpar Markdown no Chat, Copiar respostas da IA para a área de transferência, Saída Direta (Sem Janela de Chat) e Saída Direta do Assistente Ao Vivo.

### 1.2 Guia Comportamento da IA

- **Criatividade (Temperatura):** Controla a aleatoriedade e a criatividade da IA (de 0,0 a 2,0). Valores mais baixos produzem resultados de tradução e OCR mais determinísticos e precisos.

### 1.3 Guia Idiomas de Tradução

- **Idioma de Origem:** Selecione o seu idioma de entrada padrão.
- **Idioma de Destino:** Selecione o seu idioma principal de destino para tradução.
- **Idioma de Resposta da IA:** Selecione o idioma para as respostas gerais da IA.
- **Troca Inteligente:** Troca automaticamente os idiomas de origem e destino com base na entrada detectada.

### 1.4 Guia Leitor de Documentos

- **Mecanismo de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **IA (Avançado)** para uma preservação de layout superior.
- **Tamanho do Lote do OCR:** Especifique as páginas por requisição (defina como 0 para processamento em requisição única).
- **Descrever Imagens no Corpo do Texto:** Ative ou desative descrições de imagens integradas durante a extração de texto de documentos.
- **Exportar Números de Página:** Ative ou desative números de página e separadores na saída de documentos com várias páginas.
- **Voz do TTS:** Selecione o estilo de voz padrão para a geração de áudio.

### 1.5 Guia Vídeo

- **Tamanho do Bloco de Vídeo:** Duração do segmento em minutos para a geração de Audiodescrição (defina como 0 para processar o arquivo inteiro).
- **Adicionar Lista de Personagens:** Opção para adicionar o dicionário de personagens como a primeira entrada da legenda.
- **Adicionar Isenção de Responsabilidade da IA:** Opção para inserir uma isenção de responsabilidade da IA no início das legendas SRT do vídeo.

### 1.6 Guia CAPTCHA

- **Ativar Solucionador de CAPTCHA Visual:** Ative ou desative a resolução automatizada de desafios visuais (hCaptcha, reCAPTCHA).
- **Método de CAPTCHA de Texto:** Escolha entre capturar o **Objeto Navegador** ou a **Tela Cheia**.

### 1.7 Guia Prompts

- **Gerenciar Prompts:** Abre uma caixa de diálogo dedicada para personalizar os prompts padrão do sistema ou criar, editar, reordenar e pré-visualizar prompts personalizados definidos pelo usuário com variáveis dinâmicas (ex.: `[selection]`, `[screen_fg_obj]`).

### 1.8 Guia Avançado e Registros Globais

Navegue até a guia **Avançado** para configurar os registros globais do complemento:

- **Ativar arquivo de log dedicado:** Ative ou desative o registro de todos os eventos operacionais, tráfego de API e erros em todos os módulos do complemento em um arquivo separado (`vision_assistant.log`).
- **Nível de Log:** Selecione a detalhamento entre **Depuração (Todos os Detalhes)**, **Informação (Informações Gerais)**, **Aviso (Apenas Avisos)** e **Erro (Apenas Erros)**.
- **Manter Logs Por:** Defina períodos de retenção automática para limpar automaticamente entradas de log mais antigas (variando de 1 hora a 90 dias).
- **Controles de Gerenciamento do Log:** Use **Abrir Arquivo de Log**, **Abrir Pasta do Log** ou **Limpar Arquivo de Log** para inspecionar ou limpar os dados do log diretamente sem reiniciar o NVDA ou interferir nos logs padrão do NVDA.

## 2. Camada de Comandos e Atalhos

Para evitar conflitos de teclado, este complemento usa uma **Camada de Comandos**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um sinal sonoro).
2. Solte as teclas e pressione uma das seguintes teclas individuais:

| Tecla                  | Função                             | Descrição                                                                                                                                |
| ---------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + A**          | **Operador de IA**                 | **Operação Autônoma:** Peça à IA para realizar uma tarefa na sua tela. Pressionar novamente aborta instantaneamente as operações ativas. |
| **E**                  | **Explorador de IU**               | **Clique Interativo:** Identifica e clica em elementos da interface em qualquer aplicativo.                                              |
| **T**                  | Tradutor Inteligente               | Traduz o texto sob o cursor do navegador de objetos ou seleção.                                                                          |
| **Shift + T**          | Tradutor da Área de Transferência  | Traduz o conteúdo atualmente na área de transferência.                                                                                   |
| **R**                  | Refinador de Texto                 | Resumir, Corrigir Gramática, Explicar ou executar **Prompts Personalizados**.                                                            |
| **V**                  | Visão de Objeto                    | Descreve o objeto navegador atual.                                                                                                       |
| **O**                  | Visão de Tela Cheia                | Analisa toda a disposição e o conteúdo da tela.                                                                                          |
| **Shift + V**          | Análise de Vídeo                   | Analisa arquivos de vídeo locais ou vídeos online do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.                          |
| **Control + V**        | Gravação de Vídeo Local            | Grava um vídeo silencioso da sua tela e analisa as ações e o layout.                                                                     |
| **D**                  | Leitor de Documentos               | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.                                                                  |
| **F**                  | **Ação de Arquivo Inteligente**    | Reconhecimento contextual a partir de arquivos selecionados de imagem, PDF ou TIFF.                                                      |
| **M**                  | Transcrição e Dublagem de Mídia    | Transcreve ou dubla arquivos de áudio/vídeo (MP3, WAV, MP4, etc.) para o seu idioma de destino.                                          |
| **C**                  | Solucionador de CAPTCHA            | Captura e resolve CAPTCHAs.                                                                                                              |
| **Shift + C**          | Chat Direto                        | Abre uma interface de chat direto baseada em texto com a IA.                                                                             |
| **S**                  | Ditado Inteligente                 | Converte fala em texto. Pressione para iniciar a gravação e novamente para parar/digitar.                                                |
| **Control+T**          | Tradução de Voz                    | Transcreve, traduz e digita o resultado com base nas suas configurações de idioma.                                                       |
| **Control+L**          | **Assistente Ao Vivo**             | **Copiloto em Tempo Real (Apenas Gemini):** Inicia ou encerra uma conversa ao vivo por voz e tela com o assistente de IA.                |
| **I**                  | Relatório de Status                | Anuncia o progresso atual (ex.: "Analisando...", "Ocioso").                                                                              |
| **L**                  | **Rotular Objeto**                 | **Rotulagem Semântica por IA:** Rotula permanentemente o elemento/ícone focado no momento.                                               |
| **Shift + L**          | **Gerenciar/Escanear Rótulos**     | Abre o Gerenciador de Rótulos (se existirem rótulos) ou escaneia o app em busca de elementos sem nome.                                   |
| **U**                  | Verificar Atualizações             | Verifica manualmente no GitHub a existência da versão mais recente do complemento.                                                       |
| **Espaço**             | Relembrar Último Resultado         | Exibe a última resposta da IA em uma caixa de diálogo de chat para revisão ou acompanhamento.                                            |
| **H**                  | Ajuda de Comandos                  | Exibe uma lista de todos os atalhos disponíveis.                                                                                         |
| **Alt + S**            | Configurações                      | Abre a caixa de diálogo de configurações do Vision Assistant Pro.                                                                        |
| **Alt + Q**            | Relatório de Chaves Esgotadas      | Relata o número de chaves de API do Gemini que excederam a cota diária e seu tempo de redefinição.                                       |
| **Alt + M**            | Auditoria de Roteamento            | Relata os modelos de IA selecionados atualmente no roteamento avançado.                                                                  |
| **Cima / Baixo**       | Navegação de Configurações Rápidas | Navega entre as categorias de configurações rápidas (Provedor, Modelo, etc.) na camada.                                                  |
| **Esquerda / Direita** | Alterar Configuração Rápida        | Altera o valor da configuração rápida selecionada no momento.                                                                            |

## 3. Operador de IA - Controle Autônomo do Computador

O **Operador de IA** transforma o Vision Assistant Pro de um leitor passivo em um assistente ativo capaz de interagir com o computador em seu nome. Você pode pedir para ele descrever a tela, responder a perguntas sobre o que vê ou até assumir o controle — clicando em botões, arrastando itens, digitando texto e navegando por aplicativos usando comandos em linguagem natural.

A maior vantagem? Ele funciona perfeitamente em softwares completamente inacessíveis. Se você estiver preso em um aplicativo personalizado, em uma área de trabalho remota ou em um site onde o seu leitor de tela fica totalmente silencioso, isso não é um problema para o operador. Como ele "vê" a tela visualmente, ele consegue encontrar, ler e interagir com elementos que não possuem nenhum rótulo de acessibilidade.

### Como Funciona

1. Pressione **NVDA + Shift + V** e, em seguida, pressione **Shift + A** (ou use o atalho direto) para abrir a caixa de diálogo do Operador de IA.
2. Digite o que deseja fazer em linguagem simples (ex.: "Clique no botão Salvar", "O que diz a mensagem de erro?" ou "Renomeie o arquivo para final.pdf").
3. A IA analisará sua tela, identificará os elementos relevantes e executará a ação ou fornecerá a resposta. Se uma tarefa exigir várias etapas, o operador continuará trabalhando até que ela seja concluída.
4. Pressione **Shift + A** novamente a qualquer momento para abortar instantaneamente uma operação em andamento.

### Ações Suportadas

O operador entende uma grande variedade de comandos:

- **Descrever e Responder**: "Descreva a disposição da tela" ou "O que diz a mensagem de erro?"
- **Clique**: "Clique no botão Salvar"
- **Clique com o Botão Direito**: "Clique com o botão direito no arquivo"
- **Clique Duplo**: "Dê um clique duplo no documento"
- **Arrastar e Soltar**: "Arraste o documento para a pasta Arquivo"
- **Digitar**: "Digite 'Olá Mundo' na caixa de pesquisa"
- **Rolar**: "Role para baixo três vezes"
- **Pressionar Tecla**: "Pressione Enter", "Pressione Tab", "Pressione Escape"
- **Tarefas de Múltiplas Etapas**: "Abra o Explorador de Arquivos, encontre o relatório e renomeie-o para final.pdf"

### Notas Importantes

- **⚠️ Aviso de Uso da API**: Como o operador precisa "ver" exatamente o que está acontecendo na tela, ele envia uma captura de tela de alta resolução a cada etapa. O uso frequente consumirá sua cota de API muito mais rápido do que os recursos padrão baseados em texto.
- **Aplicativos como Administrador**: Se o NVDA não estiver sendo executado com privilégios de Administrador, o operador pode não conseguir interagir com janelas que exigem permissões elevadas. Essa é uma limitação de segurança do Windows, não um erro no complemento.
- **Boas Práticas**: Para obter os melhores resultados, dê comandos claros e específicos. "Clique no botão Enviar azul na parte inferior do formulário" quase sempre funcionará melhor do que apenas "Clique no botão".

## 4. Análise de Vídeo e Audiodescrição

> **Nota:** Os recursos de Análise de Vídeo e Audiodescrição são executados exclusivamente pelo provedor **Google Gemini**. Certifique-se de que o seu provedor ativo nas configurações do complemento esteja definido como Google Gemini.

O Vision Assistant Pro introduz recursos poderosos de processamento de vídeo desenvolvidos especificamente para usuários cegos. Ele pode analisar tanto vídeos online quanto gravações de tela locais para fornecer descrições visuais altamente detalhadas e gerar roteiros profissionais de Audiodescrição (SRT).

### 4.1 Gravação de Vídeo Local (Control + V)

Se você encontrar um vídeo sem som, uma animação ou um tutorial em sua tela, poderá capturá-lo diretamente:

1. Pressione **NVDA + Shift + V** para entrar na Camada de Comandos e, em seguida, pressione **Control + V**.
2. O complemento gravará silenciosamente sua tela em segundo plano.
3. Pressione **Control + V** novamente para parar a gravação.
4. A IA analisará o trecho de vídeo gravado e fornecerá uma descrição altamente detalhada da cena, dos personagens e das ações.

### 4.2 Análise de Vídeo (Shift + V)

Você pode analisar arquivos de vídeo locais e vídeos online. Basta selecionar um arquivo de vídeo local no Explorador de Arquivos do Windows ou copiar o link de um vídeo online para a área de transferência. Você também pode pressionar **Shift + V** em qualquer lugar (como dentro de um reprodutor de mídia) para abrir uma caixa de diálogo onde pode procurar por um arquivo de vídeo ou colar uma URL manualmente.

- **Plataformas Online Suportadas:** YouTube, Instagram, TikTok e Twitter (X).
- A IA detectará automaticamente o arquivo local ou a URL, processará o vídeo e fornecerá uma descrição visual abrangente e um resumo em áudio.

### 4.3 Geração de Audiodescrição (SRT)

Para uma experiência mais estruturada, o complemento pode gerar roteiros profissionais de Audiodescrição no formato padrão SubRip (SRT).

- **Sincronização Inteligente por Intervalos:** A IA ouve a faixa de áudio e ancora especificamente suas descrições visuais em pausas naturais e momentos de silêncio para minimizar de forma inteligente a sobreposição de diálogos.
- **Rastreamento de Personagens:** O mecanismo realiza uma análise prévia para extrair personagens distintos com base em traços faciais imutáveis. Ele constrói um dicionário global para rastrear e rotular com precisão os personagens em diferentes cenas sem confusão.
- **OCR do Texto Íntegra:** Qualquer texto exibido na tela (placas, telefones, créditos) é rigorosamente transcrito ao pé da letra.
- **Como Usar:** Para ouvir a legenda gerada, basta colocar o arquivo `.srt` na mesma pasta do seu arquivo de vídeo e dar a ele exatamente o mesmo nome. Em seguida, configure seu reprodutor de mídia (ex.: VLC ou PotPlayer) para direcionar o texto das legendas diretamente para o seu leitor de tela ou mecanismo de TTS durante a reprodução.

### 4.4 Narração de Áudio Sincronizada (Exportação em MP3)

Além de criar arquivos SRT em texto, o complemento funciona como uma ferramenta completa de produção de Audiodescrição, sintetizando as descrições em fala e misturando-as ao vídeo. Você pode escolher o **Gemini Live TTS** como mecanismo de voz, que utiliza a API Gemini Live para gerar narrações de voz altamente realistas e ilimitadas. Ao gerar um MP3 para arquivos de vídeo locais, você tem vários modos de mixagem à disposição:

- **AD Padrão (Mixar Voz):** A narração é sobreposta diretamente ao áudio do vídeo. Você será perguntado se deseja aplicar o **Audio Ducking** (redução do volume do áudio de fundo durante as descrições) para garantir que a narração fique clara.
- **AD Estendida (Pausar Áudio):** O mecanismo pausa o áudio original do vídeo durante as descrições, garantindo que você nunca perca uma única palavra do diálogo original ou da narração da IA.
- **Vídeos do YouTube:** Para fontes do YouTube (que não são baixadas localmente), a exportação em MP3 conterá estritamente a faixa de voz sintetizada da IA sincronizada, sem o áudio de fundo do vídeo.

## 5. Transcrição e Dublagem de Mídia (M)

O Transcritor de Áudio foi completamente reformulado para suportar arquivos de áudio e vídeo (MP3, WAV, MP4, MKV, etc.). Pressione **M** na Camada de Comandos para selecionar um arquivo de mídia e escolher um dos 3 modos de operação distintos:

1. **Transcrever (Idioma Original)**: Transcreve com precisão a fala no seu idioma original.
2. **Transcrever e Traduzir (Idioma de Destino)**: Transcreve a fala e a traduz para o idioma de destino configurado.
3. **Dublar e Traduzir (Idioma de Destino)** _(Apenas Gemini)_: Um recurso novo e poderoso que transcreve a fala, a traduz para o seu idioma de destino e sintetiza uma dublagem em áudio usando o mecanismo de TTS do complemento.

## 6. Leitor Avançado de Documentos e Imagens

O Vision Assistant Pro inclui um Leitor de Documentos altamente otimizado, projetado para PDFs de várias páginas, imagens complexas e até arquivos no formato HEIC do iPhone.

### 6.1 Processamento em Lote e Retomada

Você não precisa ler um documento enorme de uma só vez. Digite um intervalo de páginas (ex.: `1-20`) e a IA processará todas as páginas em segundo plano. Se o NVDA fechar ou você interromper a leitura, o complemento lembrará o seu progresso e oferecerá a opção de **Retomar** exatamente de onde parou!

### 6.2 Ação de Arquivo Inteligente

Nem sempre você precisa abrir o documento primeiro. No Explorador de Arquivos do Windows, basta selecionar um PDF ou imagem e pressionar **D** (Leitor de Documentos) ou **F** (Ação de Arquivo Inteligente) dentro da Camada de Comandos. O complemento ignorará instantaneamente a caixa de seleção de arquivo e começará a processar o item destacado.

### 6.3 Atalhos do Visualizador de Documentos

Quando a janela do Leitor de Documentos estiver aberta, você poderá usar os seguintes atalhos:

- **Ctrl + PageDown:** Vai para a próxima página.
- **Ctrl + PageUp:** Vai para a página anterior.
- **Alt + A:** Abre uma caixa de diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Força uma **Reanálise com IA** usando o seu provedor ativo.
- **Alt + G:** Gera e salva um arquivo de áudio de alta qualidade (WAV/MP3). _(Oculto se o provedor não suportar TTS)._
- **Alt + S / Ctrl + S:** Salva o texto extraído como um arquivo TXT ou HTML.

## 7. Rotulagem Semântica por IA e Explorador de IU

Preso em um aplicativo repleto de "botão não rotulado" por toda parte? O mecanismo de Rotulagem Semântica por IA resolve isso permanentemente.

### 7.1 Rotulagem Permanente de Objetos (L)

Foque o leitor de tela em um elemento gráfico ou botão sem rótulo e pressione **L** na Camada de Comandos. A IA examinará o botão visualmente, determinará sua função e aplicará um rótulo permanente.
_Diferente de ferramentas antigas de rotulagem em leitores de tela, este complemento usa um sistema híbrido avançado de "Assinatura de Objeto" (AutomationId/ControlID). Seus rótulos personalizados permanecerão intactos mesmo após o redimensionamento da janela, troca de monitor e atualizações do aplicativo!_

### 7.2 Escaneamento Completo do Aplicativo (Shift + L)

Pressione **Shift + L** para escanear toda a janela ativa de uma só vez. A IA encontrará todos os elementos não rotulados e os nomeará inteligentemente de uma só vez. Mais tarde, você poderá gerenciar, renomear ou excluir esses rótulos em lote por meio do Gerenciador de Rótulos integrado.

### 7.3 Explorador de IU (E)

Precisa interagir com um elemento sem navegar até ele manualmente? Pressione **E** para ativar o Explorador de IU. A IA escaneará a tela e gerará uma lista acessível de todos os elementos clicáveis (ignorando ruídos do sistema, como a barra de tarefas). Escolha um item da lista e o complemento clicará nele para você instantaneamente.

## 8. Assistente de Voz Ao Vivo

O Assistente Ao Vivo transforma o Vision Assistant Pro em um copiloto interativo em tempo real.
_(Nota: Este recurso é exclusivo do Google Gemini e de provedores Personalizados compatíveis com Gemini)._

- **Ativação:** Pressione **Control + L** na Camada de Comandos para abrir a caixa de diálogo do Assistente Ao Vivo.
- **Interação em Tempo Real:** Fale naturalmente através do seu microfone. A IA ouvirá sua voz e analisará a tela ativa simultaneamente. Você pode fazer perguntas como "O que estou vendo na tela?" ou "Leia o terceiro parágrafo para mim".
- **Personalização:** Na caixa de diálogo, você pode alterar o Estilo de Voz da IA (ex.: Profissional, Amigável, Animado) e ajustar sua "Profundidade de Raciocínio" para controlar o quão profundamente ela analisa as informações antes de responder.

## 9. Prompts Personalizados e Variáveis

Você pode gerenciar os prompts em **Configurações > Prompts > Gerenciar Prompts...**.

### Variáveis Suportadas

- `[selection]`: Texto selecionado no momento.
- `[clipboard]`: Conteúdo da área de transferência.
- `[clipboard_image]`: Imagem atualmente na área de transferência.
- `[screen_obj]`: Captura de tela do objeto navegador.
- `[screen_fg_obj]`: Captura de tela da janela ativa em primeiro plano.
- `[screen_full]`: Captura de tela inteira.
- `[file_ocr]`: Seleciona o arquivo de imagem/PDF para extração de texto.
- `[file_read]`: Seleciona o documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Seleciona o arquivo de áudio para análise (MP3, WAV, OGG).
- `{target_lang}`: Idioma de destino atual.
- `{source_lang}`: Idioma de origem atual.
- `{response_lang}`: Idioma de resposta da IA atual.
- `{swap_target}`: Idioma de alternância para a tradução por troca inteligente.
- `{swap_instruction}`: Bloco de instruções para a tradução por troca inteligente.

## 10. Casos de Uso Práticos (Qual recurso devo usar?)

O Vision Assistant Pro está repleto de ferramentas avançadas. Aqui estão alguns cenários comuns para ajudá-lo a escolher a opção certa:

- **Scenario: You want to understand the complete layout of a complicated window or inaccessible app.**
  _Solution:_ Press **O** (Full Screen Vision). The AI will analyze the entire screen and describe exactly where elements, texts, and buttons are positioned.

- **Scenario: You found an image on a webpage or an unlabeled graphic in a document.**
  _Solution:_ Move your navigator object to the graphic and press **V** (Object Vision). The AI will describe specifically what that image contains.

- **Scenario: You want to watch a movie or video clip with audio descriptions.**
  _Solution:_ Press **Shift + V** on your video and choose **"Generate Audio Description (SRT File)"**. When it finishes, click **"Generate Synced Narration (MP3)"** and select **"Extended AD"**. The add-on will create an audio track that intelligently pauses the movie's dialogue to describe the visual scenes.

- **Scenario: You encountered an app full of "unlabeled buttons".**
  _Solution:_ Press **L** to permanently label the specific button using AI. Or, press **Shift + L** to scan and label the entire window at once. If you just want to click something quickly, press **E** (UI Explorer) to get a list of all clickable items.

- **Scenario: You need to bypass an inaccessible CAPTCHA.**
  _Solution:_ Press **C** (CAPTCHA Solver). The AI will automatically capture the CAPTCHA, solve it, and inject the answer into the correct field.

- **Scenario: You want to read a long, 50-page PDF document.**
  _Solution:_ Press **D** (Document Reader), set your provider to Google Gemini, and enter the page range `1-50`. The add-on will extract the text accurately in the background.

- **Scenario: You are watching a silent video tutorial or animation on your screen.**
  _Solution:_ Press **Control + V** to start recording the screen. Let the tutorial play, then press **Control + V** again. The AI will explain exactly what was demonstrated.

- **Scenario: You encounter an unexpected error, API connection failure, or want to diagnose issues with custom local servers.**
  _Solution:_ Go to **Settings > Advanced**, check **"Enable dedicated log file"**, and set the **Log Level** to **"Debug"**. Perform the action again, then click **"Open Log File"** to inspect technical details or attach `vision_assistant.log` to a support ticket.

***
**Nota:** Uma conexão ativa com a internet é necessária para todos os recursos de IA. Documentos de várias páginas são processados automaticamente.

## 11. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, recursos e lançamentos:

- **Cana no Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **GitHub Issues:** Para relatórios de erros e solicitações de recursos.

### Relatando Erros e Logs

Ao abrir uma issue no GitHub ou solicitar suporte, inclua detalhes sobre o seu provedor de IA ativo, modelo e versão do NVDA. Se estiver enfrentando problemas de conexão ou encerramentos inesperados, ative o arquivo de log dedicado em **Configurações > Avançado**, reproduza o erro e anexe o arquivo `vision_assistant.log` para nos ajudar a resolver o problema mais rapidamente.

## 12. Apoiadores do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto por meio de suas generosas contribuições financeiras:

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **Apoiador Anônimo** (`UQDd...CnMY`)
- **leonardo0216**
- **Sergei Fleytin**
- **Suman Gayen**

_Se você deseja apoiar o projeto financeiramente e ver seu nome aqui, encontrará a opção **Doar** no menu Ferramentas do NVDA (sub-menu Vision Assistant) ou durante o processo de configuração após a instalação._

***

## Alterações da versão 2026.08.06

- **Rotulagem no Explorador de IU**: Agora você pode adicionar rótulos diretamente aos elementos encontrados dentro do Explorador de IU! Um novo botão "Adicionar Rótulo" foi incluído e a interface permanece aberta de forma inteligente, mantendo o foco para que você possa rotular rapidamente vários objetos sem interrupções.
- **Melhoria na Camada de Configurações Rápidas**: A camada do Vision Assistant (`Insert+Shift+V`) agora é persistente e altamente interativa! Você pode usar as setas `Para cima/Para baixo` para navegar entre as configurações rápidas (Provedor, Modelo, Idioma de Resposta da IA, Modelo de TTS) e as setas `Esquerda/Direita` para alterar instantaneamente seus valores com um retorno de voz inteligente e conciso. Suas seleções entram em vigor imediatamente (incluindo a ativação automática do roteamento avançado quando necessário) e a camada permanece ativa enquanto você configura.
- **Chat Direto (`Shift+C`)**: Adicionado um novo comando à camada! Pressione `Shift+C` para abrir instantaneamente uma janela de "Chat Direto". Isso fornece uma interface de conversa baseada em texto limpa e direta com a IA, sem precisar de uma imagem ou documento como ponto de partida.
- **Restauração Perfeita do Histórico de Chat**: Corrigido um erro crítico em que pressionar `Espaço` para relembrar o último resultado perdia o histórico subsequente da conversa. Agora, o complemento rastreia globalmente o seu bate-papo. Se você conversar, fechar a caixa de diálogo e pressionar `Espaço` para relembrá-la, todo o seu histórico de ida e volta será perfeitamente restaurado! Funciona para Chat Direto, Análise de Visão, Chat de Documentos e Tradução.
- **Descrições de Imagens no Corpo do Texto no OCR**: Adicionado um recurso opcional para descrever imagens integradas ao texto durante o OCR de documentos. Você pode alternar essa configuração nas opções de OCR do complemento, dentro do Leitor de Documentos antes da extração, ou rapidamente em tempo de execução na Camada de Configurações Rápidas.
- **Tradução de Voz (`Control+T`)**: Adicionado um novo e poderoso recurso! Dite o texto e a IA irá traduzi-lo e digitá-lo instantaneamente com base nos seus idiomas de origem e destino configurados.
- **Melhorias no Baixador de Atualizações**: A caixa de diálogo de download da atualização agora exibe corretamente o progresso em porcentagem, e um erro onde uma mensagem fantasma "Baixando atualização" aparecia ao cancelar a instalação foi corrigido.
- **Melhorias no Baixador do eSpeak-NG**: Adicionado o acompanhamento do progresso em porcentagem para os downloads do eSpeak-NG.
- **Resiliência do OCR em Lote**: Corrigido um problema no OCR de PDF em lote onde o processo parava se a chave de API ativa atingisse a cota na metade do caminho; agora ele alterna automaticamente para a próxima chave disponível e retoma o processo.
- **Suporte a CAPTCHA Visual**: Adicionado suporte robusto para a resolução de CAPTCHAs visuais. Ele tenta resolver automaticamente desafios de imagem complexos, como hCaptcha e reCAPTCHA, aprimorando significativamente a acessibilidade em formulários web desafiadores.
- **Reformulação do Transcritor de Áudio**: O módulo Transcritor de Áudio foi completamente reconstruído e agora suporta arquivos de áudio e vídeo. Ele possui 3 modos de operação distintos: "Transcrever (Idioma Original)", "Transcrever e Traduzir (Idioma de Destino)" e uma nova e poderosa opção "Dublar e Traduzir (Idioma de Destino)" (exclusiva para o Gemini) que gera uma dublagem em áudio traduzida da fala original.
- **Números de Página Opcionais no Leitor de Documentos**: Adicionada uma nova configuração para alternar a inclusão de números de página e separadores na saída de documentos com várias páginas. Você pode gerenciar facilmente essa opção nas configurações principais ou alterná-la rapidamente na Camada de Configurações Rápidas. Este recurso se aplica tanto à exportação de arquivos de texto/HTML quanto à janela "Exibir Formatado", permitindo ler documentos combinados perfeitamente.
- **Gemini Live TTS Ilimitado para Descrições de Vídeo**: Agora você pode selecionar "Gemini Live TTS" como o mecanismo de voz ao gerar a Narração de Áudio Sincronizada (MP3) para vídeos. Isso utiliza a API Gemini Live para sintetizar audiodescrições de alta qualidade, sem qualquer limite de caracteres ou restrições de duração.
- **Modularização da Base de Código**: A estrutura do complemento foi refatorada de um único arquivo para uma arquitetura modular multifuncional, visando melhorar a manutenção.
- **Reformulação da Interface de Configurações**: A caixa de diálogo de Configurações foi completamente redesenhada para usar uma interface moderna baseada em guias em vez de um layout agrupado, proporcionando melhor organização e navegação mais fácil, mantendo todas as opções existentes.
- **Registro Global e Dedicado em Arquivo**: Adicionado um sistema opcional de registro global em arquivo sob a nova guia de configurações "Avançado". Ele captura automaticamente eventos operacionais, tráfego da API e erros em todos os módulos do complemento em um arquivo dedicado (`vision_assistant.log`). Suporta níveis configuráveis de detalhamento do log (Depuração, Informação, Aviso, Erro), períodos de retenção automatizados (1 hora a 90 dias) e abertura ou limpeza direta do log a partir das configurações, com zero impacto no desempenho ou interferência nos logs do NVDA.
- **Acompanhamento do Progresso de Envio no Gemini**: Adicionados anúncios em tempo real do progresso em porcentagem ao enviar arquivos grandes (vídeo, áudio, documentos) para a API do Google Gemini.

## Alterações da versão 2026.07.15

- **Filtragem Inteligente de Modelos de API**: Reformulação completa do sistema de filtragem de modelos para usar uma abordagem puramente baseada em lista negra, em vez de listas brancas. Adicionadas palavras-chave de filtragem mais fortes (`embedding`, `bison`, `gecko`, `audio`, `realtime`, `babbage`, `moderation`, `deep`, `antigravity`, `computer`) para garantir que o menu suspenso do modelo de chat principal permaneça perfeitamente limpo e preparado para o futuro, mantendo todos os modelos especializados acessíveis na seção de Roteamento Avançado.
- **Pesquisa no Roteamento Avançado**: Todos os menus suspensos do Roteamento Avançado de Modelos (OCR, STT, TTS, Operador, Vídeo, Ao Vivo) e o seletor de variantes do eSpeak agora são totalmente pesquisáveis. Você pode digitar rapidamente para filtrar e encontrar o modelo ou variante desejado.
- **Novos Atalhos na Camada de Comandos**:
  - **Configurações (`Alt + S`)**: Abre instantaneamente a caixa de diálogo de configurações do Vision Assistant Pro.
  - **Relatório de Chaves Esgotadas (`Alt + Q`)**: Relata o número exato de chaves de API do Gemini que excederam sua cota diária, identificando em qual modelo específico elas foram esgotadas, e anuncia o tempo exato de redefinição.
  - **Auditoria de Roteamento (`Alt + M`)**: Audita e anuncia sua configuração atual do Roteamento Avançado, lendo quais modelos estão selecionados ativamente para tarefas especializadas (ignorando as configurações padrão).
- **Reformulação Completa do Analisador de Vídeo**: O Analisador de Vídeo foi completamente transformado! Anteriormente, ele apenas fornecia uma descrição básica de vídeos online. Agora, é uma suíte completa de processamento de vídeo adaptada para usuários cegos:
  - **Gravação de Tela Local (`Control+V`)**: Agora você pode gravar vídeos sem som diretamente da sua tela. A IA analisará o trecho gravado e fornecerá uma descrição altamente detalhada da cena, layout e ações.
  - **Geração de Audiodescrição (SRT)**: O complemento agora pode gerar roteiros de Audiodescrição altamente detalhados (no formato padrão SRT) para vídeos, com sincronização inteligente por intervalos para ancorar as descrições nas pausas naturais da faixa de áudio, além de OCR na íntegra para qualquer texto na tela.
  - **Narração de Áudio Sincronizada (Exportação em MP3)**: Além de legendas baseadas em texto, o complemento pode sintetizar a Audiodescrição em fala, misturá-la automaticamente com a faixa de áudio original do vídeo, aplicar audio ducking (redução do volume de fundo durante as descrições) e exportar o resultado final sincronizado como um arquivo MP3!
  - **Ação Inteligente em Arquivos de Vídeo**: Se você focar em um arquivo de vídeo local e pressionar o atalho de vídeo, o complemento o detectará automaticamente e processará o arquivo diretamente.
  - **Rastreamento Avançado de Personagens**: A IA agora realiza uma etapa prévia de extração de personagens. Ela constrói um dicionário global de personagens e os rastreia com precisão, segmento por segmento, sem confundir identidades.
  - **Configuração de Análise de Vídeo**: Adicionadas novas configurações para controlar o tamanho dos blocos de SRT, legendagem de personagens e avisos de isenção.
  - **Roteamento Estendido de Modelos**: Agora você pode selecionar explicitamente modelos de vídeo especializados (`gemini_video_model`, `custom_video_model`) nas configurações do Roteamento Avançado de Modelos.
- **Gerenciamento Inteligente de Cotas da API**: Tratamento aprimorado dos erros 429 (Limite Diário), rastreando cotas por modelo. Se uma chave atingir o limite diário em um modelo, ela será colocada em quarentena apenas para aquele modelo específico, deixando a chave disponível para uso com outros modelos.

## Alterações da versão 7.0.0

- **Retomada de Leituras Incompletas**: Adicionado um recurso de retomada para o Leitor de Documentos e para as Ações de Arquivo Inteligente. Se uma leitura for interrompida, agora você pode continuar de onde parou em vez de recomeçar do zero.
- **Nova Variável `[screen_fg_obj]`**: Adicionada uma variável de prompt personalizado para capturar uma tela apenas da janela ativa em primeiro plano, em vez da tela inteira.
- **Tentativas Inteligentes e Rotação de Chaves**: O complemento agora tenta novamente em segundo plano até 5 vezes usando a mesma chave ao encontrar sobrecargas temporárias no servidor (como "alta demanda" ou respostas malformatadas). Se as tentativas falharem, ele alterna automaticamente para a próxima chave de API da sua lista.
- **Detecção da Cortina de Tela**: Adicionada uma verificação para evitar a captura de tela quando a Cortina de Tela estiver ativa (seja ativada permanentemente ou alternada temporariamente por atalho). Ele exibirá um aviso e interromperá a ação, evitando o envio de imagens pretas e o desperdício de tokens de API.
- **Ajustes no Leitor de Documentos**: A caixa de diálogo de intervalo de PDF agora pré-seleciona automaticamente o idioma de destino padrão configurado no complemento. O gerenciamento de threads também foi aprimorado para garantir que tarefas em segundo plano sejam encerradas corretamente quando o leitor for fechado.
- **Integração Nativa com o OCR da Mistral**: Integrada a API nativa de OCR de Documentos da Mistral. Documentos de várias páginas são mesclados, enviados e processados em lote automaticamente usando o endpoint especializado `/v1/ocr` da Mistral, enquanto imagens de página única são processadas diretamente sem conversões desnecessárias para PDF [1].
- **Manipulação Dinâmica de URL Personalizada**: A modificação da URL personalizada da API agora limpa instantaneamente a lista de modelos em cache e restaura a caixa de texto para entrada manual. Isso garante compatibilidade total com endpoints personalizados (como o Cloudflare AI Gateway) que não suportam o endpoint padrão de listagem `/v1/models`.
- **Reformulação do Motor de Entrada do Operador de IA**: O sistema subjacente de simulação de mouse e teclado do Operador de IA foi completamente reescrito. A API legada `mouse_event` foi substituída pela API moderna `SendInput` do Windows, oferecendo compatibilidade significativamente maior com aplicativos modernos, janelas protegidas pelo UAC e telas de alta densidade (high-DPI).
- **Correção nas Operações de Arrastar e Soltar**: As ações de arrastar e soltar no Operador de IA agora são totalmente estáveis e confiáveis. O novo motor usa curvas suaves de aceleração, posicionamento preciso do cursor, temporização otimizada e uma técnica inteligente de toque para garantir que o Windows e os aplicativos reconheçam e executem gestos de arrastar e soltar sem falhar no meio do caminho.
- **Suporte a Múltiplos Monitores**: O Operador de IA agora suporta totalmente configurações com múltiplos monitores. Movimentos de mouse e cliques funcionam corretamente em todos os monitores usando a opção `MOUSEEVENTF_VIRTUALDESK`, garantindo um posicionamento preciso, independentemente de em qual monitor o aplicativo de destino esteja.
- **Simulação de Teclado Aprimorada**: Injeção de teclas aprimorada para suportar totalmente as "Teclas Estendidas" (como Setas, Home, End, Page Up/Down, Insert, Delete e F1-F12). Isso garante que os comandos de navegação e atalhos enviados pelo Operador de IA funcionem perfeitamente em todos os aplicativos.
- **Suporte a Imagens HEIC/HEIF**: Adicionado suporte nativo a formatos de foto do iPhone. Agora você pode selecionar diretamente arquivos `.heic` e `.heif` para descrição por IA, OCR ou Leitura de Documentos sem necessidade de conversão prévia.

## Alterações da versão 6.5.0

- **Assistente Ao Vivo**: Adicionado um recurso de assistente de voz e tela em tempo real, disponível exclusivamente para o provedor Google Gemini (ou provedores personalizados compatíveis com o Gemini). Inclui personalização interativa de voz e profundidade de raciocínio diretamente na caixa de diálogo, com reconexão automática ao alterar as configurações.
- **Provedor de IA MiniMax**: Integrado o MiniMax como provedor principal com suporte multimodal completo (chat, visão, OCR), TTS personalizado com mais de 300 vozes dinâmicas e remoção automática de blocos de raciocínio (ex.: `<think>...</think>`) das respostas.
- **Tradução no Visualizador de Documentos**: Corrigida uma falha silenciosa de tradução para usuários do NVDA em idiomas diferentes do inglês, garantindo que o código de idioma padrão de 2 letras seja enviado ao Google Tradutor em vez do nome do idioma localizado.
- **Tentativa de Leitura em Lote de PDF**: Implementada uma lógica de nova tentativa separada, silenciosa e altamente otimizada para o escaneamento em lote de documentos PDF, evitando uploads redundantes e janelas de erro incômodas durante as novas tentativas.
- **Status no Visualizador de Documentos**: Corrigido um erro onde o status geral do plugin (verificado via `I`) ficava preso em "Processamento em Lote Iniciado" durante leituras longas de documentos.
- **Correção de Falha de Threading**: Corrigida uma falha grave de asserção de thread `IsMain() failed in wxTimerImpl` ao abrir documentos a partir de uma thread em segundo plano, aplicando `wx.CallAfter` na fila de chamadas da interface gráfica.

## Alterações da versão 6.1.2

- **Pré-Verificação de Rótulos Duplicados**: Corrigido um problema na rotulagem individual onde a verificação de duplicados usava chaves de coordenadas antigas, fazendo com que o NVDA fizesse requisições duplicadas de IA para objetos já rotulados em vez de anunciar o rótulo existente.
- **Chat de Documentos para Provedores Não-Gemini**: Corrigida uma verificação rigorosa da chave de API no Chat de Documentos (`on_ask`) para garantir que usuários de provedores OpenAI, Groq ou Personalizados locais (como Ollama) possam conversar com documentos com sucesso, sem serem bloqueados.
- **Tradução Rápida no OCR do Chrome**: Restaurada a API de tradução gratuita e sem necessidade de chave para o OCR do Chrome. A tradução do texto extraído agora ignora a IA do Gemini, economizando cotas de API e acelerando o processo de tradução.
- **Filtro Alfanumérico de CAPTCHA**: Corrigida a lógica de filtragem no solucionador de CAPTCHA para garantir que caracteres não alfanuméricos sejam limpos corretamente em todas as situações.
- **Atualização na Ajuda da Camada de Comandos**: Corrigido o atalho de anúncio de status no menu de ajuda de `L` para `I`, e adicionados ambos os comandos de rotulagem (`L` e `Shift+L`) à lista.

## Alterações da versão 6.1.1

- **Correção na Saída do Raciocínio do Gemma 4**: Corrigido um problema nos modelos Gemma 4 onde todo o processo de raciocínio interno era exibido como resposta final, ou onde desativar o raciocínio resultava em respostas vazias. O complemento agora isola e extrai corretamente apenas a resposta limpa final.
- **OCR em Lote a Partir do Explorador de Arquivos**: Agora você pode selecionar várias fotos ou PDFs diretamente no Explorador de Arquivos do Windows e extrair texto ou analisá-los em lote. O complemento filtrará e processará automaticamente apenas os formatos de arquivo suportados.

## Alterações da versão 6.1.0

- **Integração Universal de IA Local (Configurar IA Local)**: Adicionado um novo botão **"Configurar IA Local"** nas Configurações do Provedor Personalizado. Agora os usuários podem configurar automaticamente e de forma instantânea motores de IA locais, incluindo **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP**.
- **Desvio Inteligente de Proxy Local**: Reconstruída a lógica de conexão com um mecanismo avançado de desvio de proxy. O complemento agora é inteligente o suficiente para ignorar completamente os proxies do sistema Windows em conexões de loopback local, garantindo conexões de IA locais estáveis mesmo com VPN ou modo TUN ativos.
- **Rotulagem por IA Ultra-Estável (v2)**: As chaves baseadas em coordenadas absolutas de tela foram substituídas por um sistema híbrido avançado de **Assinatura de Objeto**. Os rótulos agora dependem de identificadores programáticos (UIA **AutomationId** ou Win32 **ControlID**) e coordenadas relativas à janela, tornando seus rótulos personalizados totalmente imunes ao redimensionamento de janelas, movimentação, troca de monitor ou alteração de escala.
- **Migração Automática e Transparente de Rótulos**: A atualização é totalmente transparente. O complemento migrará automaticamente seus rótulos antigos baseados em coordenadas para o novo formato estável de assinatura em segundo plano assim que o elemento receber o primeiro foco, sem qualquer perda de dados.

## Alterações da versão 6.0

- **Apresentando a Rotulagem Semântica por IA**: Agora os usuários podem rotular permanentemente botões e ícones sem nome usando IA. Pressione **L** para rotular o objeto navegador atual (suportando tanto o foco do Tab quanto a navegação de objetos) ou **Shift+L** para escanear e rotular todo o aplicativo de uma só vez.
- **Gerenciamento Inteligente de Rótulos**: Adicionada uma nova caixa de diálogo para o Gerenciador de Rótulos, totalmente acessível (via **Shift+L** se já existirem rótulos), para visualizar, renomear ou excluir rótulos personalizados em lote.
- **Análise Direta de Arquivos (Ignorar Caixa de Diálogo)**: O complemento agora é inteligente o suficiente para detectar se você está focado em um arquivo PDF ou imagem no Explorador de Arquivos do Windows. Pressionar **F (Ação de Arquivo Inteligente)** ou **D (Leitor de Documentos)** no item selecionado irá processá-lo imediatamente, ignorando completamente a caixa de diálogo padrão "Abrir".

## Alterações da versão 5.6

- **Adicionado o Motor de OCR "Nenhum (Extrair Camada de Texto)"**: Agora os usuários podem extrair o texto diretamente de PDFs pesquisáveis sem gastar créditos de IA, melhorando significativamente a velocidade e a privacidade em documentos baseados em texto.
- **Precisão Aprimorada no Explorador de IU**: Melhorado o prompt do Explorador de IU para identificar melhor os tipos de elementos (como Itens de Lista) e relatar com precisão estados como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração Pós-Instalação**: Adicionada uma notificação após a instalação para guiar os usuários ao menu de configurações para definir suas chaves de API e preferências.

## Alterações da versão 5.5.2

- **Correção na Digitação do Operador de IA:** Resolvido um problema onde a letra 'v' era digitada em vez de colar o texto em determinados sistemas. Esta correção soluciona conflitos de temporização que ocorriam durante alto uso do sistema.
- **Estabilidade Aprimorada:** Adicionado um tratamento de erros robusto para operações na área de transferência para evitar travamentos do complemento quando a área de transferência do sistema estiver temporariamente bloqueada por outros aplicativos.
- **Otimização de Temporização:** Ajustados os atrasos internos para eventos de teclado para garantir maior confiabilidade em diferentes velocidades de sistema e melhor compatibilidade com gerenciadores de área de transferência de terceiros.

## Alterações da versão 5.5 (A Atualização de Automação)

- **Operador de IA (Controle Autônomo - Shift+A):** Esta é a grande novidade da v5.5. O Vision Assistant Pro deixou de ser apenas um assistente passivo para se tornar seu **Operador de IA** pessoal. Ele não apenas descreve a tela—ele assume o controle.
  - _Como funciona:_ Agora você pode dar instruções por escrito ou por voz para operar o seu PC. Por exemplo, em um aplicativo totalmente inacessível onde o seu leitor de tela permanece em silêncio, você pode pressionar **Shift+A** e digitar: _"Clique no botão Configurações"_ ou _"Encontre o campo de pesquisa, digite 'Últimas Notícias' e pressione Enter."_ A IA identifica os elementos visualmente, move o mouse e executa a tarefa para você.
  - _Nota de Desempenho:_ Este recurso é otimizado para o **Gemini 3.0 Flash (Preview)**, oferecendo respostas incrivelmente rápidas e inteligentes, capazes de lidar até mesmo com os layouts de interface mais complexos.
  - **⚠️ Aviso de Uso da API:** Como o Operador de IA precisa "ver" exatamente o que está acontecendo para ser preciso, ele envia uma captura de tela de alta resolução a cada etapa. Tenha em mente que o uso frequente consumirá sua cota de API muito mais rápido do que tarefas padrão baseadas em texto.
- **Explorador de IU Visual (E):** Cansado de navegar por "botões não rotulados"? Pressione **E** para ativar o Explorador de IU. A IA escaneará a janela inteira e gerará uma lista de todos os elementos clicáveis que encontrar—incluindo ícones, elementos gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele para você. É como ter uma "camada acessível" sobre qualquer aplicativo.
- **Ação de Arquivo Inteligente Reativa ao Contexto (F):** A tecla "F" foi completamente reformulada. Ela não presume mais que você deseja apenas o OCR. Ao selecionar uma única imagem, ela agora pergunta inteligentemente qual é a sua intenção: você pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração Estruturada de Texto (OCR)** para leitura. O menu se adapta dinamicamente com base no tipo de arquivo e no seu motor de IA ativo.
- **Otimização Principal:** Realizamos uma limpeza profunda na lógica interna do complemento, removendo funções antigas sem uso e códigos redundantes. O resultado é uma experiência mais leve, rápida e confiável para todos os usuários.

## Alterações da versão 5.0

- **Arquitetura Multiprovedor**: Adicionado suporte completo para **OpenAI**, **Groq** e **Mistral**, além do Google Gemini. Agora os usuários podem escolher seu provedor de IA preferido.
- **Roteamento Avançado de Modelos**: Usuários de provedores nativos (Gemini, OpenAI, etc.) agora podem selecionar modelos específicos em uma lista suspensa para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoints**: Usuários de provedores personalizados podem inserir manualmente URLs e nomes de modelos específicos para um controle detalhado sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de configurações e a interface do Leitor de Documentos agora ocultam automaticamente os recursos não suportados (como TTS) com base no provedor selecionado.
- **Obtenção Dinâmica de Modelos**: O complemento agora obtém a lista de modelos disponíveis diretamente da API do provedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR e Tradução Híbrida**: Otimizada a lógica para usar o Google Tradutor para maior rapidez ao utilizar o OCR do Chrome, e tradução via IA ao utilizar os motores Gemini/Groq/OpenAI.
- **"Reanalisar com IA" Universal**: O recurso de reanálise do Leitor de Documentos não está mais limitado ao Gemini. Agora ele utiliza qualquer provedor de IA que estiver ativo no momento para reprocessar as páginas.

## Alterações da versão 4.6

- **Restauração Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comandos, permitindo que os usuários reabram instantaneamente a última resposta da IA em uma janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" estiver ativo.

- **Central da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial do Telegram" no menu Ferramentas do NVDA, oferecendo um acesso rápido para se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica principal dos recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais fluida ao usar a saída direta de fala.
- **Instruções de Interface Melhoradas:** Atualizadas as descrições de configurações e a documentação para explicar melhor o novo sistema de restauração e como ele funciona em conjunto com as configurações de saída direta.

## Alterações da versão 4.5

- **Gerenciador Avançado de Prompts:** Introduzida uma caixa de diálogo dedicada nas configurações para personalizar os prompts padrão do sistema e gerenciar prompts definidos pelo usuário, com suporte completo para adicionar, editar, reordenar e pré-visualizar.

- **Suporte Abrangente a Proxy:** Resolvidos os problemas de conectividade de rede garantindo que as configurações de proxy definidas pelo usuário sejam aplicadas estritamente a todas as requisições de API, incluindo tradução, OCR e geração de fala.
- **Migração Automatizada de Dados:** Integrado um sistema inteligente de migração para atualizar automaticamente as configurações de prompts antigas para um formato JSON v2 robusto já na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima do NVDA necessária para 2025.1 devido a dependências de biblioteca em recursos avançados, como o Leitor de Documentos, garantindo um desempenho estável.
- **Interface de Configurações Otimizada:** A interface de configurações foi simplificada reorganizando o gerenciamento de prompts em uma caixa de diálogo separada, proporcionando uma experiência de uso mais limpa e acessível.
- **Guia de Variáveis de Prompt:** Adicionado um guia integrado nas caixas de diálogo de prompts para ajudar os usuários a identificar e usar facilmente variáveis dinâmicas, como [selection], [clipboard] e [screen_obj].

## Alterações da versão 4.0.3

- **Resiliência de Rede Aprimorada:** Adicionado um mecanismo de tentativa automática para lidar melhor com conexões de internet instáveis e erros temporários do servidor, garantindo respostas de IA mais confiáveis.

- **Janela de Tradução Visual:** Introduzida uma janela dedicada para resultados de tradução. Agora os usuários podem navegar facilmente e ler traduções longas linha por linha, de forma semelhante aos resultados de OCR.
- **Exibição Formatada Agregada:** O recurso "Exibir Formatado" no Leitor de Documentos agora exibe todas as páginas processadas em uma única janela organizada, com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Ignora automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e fluido.
- **Estabilidade de API Melhorada:** Alterado para um método de autenticação baseado em cabeçalho mais robusto, resolvendo possíveis erros de "Todas as chaves de API falharam" causados por conflitos na rotação de chaves.
- **Correção de Erros:** Resolvidos vários travamentos potenciais, incluindo um problema durante o encerramento do complemento e um erro de foco na caixa de diálogo do bate-papo.

## Alterações da versão 4.0.1

- **Leitor Avançado de Documentos:** Um visualizador novo e poderoso para PDF e imagens, com seleção de intervalo de páginas, processamento em segundo plano e navegação simples por `Ctrl+PageUp/PageDown`.

- **Novo Submenu no Menu Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" no menu Ferramentas do NVDA para um acesso mais rápido aos recursos principais, configurações e documentação.
- **Personalização Flexível:** Agora você pode escolher o motor de OCR de sua preferência e a voz do sintetizador diretamente no painel de configurações.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte a múltiplas chaves de API do Gemini. Você pode inserir uma chave por linha ou separá-las por vírgulas nas configurações.
- **Motor de OCR Alternativo:** Introduzido um novo motor de OCR para garantir um reconhecimento de texto confiável mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna e memoriza automaticamente a chave de API funcional mais rápida para contornar os limites de cota.
- **Documento para MP3/WAV:** Integrada a capacidade de gerar e salvar arquivos de áudio de alta qualidade nos formatos MP3 (128 kbps) e WAV diretamente no leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram usando suas URLs.
- **Suporte ao TikTok:** Introduzido o suporte para vídeos do TikTok, permitindo a descrição visual completa e a transcrição de áudio dos clipes.
- **Janela de Atualização Redesenhada:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as alterações da versão antes de instalar.
- **Interface e Status Unificados:** Padronizadas as caixas de seleção de arquivos em todo o complemento e aprimorado o comando 'L' para relatar o progresso em tempo real.

## Alterações da versão 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) na Camada de Comandos para fornecer uma lista de fácil acesso com todos os atalhos e suas funções.

- **Análise de Vídeo Online:** Suporte expandido para incluir vídeos do **Twitter (X)**. Também foram melhoradas a detecção de URL e a estabilidade para uma experiência mais confiável.
- **Contribuição para o Projeto:** Adicionada uma caixa de diálogo opcional de doação para usuários que desejarem apoiar atualizações futuras e o crescimento contínuo do projeto.

## Alterações da versão 3.5.0

\*   \*\*Camada de Comandos:\*\* Introduzido um sistema de Camada de Comandos (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestre. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido por `T`.
\*   \*\*Análise de Vídeo Online:\*\* Adicionado um novo recurso para analisar vídeos do YouTube e do Instagram diretamente fornecendo uma URL.

## Alterações da versão 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar a caixa de diálogo do bate-papo e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e direta.

- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações da versão 3.0

- **Novos Idiomas:** Adicionadas traduções para **persa** e **vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Grátis]`, `[Pro]`, `[Auto]`) para ajudar os usuários a distinguir entre modelos gratuitos e com limitação de taxa (pagos). Adicionado suporte ao **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Estabilidade do Ditado Inteligente melhorada significativamente. Adicionada uma verificação de segurança para ignorar trechos de áudio com menos de 1 segundo, evitando alucinações da IA e erros de resposta vazia.
- **Manipulação de Arquivos:** Corrigido um problema onde o envio de arquivos com nomes fora do padrão inglês falhava.
- **Otimização de Prompts:** Lógica de Tradução aprimorada e resultados de Visão estruturados.

## Alterações da versão 2.9

- **Adicionadas traduções para francês e turco.**
- **Exibição Formatada:** Adicionado o botão "Exibir Formatado" nas caixas de diálogo do bate-papo para visualizar a conversa com formatação adequada (Cabeçalhos, Negrito, Código) em uma janela de navegação padrão.
- **Configuração de Markdown:** Adicionada a nova opção "Limpar Markdown no Bate-papo" nas Configurações. Desmarcar essa opção permite aos usuários ver a sintaxe Markdown bruta (ex.: `**`, `#`) na janela do bate-papo.
- **Gerenciamento de Janelas:** Corrigido um erro onde a janela "Refinar Texto" ou do bate-papo abria várias vezes ou falhava ao obter o foco corretamente.
- **Melhorias de Usabilidade:** Padronizados os títulos das caixas de diálogo de arquivos para "Abrir" e removidos anúncios de fala redundantes (ex.: "Abrindo menu...") para uma navegação mais fluida.

## Alterações da versão 2.8

- Adicionada tradução em italiano.

- **Informa de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do complemento (ex.: "Enviando...", "Analisando...").
- **Exportação para HTML:** O botão "Salvar Conteúdo" nas caixas de diálogo de resultados agora salva a saída como um arquivo HTML formatado, preservando estilos como cabeçalhos e negrito.
- **Interface de Configurações:** Melhorado o layout do painel de Configurações com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte aos modelos gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado suporte ao idioma nepalês.
- **Lógica do Menu Refinar:** Corrigido um erro crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não estivesse em inglês.
- **Ditado:** Melhorada a detecção de silêncio para evitar saídas de texto incorretas quando nenhuma fala for capturada.
- **Configurações de Atualização:** A opção "Verificar atualizações ao iniciar" agora vem desativada por padrão para cumprir as políticas da Loja de Complementos.
- Limpeza de código.

## Alterações da versão 2.7

- Migrada a estrutura do projeto para o modelo oficial de complementos da NV Access para melhor conformidade com os padrões.

- Implementada a lógica de nova tentativa automática para erros HTTP 429 (Limite de Taxa) para garantir confiabilidade durante períodos de alto tráfego.
- Otimizados os prompts de tradução para maior precisão e melhor manipulação da lógica de "Troca Inteligente".
- Atualizada a tradução em russo.

## Alterações da versão 2.6

- Adicionado suporte à tradução em russo (Agradecimentos a nvda-ru).

- Mensagens de erro atualizadas para fornecer informações mais descritivas sobre problemas de conectividade.
- Alterado o idioma de destino padrão para inglês.

## Alterações da versão 2.5

- Adicionado Comando Nativo de OCR para Arquivos (NVDA+Control+Shift+F).

- Adicionado o botão "Salvar Bate-papo" nas caixas de diálogo de resultados.
- Implementado suporte completo de internacionalização (i18n).
- Migrados os sinais sonoros para o módulo nativo de tons do NVDA.
- Alternado para a Gemini File API para uma melhor manipulação de arquivos PDF e de áudio.
- Corrigido um travamento ao traduzir textos contendo chaves.

## Alterações da versão 2.1.1

- Corrigido um problema onde a variável [file_ocr] não funcionava corretamente nos Prompts Personalizados.

## Alterações da versão 2.1

- Padronizados todos os atalhos para usar NVDA+Control+Shift, eliminando conflitos com o layout de notebook do NVDA e atalhos do sistema.

## Alterações da versão 2.0

- Implementado sistema integrado de Atualização Automática.

- Adicionada Memória Cache para Tradução Inteligente, permitindo a recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar resultados contextualmente nas caixas de diálogo do bate-papo.
- Adicionado Comando Dedicado para Tradução da Área de Transferência (NVDA+Control+Shift+Y).
- Prompts da IA otimizados para impor rigorosamente a saída no idioma de destino.
- Corrigido travamento causado por caracteres especiais no texto de entrada.

## Alterações da versão 1.5

- Adicionado suporte a mais de 20 novos idiomas.

- Implementada Caixa de Diálogo Interativa para Refinar e fazer perguntas de acompanhamento.
- Adicionado o recurso Nativo de Ditado Inteligente.
- Adicionada a categoria "Vision Assistant" na caixa de diálogo Definir Comandos do NVDA.
- Corrigidos travamentos por COMError em aplicativos específicos, como Firefox e Word.
- Adicionado mecanismo de tentativa automática para erros de servidor.

## Alterações da versão 1.0

- Lançamento inicial.
