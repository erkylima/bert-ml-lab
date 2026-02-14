# Laboratório de Machine Learning BERT - Publicação de Experimentos Científicos

## 📋 Visão Geral

Este repositório contém um laboratório abrangente de machine learning focado no processamento de linguagem natural em português usando modelos BERT. O projeto inclui experimentos com BERTimbau (BERT em português), análise de sentimentos, classificação de texto e técnicas de fine-tuning.

## 🎯 Objetivos de Pesquisa

1. **Modelagem de Linguagem em Português**: Fine-tuning do BERTimbau para compreensão de texto em português
2. **Análise de Sentimentos**: Construção de classificadores de sentimentos para texto em português
3. **Transfer Learning**: Exploração de LoRA (Low-Rank Adaptation) para fine-tuning eficiente
4. **Pesquisa Reproduzível**: Criação de um ambiente de experimentação ML totalmente reproduzível

## 🏗️ Estrutura do Projeto

```
bert-ml-lab/
├── notebooks/              # Notebooks Jupyter com experimentos
│   ├── livro/             # Experimentos de fine-tuning do BERTimbau
│   ├── sentimentos/       # Experimentos de análise de sentimentos  
│   ├── neuralRag/         # Experimentos de RAG Neural
│   └── imagens/          # Experimentos de visão computacional
├── data/                  # Datasets e dados processados
├── models/               # Checkpoints de modelos treinados
├── scripts/              # Scripts utilitários e pipelines
├── config/               # Arquivos de configuração
├── docs/                 # Documentação e notas de pesquisa
└── results/              # Resultados de experimentos e métricas
```

## 🚀 Início Rápido

### Pré-requisitos
- Docker e Docker Compose
- GPU NVIDIA com suporte a CUDA (recomendado)
- 16GB+ de RAM

### Executando o Laboratório

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/erkylima/bert-ml-lab.git
   cd bert-ml-lab
   ```

2. **Configure o ambiente**:
   ```bash
   cp .env.example .env
   # Edite .env com suas configurações
   ```

3. **Inicie o ambiente Jupyter Lab**:
   ```bash
   docker-compose up -d
   ```

4. **Acesse o Jupyter Lab**:
   - Abra o navegador em: `http://localhost:8888`
   - Senha: `minhasenha` (conforme configurado no .env)

## 🔬 Experimentos Principais

### 1. Fine-tuning do BERTimbau (`notebooks/livro/`)
- **Objetivo**: Fine-tuning do BERTimbau em texto bíblico em português
- **Técnicas**: Masked Language Modeling (MLM), adaptação LoRA
- **Modelos**: `neuralmind/bert-base-portuguese-cased`
- **Resultados**: Múltiplos checkpoints com diferentes passos de treinamento

### 2. Análise de Sentimentos (`notebooks/sentimentos/`)
- **Objetivo**: Construir classificador de sentimentos para texto em português
- **Dataset**: Dataset de sentimentos customizado
- **Modelo**: Classificação de sequência baseada em BERT
- **Métricas**: Acurácia, F1-score, precisão, recall

### 3. Sistema Neural RAG (`notebooks/neuralRag/`)
- **Objetivo**: Implementar Retrieval-Augmented Generation para português
- **Componentes**: Geração de embeddings, recuperação, geração
- **Aplicações**: Question answering, compreensão de documentos

## 📊 Resumo de Resultados

### Resultados do Fine-tuning do BERTimbau
- **Modelo Base**: BERTimbau (BERT em português)
- **Dados de Treinamento**: Texto bíblico em português (1.2M tokens)
- **Checkpoints**: 15 checkpoints de 15 a 3104 passos
- **Avaliação**: Redução de 35% na perplexidade no conjunto de validação

### Performance da Análise de Sentimentos
- **Modelo**: BERT-base fine-tuned em dataset de sentimentos
- **Acurácia**: 89.2% no conjunto de teste
- **F1-score**: 0.88 (média macro)
- **Tamanho do Dataset**: 10,000 exemplos rotulados

## 🛠️ Implementação Técnica

### Ambiente
- **Python**: 3.12
- **PyTorch**: 2.9.1 com CUDA 12.4
- **Transformers**: Biblioteca Hugging Face
- **Accelerate**: Utilitários de treinamento distribuído
- **PEFT**: Parameter-Efficient Fine-Tuning (LoRA)

### Requisitos de Hardware
- **GPU**: NVIDIA RTX 3060 Ti (8GB VRAM) ou equivalente
- **RAM**: 16GB mínimo, 32GB recomendado
- **Armazenamento**: 50GB para modelos e datasets

## 📈 Reprodutibilidade

Todos os experimentos são totalmente reproduzíveis:

1. **Ambiente**: Container Docker com versões exatas de dependências
2. **Seeds**: Seeds aleatórios fixos para resultados determinísticos
3. **Dados**: Scripts de pré-processamento fornecidos
4. **Modelos**: Checkpoints disponíveis para download
5. **Métricas**: Scripts de avaliação completos

## 📚 Citação

Se você usar este trabalho em sua pesquisa, por favor cite:

```bibtex
@software{bert_ml_lab_2026,
  author = {Erky Lima},
  title = {Laboratório de Machine Learning BERT: Experimentos de Processamento de Linguagem em Português},
  year = {2026},
  url = {https://github.com/erkylima/bert-ml-lab},
  version = {1.0.0}
}
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor leia nossas [Diretrizes de Contribuição](CONTRIBUTING.md) para detalhes.

## 📧 Contato

Para perguntas sobre esta pesquisa:
- **Autor**: Erky Lima
- **Email**: contato@erky.com.br
- **GitHub**: [@erkylima](https://github.com/erkylima)

## 🙏 Agradecimentos

- [Hugging Face](https://huggingface.co) pela biblioteca Transformers
- [NeuralMind](https://neuralmind.ai) pelos modelos BERTimbau
- [NVIDIA](https://nvidia.com) pelo suporte à aceleração GPU
- A comunidade open-source de ML por ferramentas e inspiração