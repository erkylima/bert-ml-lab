# Notebooks de Neural RAG (Retrieval-Augmented Generation)

## 🔍 Sobre esta Pasta
Esta pasta contém notebooks para implementação de sistemas Neural RAG (Retrieval-Augmented Generation) em português, combinando recuperação de informações com geração de texto.

## 📋 Notebooks Disponíveis

### 1. `embedding.ipynb` - Sistema de Embeddings e Recuperação
**Objetivo**: Implementar sistema completo de RAG para português com embeddings, recuperação e geração.

**Conteúdo**:
- Geração de embeddings com Sentence-BERT
- Indexação de documentos com FAISS
- Sistema de recuperação semântica
- Integração com modelo de geração (Mistral)
- Avaliação de qualidade de recuperação

**Técnicas Utilizadas**:
- Embeddings multilingues (paraphrase-multilingual-MiniLM)
- Similaridade de cosseno para recuperação
- FAISS para busca eficiente em grandes volumes
- Reranking com modelos cross-encoder
- Geração condicionada ao contexto recuperado

**Componentes do Sistema**:
1. **Indexador**: Cria embeddings e índice FAISS
2. **Retriever**: Recupera documentos relevantes
3. **Reranker**: Reordena resultados por relevância
4. **Generator**: Gera resposta baseada no contexto

## 🛠️ Pré-requisitos

### Dependências
```python
# Instaladas no ambiente Docker
sentence-transformers >= 2.2.0
faiss-cpu >= 1.7.0  # ou faiss-gpu para GPU
transformers >= 4.36.0
datasets >= 2.16.0
```

### Recursos Necessários
- **GPU**: Recomendado para embeddings e geração
- **RAM**: 16GB mínimo para índices grandes
- **Armazenamento**: Variável conforme tamanho do corpus

## 📊 Arquitetura do Sistema

### Pipeline Completo
```
1. Documentos → 2. Embeddings → 3. Índice FAISS
       ↓
4. Consulta → 5. Recuperação → 6. Reranking
       ↓
7. Contexto + Consulta → 8. Geração → 9. Resposta
```

### Modelos Utilizados
- **Embeddings**: `paraphrase-multilingual-MiniLM-L12-v2`
- **Recuperação**: FAISS com índice IVF
- **Geração**: `mistralai/Mistral-7B-v0.1` (ou similar)
- **Reranking**: Cross-encoder multilingue

## 🚀 Como Executar

### Opção 1: Pipeline Completo
1. Acesse `http://localhost:8888`
2. Navegue até `notebooks/neuralRag/`
3. Abra `embedding.ipynb`
4. Execute seções na ordem:
   - Configuração do ambiente
   - Criação de embeddings
   - Construção do índice
   - Teste de recuperação
   - Integração com gerador

### Opção 2: Componentes Individuais
```python
# Exemplo: Criação de embeddings
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(documents)

# Exemplo: Recuperação com FAISS
import faiss
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
```

## 📈 Métricas de Avaliação

### Recuperação (Retrieval)
1. **Recall@K**: Proporção de relevantes nos K primeiros
2. **Precision@K**: Precisão nos K primeiros resultados
3. **MRR (Mean Reciprocal Rank)**: Média do inverso do rank
4. **NDCG@K**: Discounted cumulative gain normalizado

### Geração (Generation)
1. **ROUGE**: Overlap de n-grams com referência
2. **BLEU**: Precisão de n-grams ponderada
3. **BERTScore**: Similaridade semântica com BERT
4. **Human Evaluation**: Julgamento humano de qualidade

### Sistema Completo
1. **End-to-End Accuracy**: Resposta correta final
2. **Latência**: Tempo total de consulta a resposta
3. **Relevância Contextual**: Uso adequado do contexto

## 💾 Estrutura de Dados

### Documentos de Exemplo
- `meu_projeto_falso/`: Projeto exemplo com documentação
- Arquivos `.py` com código comentado
- Documentação em português para indexação

### Índices Gerados
- `faiss_index.bin`: Índice FAISS com embeddings
- `document_store.json`: Metadados dos documentos
- `embeddings.npy`: Embeddings em formato NumPy

## 🔬 Experimentos Sugeridos

### 1. Otimização de Embeddings
- Testar diferentes modelos de embeddings
- Fine-tuning de embeddings para domínio específico
- Dimensionality reduction (PCA, UMAP)

### 2. Melhoria de Recuperação
- Hybrid search (BM25 + embeddings)
- Query expansion com LLMs
- Learning to rank com dados anotados

### 3. Aprimoramento de Geração
- Prompt engineering para português
- Fine-tuning do gerador para domínio
- Controle de atributos (tom, estilo, comprimento)

## 📚 Referências

### RAG
- **RAG Original**: Lewis et al. (2020) - Retrieval-Augmented Generation
- **DPR**: Karpukhin et al. (2020) - Dense Passage Retrieval
- **REALM**: Guu et al. (2020) - Retrieval-Augmented Language Models

### Embeddings
- **Sentence-BERT**: Reimers & Gurevych (2019)
- **Multilingual Embeddings**: Feng et al. (2020)

### FAISS
- **FAISS**: Johnson et al. (2019) - Billion-scale similarity search

## ⚠️ Limitações e Considerações

### Técnicas
- Latência em sistemas de recuperação densa
- Qualidade de embeddings para português
- Custo computacional de modelos grandes

### Éticas
- Verificação de fatos em respostas geradas
- Transparência sobre fontes utilizadas
- Mitigação de alucinações em LLMs

## 🎯 Casos de Uso

### 1. Sistemas de Q&A
- Base de conhecimento corporativa
- Suporte técnico automatizado
- Tutoriais interativos

### 2. Assistência à Pesquisa
- Recuperação de artigos acadêmicos
- Síntese de literatura
- Descoberta de conexões

### 3. Análise Documental
- Due diligence em grandes volumes
- Monitoramento regulatório
- Análise de contratos

## 🤝 Contribuições

Para expandir o sistema RAG:
1. Adicione novos conjuntos de documentos
2. Implemente técnicas avançadas de recuperação
3. Desenvolva interfaces de usuário
4. Crie datasets de avaliação

## 📧 Contato

Para desenvolvimento de sistemas RAG:
- **Autor**: Erky Lima
- **Email**: contato@erky.com.br
- **Repositório**: https://github.com/erkylima/bert-ml-lab

---

**Última Atualização**: Fevereiro 2026  
**Versão**: 1.0.0  
**Status**: Sistema em Desenvolvimento