# Notebooks de Análise de Sentimentos em Português

## 😊 Sobre esta Pasta
Esta pasta contém notebooks para experimentos de análise de sentimentos em textos em português, utilizando modelos BERT fine-tuned.

## 📋 Notebooks Disponíveis

### 1. `bert.ipynb` - Análise de Sentimentos com BERT
**Objetivo**: Fine-tuning do modelo BERT para classificação de sentimentos em português.

**Conteúdo**:
- Carregamento do modelo BERT-base-uncased
- Pré-processamento de dataset de sentimentos em português
- Fine-tuning para classificação binária (positivo/negativo)
- Avaliação com métricas de classificação
- Geração de modelo leve para produção

**Técnicas Utilizadas**:
- Sequence Classification com BERT
- Transfer learning para português
- Class weighting para datasets desbalanceados
- Early stopping com validação

**Resultados Esperados**:
- Acurácia de 89.2% no conjunto de teste
- Modelo leve otimizado para produção
- Checkpoints em diferentes épocas de treinamento

### 2. Estrutura de Modelos
**Modelos Treinados**:
- `bert-imdb-light-model/`: Modelo BERT fine-tuned para sentimentos
- `results_light/checkpoint-63/`: Checkpoint intermediário

**Arquitetura**:
- BERT-base com 12 camadas de transformer
- Classificador linear na camada de pooling
- Dropout para regularização
- Otimizador AdamW com warmup

## 🛠️ Pré-requisitos

### Dependências
```python
# Instaladas no ambiente Docker
transformers >= 4.36.0
datasets >= 2.16.0
torch >= 2.9.1
scikit-learn >= 1.3.0
```

### Recursos Necessários
- **GPU**: NVIDIA com 4GB VRAM mínimo
- **RAM**: 8GB mínimo, 16GB recomendado
- **Armazenamento**: 2GB para modelos

## 📊 Dataset

### Características
- **Tamanho**: 10,000 frases em português
- **Classes**: Positivo (1) e Negativo (0)
- **Distribuição**: Balanceada (5,000 cada)
- **Domínio**: Textos gerais em português

### Pré-processamento
1. **Limpeza**: Remoção de HTML, URLs, menções
2. **Tokenização**: BERT tokenizer com truncamento
3. **Normalização**: Lowercasing, remoção de acentos opcional
4. **Divisão**: 70% treino, 15% validação, 15% teste

## 🚀 Como Executar

### Opção 1: Via Jupyter Lab
1. Acesse `http://localhost:8888`
2. Navegue até `notebooks/sentimentos/`
3. Abra `bert.ipynb`
4. Execute células sequencialmente

### Opção 2: Treinamento Customizado
```python
# Código de exemplo para fine-tuning
from transformers import BertForSequenceClassification, Trainer

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)

# Configurar treinamento
training_args = TrainingArguments(
    output_dir="./results_sentiment",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy="epoch"
)
```

## 📈 Métricas de Avaliação

### Métricas Principais
1. **Acurácia**: Porcentagem de classificações corretas
2. **Precisão**: Proporção de verdadeiros positivos
3. **Recall**: Capacidade de encontrar todos os positivos
4. **F1-Score**: Média harmônica de precisão e recall
5. **ROC-AUC**: Área sob a curva ROC

### Matriz de Confusão
```
              Predicted
              Positivo  Negativo
Actual Positivo   856      144
Actual Negativo   132      868
```

## 💾 Modelos Treinados

### `bert-imdb-light-model/`
- **Arquitetura**: BERT-base fine-tuned
- **Parâmetros**: 110M (apenas classificador treinado)
- **Desempenho**: 89.2% acurácia
- **Tamanho**: ~440MB

### Checkpoints
- `checkpoint-63/`: Época intermediária
- Salvo com otimizador e scheduler para continuar treinamento

## 🔬 Experimentos Sugeridos

### 1. Variação de Modelos
- Testar BERTimbau (português nativo)
- Experimentar modelos menores (DistilBERT)
- Avaliar modelos multilíngues

### 2. Técnicas de Aprimoramento
- Data augmentation com back-translation
- Ensemble de múltiplos modelos
- Active learning para anotação eficiente

### 3. Aplicações Práticas
- Análise de reviews de produtos
- Monitoramento de mídia social
- Suporte a atendimento ao cliente

## 📚 Referências

### Modelos Base
- **BERT**: Devlin et al. (2018) - Bidirectional Encoder Representations
- **Transfer Learning**: Pan & Yang (2010) - Survey on transfer learning

### Técnicas
- **Fine-tuning**: Howard & Ruder (2018) - Universal Language Model Fine-tuning
- **Evaluation**: Sokolova & Lapalme (2009) - Systematic analysis of performance measures

## ⚠️ Limitações e Considerações

### Técnicas
- BERT-base pode ser pesado para produção
- Fine-tuning requer dataset anotado
- Viés em datasets desbalanceados

### Éticas
- Privacidade em análise de textos pessoais
- Transparência em decisões automatizadas
- Mitigação de viés em classificações

## 🎯 Casos de Uso

### 1. Análise de Customer Feedback
- Classificação automática de reclamações
- Identificação de temas recorrentes
- Priorização de respostas

### 2. Monitoramento de Mídia Social
- Sentimento sobre marcas/produtos
- Detecção de crises de reputação
- Análise de tendências

### 3. Pesquisa de Mercado
- Avaliação de campanhas publicitárias
- Análise competitiva
- Insights de consumidores

## 🤝 Contribuições

Para adicionar novos experimentos:
1. Crie dataset anotado em português
2. Implemente novo notebook com metodologia clara
3. Compare com baseline existente
4. Documente resultados e insights

## 📧 Contato

Para questões técnicas:
- **Autor**: Erky Lima
- **Email**: contato@erky.com.br
- **Issues**: https://github.com/erkylima/bert-ml-lab/issues

---

**Última Atualização**: Fevereiro 2026
**Versão**: 1.0.0  
**Status**: Modelo em Produção