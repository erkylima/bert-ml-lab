# Notebooks do Laboratório BERT ML

## 🧪 Visão Geral
Esta pasta contém todos os notebooks Jupyter do Laboratório BERT ML, organizados por área de pesquisa. Cada notebook representa um experimento científico completo e reproduzível em processamento de linguagem natural, visão computacional e aprendizado multimodal em português.

## 📁 Estrutura de Pastas

### 1. `livro/` - Processamento de Linguagem Natural
- **Foco**: Fine-tuning de modelos BERT em português
- **Aplicações**: Análise de textos bíblicos, adaptação de domínio
- **Técnicas**: LoRA, MLM, transfer learning
- **Notebooks**: `bertimbau.ipynb`, `treino_atos.ipynb`

### 2. `sentimentos/` - Análise de Sentimentos
- **Foco**: Classificação de sentimentos em português
- **Aplicações**: Análise de reviews, monitoramento de mídia social
- **Técnicas**: Sequence classification, fine-tuning
- **Notebooks**: `bert.ipynb`

### 3. `neuralRag/` - Sistemas RAG
- **Foco**: Retrieval-Augmented Generation em português
- **Aplicações**: Q&A, assistentes de conhecimento
- **Técnicas**: Embeddings, FAISS, geração condicionada
- **Notebooks**: `embedding.ipynb`

### 4. `imagens/` - Visão Computacional
- **Foco**: CNNs e aprendizado multimodal
- **Aplicações**: Classificação de imagens, descrição automática
- **Técnicas**: Transfer learning, fusão imagem-texto
- **Notebooks**: `Convolutional Neural Network.ipynb`

## 🚀 Como Usar os Notebooks

### Ambiente Recomendado
```bash
# Usar o ambiente Docker configurado
docker compose up -d
# Acessar: http://localhost:8888
# Senha: minhasenha
```

### Execução Básica
1. **Abrir Jupyter Lab** no navegador
2. **Navegar** até a pasta do experimento desejado
3. **Abrir o notebook** (.ipynb)
4. **Executar células** em ordem (Kernel → Restart & Run All)
5. **Analisar resultados** e visualizações

### Execução Programática
```bash
# Converter notebook para script
jupyter nbconvert --to script notebooks/livro/bertimbau.ipynb

# Executar como script Python
python notebooks/livro/bertimbau.py
```

## 🔧 Configuração Comum

### Variáveis de Ambiente
```python
# Configurações compartilhadas
import os

# Modelos
BERTIMBAU_MODEL = "neuralmind/bert-base-portuguese-cased"
SENTIMENT_MODEL = "bert-base-uncased"

# Paths
DATA_DIR = "/workspace/data"
MODELS_DIR = "/workspace/models"
RESULTS_DIR = "/workspace/results"

# Hiperparâmetros
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
SEED = 42
```

### Boas Práticas
1. **Versionamento**: Salvar checkpoints regularmente
2. **Logging**: Registrar métricas e hiperparâmetros
3. **Visualização**: Incluir gráficos e análises
4. **Documentação**: Comentar código e explicar decisões

## 📊 Metodologia Científica

### Reprodutibilidade
- **Ambiente**: Docker com dependências fixas
- **Seeds**: Random seeds fixos (SEED=42)
- **Dados**: Versionamento de datasets
- **Modelos**: Checkpoints com metadados

### Validação
- **Split**: 70/15/15 (treino/validação/teste)
- **Métricas**: Apropriadas para cada tarefa
- **Baselines**: Comparação com métodos estabelecidos
- **Ablation**: Análise de componentes individuais

### Documentação
- **Objetivo**: Declaração clara do experimento
- **Metodologia**: Descrição detalhada dos métodos
- **Resultados**: Análise quantitativa e qualitativa
- **Conclusões**: Insights e direções futuras

## 🎯 Fluxo de Trabalho Típico

### 1. Preparação
```python
# Carregar dados
from datasets import load_dataset
dataset = load_dataset(...)

# Pré-processar
def preprocess_function(examples):
    # Tokenização, limpeza, etc.
    return processed_examples
```

