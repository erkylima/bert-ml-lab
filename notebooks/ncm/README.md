# Next-Concept Modeling (NCM) no laboratório

Este diretório reúne experimentos com **Next-Concept Modeling (NCM)** em um ambiente local com uma NVIDIA RTX 3060 Ti de 8 GB.

O objetivo é investigar se uma arquitetura coarse-to-fine pode gerar texto e código com menos passos sequenciais que uma LLM autoregressiva tradicional.

Este README documenta o conhecimento acumulado até o momento. Ele não representa a existência de um modelo pronto para produção.

## Índice

- [O que é NCM](#o-que-é-ncm)
- [Arquitetura em duas etapas](#arquitetura-em-duas-etapas)
- [Notebooks existentes](#notebooks-existentes)
- [Experimento de código Python](#experimento-de-código-python)
- [Estado atual do Stage 1](#estado-atual-do-stage-1)
- [Estado atual do Stage 2](#estado-atual-do-stage-2)
- [Hardware local](#hardware-local)
- [Plano para português brasileiro](#plano-para-português-brasileiro)
- [Plano para código Python](#plano-para-código-python)
- [Hiperparâmetros](#hiperparâmetros)
- [Avaliação](#avaliação)
- [Treinamento em hardware alugado](#treinamento-em-hardware-alugado)
- [O que os treinamentos atuais ajudam](#o-que-os-treinamentos-atuais-ajudam)
- [Limitações conhecidas](#limitações-conhecidas)
- [Metas](#metas)

---

## O que é NCM

Next-Concept Modeling é uma arquitetura que gera texto coarse-to-fine.

Em vez de prever um token por vez, como uma LLM autoregressiva, o NCM gera uma hierarquia de códigos discretos:

```text
nível grosso
    ↓
estrutura mais detalhada
    ↓
detalhes finos
    ↓
decodificador produz texto ou código
```

Dentro de um nível, todos os códigos são gerados em paralelo. Entre níveis, existe uma ordem sequencial curta.

Pense no processo como construir um desenho:

1. primeiro a estrutura;
2. depois formas;
3. depois detalhes;
4. por fim, o resultado final.

O NCM não verifica automaticamente todos os caminhos possíveis ou executa o código a cada refinamento. Ele aprende uma hierarquia de representações e as gera em ordem.

---

## Arquitetura em duas etapas

```text
texto/código
      ↓
VQ-VAE encoder
      ↓
códigos discretos em níveis
      ↓
gerador NCM
      ↓
códigos previstos
      ↓
VQ-VAE decoder
      ↓
tokens GPT-2
      ↓
texto/código final
```

### Stage 1: VQ-VAE

O **VQ-VAE** aprende uma representação discreta hierárquica:

1. encoder transforma texto em vetores;
2. vetores são substituídos pelos códigos mais próximos de um codebook;
3. códigos são organizados em vários níveis residuais;
4. decoder tenta reconstruir o texto original;
5. pesos são ajustados para melhorar essa reconstrução.

É possível comparar o VQ-VAE a um JPEG para linguagem:

- níveis grossos carregam estrutura global;
- níveis intermediários adicionam organização;
- níveis finos recuperam detalhes;
- o decoder reconstrói a saída final.

Um codebook é um vocabulário interno aprendido pelo modelo. Cada código inteiro corresponde a uma representação do codebook.

### Quantização residual

O primeiro nível representa uma aproximação grosseira.

Os níveis seguintes representam os erros restantes:

```text
reconstrução 0
    + código do nível 1
    + código do nível 2
    + código do nível 3
    ↓
reconstrução final
```

Cada nível corrige parte da reconstrução anterior.

### Stage 2: gerador

O gerador aprende a prever os códigos da hierarquia.

Ele recebe:

- prefixo do problema ou pergunta;
- contexto anterior;
- cumulativa dos níveis já gerados.

Ele produz:

- todos os códigos de um nível em paralelo;
- cada nível seguinte em uma passagem;
- uma hierarquia completa.

O VQ-VAE então decodifica esses códigos em texto ou código.

---

## Por que usar VQ-VAE

O NCM precisa de representações discretas organizadas em uma hierarquia crescente.

Um embedding contínuo comum não fornece diretamente:

- códigos discretos;
- residual entre níveis;
- níveis sucessivamente maiores;
- um formato compatível com o gerador;
- uma reconstrução do texto original.

Um encoder de LLM existente poderia fornecer vetores melhores, mas normalmente não teria:

- codebooks;
- quantização residual;
- hierarquia coarse-to-fine;
- decoder compatível;
- treinamento calibrado para o gerador.

Usar o VQ-VAE oficial como inicialização permite adaptação de domínio por transfer learning.

Também permite congelar o codec depois do Stage 1 e treinar apenas o gerador no Stage 2.

---

## Notebooks existentes

### `treino_ncm_codigo_python.ipynb`

Notebook de adaptação experimental para código Python.

Ele contém:

- carregamento do repositório oficial;
- checkpoint XSum;
- MBPP;
- recorte de CodeSearchNet Python;
- diagnóstico do VQ-VAE;
- Stage 1 para código;
- Stage 2 para geração Python;
- inferência;
- AST e sintaxe;
- checkpoints por época.

Este notebook não deve ser substituído ou reinicializado durante uma execução ativa.

### `ncm-ptbr.ipynb`

Notebook operacional preparado para o próximo plano em português brasileiro.

Ele contém:

- objetivos e gates;
- limites para RTX 3060 Ti;
- consulta aos corpora PT-BR;
- mistura piloto;
- filtros;
- Stage 1 de adaptação VQ-VAE;
- Stage 2 de instrução;
- métricas de raciocínio;
- benchmark;
- inferência em português;
- flags de treino desativados por padrão.

O notebook PT-BR não foi criado para substituir o notebook Python.

---

## Experimento de código Python

### Base oficial

O experimento usa:

- commit `c70274273f489abc73832b2b98584a8483b6b203`;
- repositório oficial HazyResearch/NCM;
- checkpoint XSum;
- GTX/RTX local com CUDA.

O tamanho registrado foi:

| Componente | Parâmetros |
|---|---:|
| VQ-VAE | 60,63 M |
| Gerador | 88,02 M |
| Total aproximado | 148,65 M |

### Corpus Python

O corpus combina:

- MBPP sanitized;
- recorte de CodeSearchNet Python.

O tamanho observado no notebook foi:

- treino: aproximadamente 127 itens no corpus pequeno descrito inicialmente;
- corpus expandido: 55.944 pares gerador;
- validação: aproximadamente 27 itens no conjunto inicial;
- teste: aproximadamente 28 itens no conjunto inicial.

Os números podem variar conforme o streaming e o corpus completo usado pelo notebook.

O texto não é normalizado agressivamente:

- indentação preservada;
- quebras de linha preservadas;
- pontuação preservada;
- blocos nativos de 48 tokens.

### Preparação do exemplo

Um exemplo se torna pares aproximadamente assim:

```text
prompt
    + blocos anteriores
    ↓
prefixo

código atual
    ↓
block size 48
    ↓
códigos NCM
```

O gerador prevê a hierarquia do bloco atual usando o prompt e os blocos anteriores.

---

## Estado atual do Stage 1

No experimento Python, o Stage 1 adaptou o VQ-VAE XSum a código.

O diagnóstico inicial em 100 exemplos foi:

| Métrica | Baseline XSum |
|---|---:|
| Token accuracy | 88,22% |
| Exact block rate | 1,70% |
| Syntax valid rate | 0% |
| Indentation exact | 13% |

Exemplo registrado ao final das primeiras épocas:

| Época | Token accuracy | Exact block | Syntax valid | Indentation |
|---|---:|---:|---:|---:|
| 1 | 89,62% | 4,42% | 0% | 31% |
| 2 | 96,79% | 34,35% | 8% | 77% |
| 3 | 97,87% | 43,88% | 11% | 90% |
| 4 | 98,34% | 52,72% | 10% | 88% |
| 5 | 98,61% | 59,52% | 13% | 95% |
| 7 | 98,77% | 64,29% | 13% | 96% |
| 8 | 98,89% | 68,37% | 11% | 98% |

Esses números mostram melhoria clara na reconstrução token a token e na indentação.

Eles não mostram que o modelo produziu código correto ou funcional.

O Stage 1 é um ajuste do codec, não um modelo inteligente de programação.

---

## Estado atual do Stage 2

O Stage 2 treina somente o gerador com o VQ-VAE adaptado.

Configuração registrada:

```text
BATCH_SIZE = 1
ACCUMULATION_STEPS = 8
LEARNING_RATE = 5e-5
TOTAL_EPOCHS = 20
MAX_TRAIN_ITEMS = len(generator_train_items)
PATIENCE = 12
```

O conjunto expandido chegou a aproximadamente 55.944 pares gerador.

Na época 1:

- treino chegou ao passo 55.944;
- treino loss: aproximadamente 3,7713;
- validation loss: aproximadamente 2,7029.

A época 1 levou cerca de uma hora na RTX 3060 Ti.

Estimativa aproximada:

- 20 épocas completas: cerca de 20 horas;
- 10 épocas: cerca de 10 horas;
- uma época pode variar conforme carga, kernel, validação e checkpoint;
- parada antecipada pode encurtar ou cancelar o restante.

Uma validation loss menor é melhor.

Uma loss próxima de 0,5 não é uma meta universal:

- depende dos codebooks;
- depende da hierarquia;
- depende da distribuição dos dados;
- depende da perda;
- não representa diretamente Pass@k;
- não garante código sintático ou funcional.

A métrica decisiva é combinação de:

- validation loss;
- AST válido;
- testes executáveis;
- Pass@k;
- indentação;
- qualidade qualitativa;
- repetição.

### Forward

Forward é quando os dados atravessam o modelo:

```text
entrada
    ↓
pesos atuais
    ↓
logits previstos
    ↓
loss
```

O forward não altera os pesos.

Ele é semelhante a o modelo responder uma questão.

### Backward

Backward calcula como cada peso contribuiu para o erro:

```text
loss
    ↓
derivadas
    ↓
gradientes
```

Depois, o otimizador usa os gradientes para ajustar os pesos.

Sequência:

```text
forward → loss → backward → atualização
```

Forward e backward são executados várias vezes entre uma atualização devido à acumulação.

---

## Hardware local

### RTX 3060 Ti

- VRAM: 8 GB;
- CUDA;
- BF16 ou FP16 conforme suporte;
- batch pequeno;
- acumulação de gradiente;
- checkpoint frequente.

Limites iniciais seguros:

```text
BATCH_SIZE = 1 ou 2
ACCUMULATION_STEPS = 8
prefixo = 512
blocos = 48
máximo piloto = 128–256 tokens
```

Não é necessário e nem saudável tentar preencher toda a VRAM.

O Stage 1 do VQ-VAE conseguiu treinamentos com cerca de 2–3 GB de VRAM em partes da execução.

O uso real depende de:

- batch;
- sequência;
- tamanho dos logits;
- GradScaler;
- dtype;
- ativações;
- kernel;
- estado do otimizador.

### RTX 5090 com 32 GB

Uma RTX 5090 seria útil para:

- batch maior;
- contextos maiores;
- modelos maiores;
- menos necessidade de acumulação;
- paralelismo real;
- modelos próximos de 300–725 M;
- iteração mais rápida.

A VRAM 4× maior não garante treinamento 4× mais rápido.

VRAM permite tentar batches maiores, mas:

- throughput pode aumentar;
- tempo por exemplo pode cair;
- learning rate pode exigir ajuste;
- kernels ainda podem ser limitados;
- CPU pode continuar sendo gargalo;
- logits/codebooks podem crescer.

Uma configuração equivalente de batch efetivo 8 seria:

```text
batch 1 + acumulação 8
batch 2 + acumulação 4
batch 4 + acumulação 2
batch 8 + acumulação 1
```

O batch físico maior tende a ser mais eficiente em uma GPU moderna, mas deve ser comparado pela métrica de exemplos por segundo.

---

## Plano para português brasileiro

Os dados candidatos são:

- `carolina-c4ai/corpus-carolina`;
- `carolina-c4ai/carol-subcorpora`;
- `cnmoro/smoltalk-555k-ptbr`;
- `cnmoro/reasoning-v1-20m-portuguese`.

### Carolina

Carolina é um corpus:

- brasileiro;
- contemporâneo;
- diverso;
- com várias tipologias;
- com múltiplas licenças internas;
- cerca de 1–10 bilhões de elementos/tokens/itens dependendo da versão.

Para o piloto, usar:

- Carol·B;
- Carol·(D+B);
- subcorpus deduplicado.

O modo Carol·(D+B) reduz duplicação entre domínios.

Antes de treinar:

- remover XML/metadata exposto;
- remover vazio;
- remover textos curtos;
- remover duplicatas;
- remover quase duplicatas;
- filtrar caracteres;
- normalizar Unicode;
- separar por documento;
- manter split congelado.

### SmolTalk PT-BR

Contém cerca de 556 mil registros.

É composto por:

- instruções;
- perguntas;
- respostas;
- reescrita;
- classificação;
- resumo;
- conversa.

Os registros precisam ser convertidos para prefixo/alvo consistentes.

Exemplo:

```text
<sistema>
instrução

<usuário>
pergunta

<assistente>
resposta
```

### Reasoning PT-BR

Contém aproximadamente 20,9 milhões de registros.

Cada registro pode possuir:

- prompt;
- thought;
- answer.

O dataset é uma tradução sintética/de domínio amplo.

Limitações observadas:

- traduções podem ser artificiais;
- português pode misturar inglês;
- pensamentos podem ser enormes;
- respostas podem conter conteúdo factual incorreto;
- registros repetidos podem existir;
- qualidade não é uniforme.

O piloto não deve usar os 20,9 milhões integralmente.

### Mistura piloto

Mistura inicial recomendada:

```text
70% Carolina
20% SmolTalk
10% raciocínio
```

Meta piloto:

- 300–500 milhões de tokens;
- não mais que 256 tokens alvo inicialmente;
- prefixo 512;
- 128–256 contextos experimentais;
- corpus de validação separado.

### Jornada PT-BR

```text
Gate A: vocabulário português decodifica corretamente
Gate B: Stage 1 melhora reconstrução de Carolina
Gate C: perplexidade/loss cai em Carolina
Gate D: instruções curtas são coerentes
Gate E: raciocínio curto passa em problemas verificáveis
Gate F: VRAM e throughput são aceitáveis
```

Não avançar ao piloto completo sem:

- métricas registradas;
- baseline;
- validação humana;
- checkpoint persistente;
- corpus congelado.

### Formato recomendado

```json
{
  "source": "carolina|smoltalk|reasoning",
  "prefix": "texto de contexto",
  "target": "texto esperado",
  "quality": "score",
  "dedup_key": "hash"
}
```

---

## Plano para código Python

### Stage 1

Objetivo:

```text
melhorar reconstrução de código pelo VQ-VAE
```

Dados:

- MBPP;
- CodeSearchNet;
- repositórios licenciados;
- data cleaning;
- AST válido.

### Stage 2

Objetivo:

```text
gerar a hierarquia que decodifica Python correto
```

Dados:

- prompt;
- código completo;
- blocos anteriores;
- bloco alvo;
- testes.

### Validação necessária

Não medir apenas loss.

Executar:

```text
ast.parse
compile
execução segura
testes unitários
Pass@k
taxa de indentação
taxa de sintaxe
taxa de nomes válidos
tempo por solução
```

Aceitar dados sintéticos somente depois de:

1. executar o modelo;
2. compilar;
3. executar testes;
4. verificar resultado;
5. remover duplicata;
6. separar origem;
7. registrar prompt.

Não existe dataset sintético automático nos notebooks atuais.

---

## Hiperparâmetros

### Learning rate

É o tamanho do ajuste aplicado aos pesos.

Exemplo:

```text
LEARNING_RATE = 5e-5
```

Equivale a `0.00005`.

- muito alto: instabilidade;
- muito baixo: aprendizagem lenta;
- deve ser ajustado após comparação.

### Batch size

É o número de exemplos processados antes da atualização.

Com:

```text
BATCH_SIZE = 1
```

um exemplo entra por vez na GPU.

Batch maior:

- usa mais VRAM;
- tende a usar CUDA com mais eficiência;
- pode exigir learning rate maior;
- pode mudar a convergência.

### Accumulation steps

Permite simular um batch maior sem armazenar todos os exemplos ao mesmo tempo.

```text
BATCH_SIZE = 1
ACCUMULATION_STEPS = 8
```

Batch efetivo:

```text
1 × 8 = 8 exemplos por atualização
```

O forward/backward ocorre oito vezes antes da atualização dos pesos.

### Max train items

Limita quantos itens entram em uma época.

No Stage 2 atual:

```text
MAX_TRAIN_ITEMS = len(generator_train_items)
```

Assim, usa-se o conjunto inteiro expandido.

Em um piloto pode ser reduzido.

### Patience

Define quantas épocas podem ocorrer sem uma nova melhor validation loss.

```text
PATIENCE = 12
```

Se 12 épocas consecutivas não melhorarem o melhor resultado:

- a execução para antecipadamente;
- checkpoint `best.pt` é preservado.

`PATIENCE` não altera o máximo de épocas.

---

## Avaliação

### VQ-VAE

Métricas mínimas:

- token accuracy;
- exact block rate;
- texto reconstruído;
- caracteres portugueses preservados;
- acentos preservados;
- indentação;
- syntax valid;
- codebook utilization.

Gate prático:

```text
melhorar o baseline XSum
e não degradar reconstrução em inglês
```

### Gerador

Métricas mínimas:

- train loss;
- validation loss;
- perplexidade;
- sintaxe;
- execução;
- testes;
- repetição;
- diversidade;
- aderência ao prompt;
- velocidade.

### PT-BR

Separar em:

- Carolina: loss/perplexidade;
- SmolTalk: aderência;
- Reasoning: respostas verificáveis;
- Português: gramática e mistura com inglês;
- Humano: coerência.

### Conjuntos

- treino: 94%;
- validação: 3%;
- teste: 3%;
- sem overlap por documento;
- sem duplicata;
- sem vazamento de prompt.

---

## Treinamento em hardware alugado

Uma GPU com 32 GB pode ser útil para validar uma escala maior.

Pré-requisitos:

- `tokenizer.pt`;
- `generator.pt`;
- `config.yaml`;
- manifest dos datasets;
- hash dos pesos;
- seed;
- logs;
- versão exata do repositório;
- dependências fixadas;
- storage persistente;
- checkpoints por etapa.

Estratégia econômica:

1. benchmark curto;
2. modelo piloto 300 M;
3. validar loss;
4. avaliar Português/Python;
5. expandir para 700 M;
6. baixar checkpoint;
7. desligar instância imediatamente;
8. testar inferência local.

Não iniciar pelo corpus completo antes de validar:

- dados;
- separação;
- codec;
- smoke test;
- VRAM;
- throughput.

### Inferência na 3060 Ti

É possível que pesos próximos de 700 M caibam em 8 GB em FP16 com batch 1.

Estimativa teórica:

- pesos FP16: cerca de 1,4 GB;
- contexto, VQ-VAE, buffers e logits elevam o consumo;
- batch 1 provável;
- batch maior incerto;
- quantização pode ser necessária;
- qualidade da quantização deve ser validada.

Não quantizar antes de medir:

- AST;
- Pass@k;
- acurácia;
- velocidade;
- coerência;
- repetição.

---

## O que os treinamentos atuais ajudam

### Reutilizável

- pipeline Stage 1;
- pipeline Stage 2;
- batch/acumulação;
- checkpoints;
- smoke test;
- métricas;
- configuração CUDA;
- gerador VQ-VAE compatível;
- experiência em CodeSearchNet/MBPP.

### Não reutilizável diretamente para PT-BR

- pesos VQ-VAE especializados em Python;
- gerador especializado em Python;
- checkpoint XSum engloba um domínio inglês.

Para português, o caminho mais seguro é:

1. usar XSum como baseline;
2. adaptar VQ-VAE ao português;
3. congelar o novo codec;
4. treinar o gerador PT-BR.

Os pesos Python podem ajudar como inicialização opcional, mas não devem ser misturados ao português sem teste.

---

## Limitações conhecidas

- NCM não é um chat model pronto;
- não existem resultados públicos de NCM generalista em 700 M;
- benchmarks oficiais não medem instrução geral;
- velocidade depende do hardware;
- geração hierárquica pode acumular erros;
- o VQ-VAE pode perder detalhes;
- codebooks podem colapsar;
- o checkpoint XSum não representa português corretamente;
- o dataset PT-BR pode conter tradução artificial;
- 300–500 milhões de tokens são apenas piloto;
- gerar dados sintéticos pode ampliar erros;
- modelos maiores não garantem qualidade.

---

## Metas

### Meta curta

- finalizar o Stage 2 Python;
- medir validation loss;
- medir AST válida;
- medir execução MBPP;
- registrar Pass@k;
- criar checkpoint `best.pt`;
- documentar throughput.

### Meta do piloto local

- adaptar VQ-VAE a PT-BR;
- treinar gerador de aproximadamente 100 M;
- validar Carolina;
- validar SmolTalk;
- validar raciocínio curto;
- medir VRAM e throughput.

### Meta intermediária

- gerar 300 M tokens;
- pilotar modelo 300 M;
- comparar com baseline autoregressivo;
- medir velocidade real;
- medir qualidade em português e código.

### Meta de escala

- validar modelo até cerca de 700 M;
- usar hardware 32 GB;
- manter inferência possível em 8 GB;
- construir modelo PT-BR multimodal de tarefa;
- somente depois considerar corpus completo e sintético.

### Critério final

Avançar apenas se houver:

```text
melhor qualidade
  + menor custo por geração
  + menor dependência de passos
  + operação estável
  + saída verificável
  + inferência viável localmente
```
