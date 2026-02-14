# Notebooks de Processamento de Linguagem Natural em Português

## 📚 Sobre esta Pasta
Esta pasta contém notebooks para experimentos com modelos de linguagem em português, focando no fine-tuning do BERTimbau e processamento de textos bíblicos.

## 📋 Notebooks Disponíveis

### 1. `bertimbau.ipynb` - Fine-tuning do BERTimbau
**Objetivo**: Fine-tuning do modelo BERTimbau (BERT em português) em textos bíblicos em português.

**Conteúdo**:
- Carregamento do modelo `neuralmind/bert-base-portuguese-cased`
- Pré-processamento de textos bíblicos em português
- Fine-tuning usando LoRA (Low-Rank Adaptation)
- Avaliação com métricas de perplexidade
- Geração de múltiplos checkpoints durante o treinamento

**Técnicas Utilizadas**:
- Masked Language Modeling (MLM)
- Parameter-Efficient Fine-Tuning (PEFT) com LoRA
- Gradient accumulation para treinamento eficiente
- Early stopping baseado em loss de validação

**Resultados Esperados**:
- Redução de 35% na perplexidade em relação ao modelo base
- Múltiplos checkpoints salvos (15 a 3104 steps)
- Modelo adaptado para linguagem religiosa em português

### 2. `treino_atos.ipynb` - Treinamento em Textos de Atos
**Objetivo**: Treinamento específico em textos do livro de Atos dos Apóstolos.

**Conteúdo**:
- Processamento do arquivo `atos.txt`
- Tokenização específica para textos bíblicos
- Treinamento com parâmetros otimizados
- Análise de resultados por capítulo

**Dados Utilizados**:
- Texto completo do livro de Atos (28 capítulos)
- Divisão em versículos para treinamento
- Validação cruzada por capítulo

**Aplicações**:
- Análise de estilo literário
- Geração de texto bíblico
- Classificação de passagens

## 🛠️ Pré-requisitos

### Dependências
```python
# Instaladas no ambiente Docker
transformers >= 4.36.0
datasets >= 2.16.0
peft >= 0.7.0
accelerate >= 0.26.0
torch >= 2.9.1
```

### Recursos Necessários
- **GPU**: NVIDIA com pelo menos 8GB VRAM (recomendado)
- **RAM**: 16GB mínimo, 32GB recomendado
- **Armazenamento**: 10GB para modelos e dados

## 📊 Estrutura de Dados

### Arquivos de Texto
- `biblia.txt`: Texto bíblico completo em português
- `biblia_normalizada.txt`: Versão normalizada (sem números, pontuação)
- `atos.txt`: Livro de Atos dos Apóstolos
- `fonte.txt`: Metadados e fontes dos textos
- `nao_biblico.txt`: Textos não-bíblicos para contraste

### Pastas de Resultados
- `results_bertimbau_ft/`: Checkpoints do fine-tuning
- `results_mistral_book/`: Resultados com modelo Mistral

## 🚀 Como Executar

### Opção 1: Via Jupyter Lab
1. Acesse `http://localhost:8888`
2. Navegue até `notebooks/livro/`
3. Abra o notebook desejado
4. Execute todas as células (Kernel → Restart & Run All)

### Opção 2: Via Script
```bash
# Executar fine-tuning do BERTimbau
python scripts/run_experiment.py --notebook livro/bertimbau.ipynb

# Executar treino em Atos
python scripts/run_experiment.py --notebook livro/treino_atos.ipynb
```

## 📈 Métricas de Avaliação

### Para Fine-tuning
1. **Perplexidade**: Medida de quão bem o modelo prevê o texto
2. **Loss de Treinamento**: Redução ao longo das épocas
3. **Loss de Validação**: Generalização para dados não vistos
4. **Acurácia de Tokens Mascarados**: Precisão nas previsões

### Para Treinamento Específico
1. **Acurácia por Capítulo**
2. **Consistência Temática**
3. **Coerência de Geração**

## 💾 Salvamento de Resultados

### Checkpoints
Os modelos são salvos em intervalos regulares:
- A cada 100 steps durante treinamento longo
- No final de cada época
- Quando há melhoria na loss de validação

### Estrutura de Checkpoints
```
results_bertimbau_ft/
├── checkpoint-15/
├── checkpoint-100/
├── checkpoint-3104/
└── (outros checkpoints)
```

## 🔬 Experimentos Sugeridos

### 1. Variação de Hiperparâmetros
- Testar diferentes taxas de aprendizado
- Variar tamanho de batch
- Experimentar diferentes configurações de LoRA

### 2. Transfer Learning
- Fine-tuning em outros gêneros textuais
- Adaptação para português contemporâneo
- Combinação com outros modelos

### 3. Análise Comparativa
- Comparar BERTimbau com BERT multilíngue
- Avaliar impacto do tamanho do dataset
- Medir ganhos com pré-treinamento específico

## 📚 Referências

### Modelos
- **BERTimbau**: Souza et al. (2020) - BERT pré-treinado para português brasileiro
- **LoRA**: Hu et al. (2021) - Low-Rank Adaptation of Large Language Models

### Bibliotecas
- **Hugging Face Transformers**: Wolf et al. (2020)
- **PEFT Library**: Mangrulkar et al. (2022)

### Datasets
- Textos bíblicos em português (domínio público)
- Processamento personalizado para NLP

## ⚠️ Limitações e Considerações

### Técnicas
- Fine-tuning requer GPU para treinamento eficiente
- LoRA reduz parâmetros treináveis, mas mantém qualidade
- Textos bíblicos têm vocabulário específico

### Éticas
- Uso responsável de textos religiosos
- Respeito a contextos culturais e religiosos
- Transparência nas aplicações

## 🤝 Contribuições

Para contribuir com novos experimentos:
1. Crie um novo notebook com nome descritivo
2. Documente metodologia e resultados
3. Adicione referências relevantes
4. Submeta pull request

## 📧 Contato

Para dúvidas sobre estes experimentos:
- **Autor**: Erky Lima
- **Email**: contato@erky.com.br
- **Repositório**: https://github.com/erkylima/bert-ml-lab

---

**Última Atualização**: Fevereiro 2026
**Versão**: 1.0.0  
**Status**: Experimentos Ativos