### 2. Modelagem
```python
# Definir modelo
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained(...)

# Configurar treinamento
from transformers import TrainingArguments
training_args = TrainingArguments(...)
```

### 3. Treinamento
```python
# Treinar
from transformers import Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset
)
trainer.train()
```

### 4. Avaliação
```python
# Avaliar
results = trainer.evaluate()
print(f"Acurácia: {results['eval_accuracy']:.2%}")

# Visualizar
import matplotlib.pyplot as plt
plt.plot(history['loss'])
plt.savefig('loss_curve.png')
```

### 5. Documentação
```markdown
# Resultados do Experimento

## Métricas
- Acurácia: 89.2%
- F1-Score: 0.88

## Insights
- O modelo performa melhor em textos curtos
- Há overfitting após 3 épocas
```

## 🔬 Experimentos Sugeridos

### Novas Arquiteturas
1. Testar modelos Transformer mais recentes
2. Implementar técnicas de eficiência (quantização, pruning)
3. Explorar arquiteturas multimodais

### Aplicações em Português
1. Fine-tuning para domínios específicos (jurídico, médico)
2. Desenvolvimento de datasets anotados
3. Avaliação comparativa com outros idiomas

### Integração com Produção
1. Desenvolvimento de APIs para modelos
2. Monitoramento de desempenho em produção
3. Sistemas de feedback e retreinamento

## 📚 Recursos Adicionais

### Documentação
- **READMEs específicos**: Cada pasta tem documentação detalhada
- **Comentários no código**: Explicações inline
- **Exemplos de uso**: Células demonstrativas

### Ferramentas
- **TensorBoard**: Visualização de treinamento
- **MLflow**: Tracking de experimentos
- **Weights & Biases**: Logging avançado (opcional)

### Comunidade
- **Issues GitHub**: Reportar problemas e sugerir melhorias
- **Discussions**: Discussões técnicas e colaboração
- **Pull Requests**: Contribuições de código

## ⚠️ Considerações Importantes

### Recursos Computacionais
- **GPU**: Necessária para treinamento eficiente
- **Memória**: Monitorar uso durante execução
- **Armazenamento**: Gerenciar checkpoints e logs

### Ética em IA
- **Bias**: Avaliar viés em datasets e modelos
- **Transparência**: Documentar limitações
- **Privacidade**: Proteger dados sensíveis

### Manutenção
- **Atualizações**: Manter dependências atualizadas
- **Backup**: Versionar resultados importantes
- **Depreciação**: Marcar experimentos obsoletos

## 🤝 Como Contribuir

### Adicionar Novo Experimento
1. Criar pasta com nome descritivo
2. Desenvolver notebook completo
3. Adicionar README em português
4. Incluir dataset de exemplo (se aplicável)
5. Submeter pull request

### Melhorar Experimentos Existentes
1. Identificar área de melhoria
2. Implementar mudança incremental
3. Validar com métricas apropriadas
4. Atualizar documentação
5. Compartilhar resultados

### Reportar Problemas
1. Verificar se é problema conhecido
2. Coletar informações relevantes
3. Criar issue no GitHub
4. Incluir steps para reproduzir
5. Propor solução (se possível)

## 📧 Suporte e Contato

### Para Dúvidas Técnicas
- **Documentação**: Ler READMEs específicos
- **Issues GitHub**: https://github.com/erkylima/bert-ml-lab/issues
- **Email**: contato@erky.com.br

### Para Colaboração
- **Fork do repositório**: Desenvolver features
- **Discussions**: Planejar colaborações
- **Pull Requests**: Contribuir código

### Para Uso em Pesquisa
- **Citação**: Usar formato CITATION.cff
- **Atribuição**: Reconhecer contribuições
- **Compartilhamento**: Divulgar resultados

---

**Laboratório BERT ML** - Experimentos Científicos em Português  
**Última Atualização**: Fevereiro 2025  
**Versão**: 1.0.0  
**Status**: Ativo e em Desenvolvimento