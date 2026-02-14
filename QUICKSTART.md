# Laboratório BERT ML - Guia de Início Rápido

## 🚀 Comece em 5 Minutos

### 1. Clone e Configuração
```bash
# Clone o repositório
git clone https://github.com/erkylima/bert-ml-lab.git
cd bert-ml-lab

# Execute o script de setup
./scripts/setup_project.sh
```

### 2. Acesse o Laboratório
- **URL**: http://localhost:8888
- **Senha**: `minhasenha`
- **Usuário**: Não requer nome de usuário

### 3. Execute Seu Primeiro Experimento
1. Abra o Jupyter Lab no seu navegador
2. Navegue até `notebooks/livro/bertimbau.ipynb`
3. Execute todas as células (Kernel → Restart & Run All)

## 📋 O Que Está Incluído

### Ambiente Pré-configurado
- ✅ Python 3.12 com pacotes científicos
- ✅ PyTorch 2.9.1 com suporte a CUDA 12.4
- ✅ Biblioteca Hugging Face Transformers
- ✅ Jupyter Lab com tema escuro
- ✅ Aceleração GPU pronta

### Experimentos Prontos para Executar
1. **Fine-tuning do BERTimbau** (`notebooks/livro/`)
   - Modelo BERT em português
   - Dataset de texto bíblico
   - Fine-tuning LoRA

2. **Análise de Sentimentos** (`notebooks/sentimentos/`)
   - Classificação de sentimentos em português
   - Checkpoints de modelo pré-treinado
   - Métricas de avaliação

3. **Sistema Neural RAG** (`notebooks/neuralRag/`)
   - Retrieval-Augmented Generation
   - Question answering em português
   - Embeddings e recuperação

## 🎯 Para Pesquisadores

### Reproduza Resultados Publicados
```bash
# Execute o script de reprodução
python scripts/reproduce_experiments.py --experiment all

# Gere figuras prontas para publicação
python scripts/generate_figures.py
```

### Inicie Novo Experimento
1. Copie o template de notebook: `templates/experiment_template.ipynb`
2. Atualize a configuração em `config/experiment_config.yaml`
3. Execute com: `python scripts/run_experiment.py --config your_config.yaml`

## 🛠️ Tarefas Comuns

### Verifique o Status do Sistema
```bash
# Verifique containers Docker
docker-compose ps

# Visualize logs
docker-compose logs -f

# Verifique disponibilidade GPU
docker-compose exec bert-ml-lab nvidia-smi
```

### Gerencie Dados
```bash
# Adicione novo dataset
cp your_data.csv data/raw/
python scripts/preprocess_data.py --input data/raw/your_data.csv

# Baixe dataset externo
python scripts/download_dataset.py --name portuguese_wikipedia
```

### Exporte Resultados
```bash
# Exporte resultados de experimentos
python scripts/export_results.py --format latex

# Gere model cards
python scripts/generate_model_card.py --model models/checkpoints/bertimbau_ft
```

## 🔧 Solução de Problemas

### Problemas Comuns

#### 1. Build do Docker Falha
```bash
# Build limpo
docker-compose down
docker-compose build --no-cache
```

#### 2. GPU Não Detectada
```bash
# Verifique NVIDIA Docker
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi

# Atualize Docker Compose
docker-compose down
export NVIDIA_VISIBLE_DEVICES=all
docker-compose up -d
```

#### 3. Problemas de Memória
```bash
# Aumente memória compartilhada
export DOCKER_SHARED_MEMORY=32gb
docker-compose down && docker-compose up -d

# Reduza batch size
export TRAIN_BATCH_SIZE=4
```

## 📊 Monitoramento

### Uso de Recursos
```bash
# Monitore uso de GPU
watch -n 1 nvidia-smi

# Monitore memória
docker stats bert-ml-lab

# Verifique espaço em disco
df -h /workspace
```

### Tracking de Experimentos
- **TensorBoard**: http://localhost:6006 (se habilitado)
- **MLflow**: http://localhost:5000 (se habilitado)
- **Logs**: `results/logs/`

## 🎓 Recursos de Aprendizado

### Notebooks Tutoriais
1. `tutorials/01_bert_basics.ipynb` - Fundamentos do BERT
2. `tutorials/02_fine_tuning.ipynb` - Transfer learning
3. `tutorials/03_evaluation.ipynb` - Avaliação de modelos
4. `tutorials/04_publication.ipynb` - Escrita científica

### Documentação
- Documentação completa: `docs/`
- Referência de API: `docs/api/`
- Catálogo de experimentos: `docs/experiment_catalog.md`
- Guia de publicação: `docs/publication_guide.md`

## 🤝 Obtendo Ajuda

### Suporte da Comunidade
- **GitHub Issues**: Relatórios de bugs e solicitações de features
- **Discussions**: Perguntas e ajuda da comunidade
- **Wiki**: Documentação detalhada e tutoriais

### Contate o Mantenedor
- **Email**: contato@erky.com.br
- **GitHub**: @erkylima

## 📈 Próximos Passos

### Para Iniciantes
1. Complete os notebooks tutoriais
2. Execute experimentos de exemplo
3. Modifique hiperparâmetros
4. Adicione seu próprio dataset

### Para Usuários Avançados
1. Implemente novas arquiteturas de modelo
2. Adicione métricas de avaliação customizadas
3. Crie visualizações prontas para publicação
4. Contribua para a base de código

### Para Publicação
1. Documente sua metodologia
2. Gere resultados reproduzíveis
3. Prepare materiais suplementares
4. Siga o guia de publicação

---

**Bons Experimentos!** 🧪🔬

Lembre-se de citar este trabalho se usá-lo em sua pesquisa:
```bibtex
@software{bert_ml_lab_2026,
  author = {Erky Lima},
  title = {Laboratório de Machine Learning BERT},
  year = {2026},
  url = {https://github.com/erkylima/bert-ml-lab}
}
```