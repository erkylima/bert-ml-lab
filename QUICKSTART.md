# BERT ML Laboratory - Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/erkylima/bert-ml-lab.git
cd bert-ml-lab

# Run the setup script
./scripts/setup_project.sh
```

### 2. Access the Laboratory
- **URL**: http://localhost:8888
- **Password**: `minhasenha`
- **Username**: No username required

### 3. Run Your First Experiment
1. Open Jupyter Lab in your browser
2. Navigate to `notebooks/livro/bertimbau.ipynb`
3. Run all cells (Kernel → Restart & Run All)

## 📋 What's Included

### Pre-configured Environment
- ✅ Python 3.12 with scientific packages
- ✅ PyTorch 2.9.1 with CUDA 12.4 support
- ✅ Hugging Face Transformers library
- ✅ Jupyter Lab with dark theme
- ✅ GPU acceleration ready

### Ready-to-Run Experiments
1. **BERTimbau Fine-tuning** (`notebooks/livro/`)
   - Portuguese BERT model
   - Biblical text dataset
   - LoRA fine-tuning

2. **Sentiment Analysis** (`notebooks/sentimentos/`)
   - Portuguese sentiment classification
   - Pre-trained model checkpoints
   - Evaluation metrics

3. **Neural RAG System** (`notebooks/neuralRag/`)
   - Retrieval-Augmented Generation
   - Portuguese question answering
   - Embedding and retrieval

## 🎯 For Researchers

### Reproduce Published Results
```bash
# Run reproduction script
python scripts/reproduce_experiments.py --experiment all

# Generate publication-ready figures
python scripts/generate_figures.py
```

### Start New Experiment
1. Copy template notebook: `templates/experiment_template.ipynb`
2. Update configuration in `config/experiment_config.yaml`
3. Run with: `python scripts/run_experiment.py --config your_config.yaml`

## 🛠️ Common Tasks

### Check System Status
```bash
# Check Docker containers
docker-compose ps

# View logs
docker-compose logs -f

# Check GPU availability
docker-compose exec bert-ml-lab nvidia-smi
```

### Manage Data
```bash
# Add new dataset
cp your_data.csv data/raw/
python scripts/preprocess_data.py --input data/raw/your_data.csv

# Download external dataset
python scripts/download_dataset.py --name portuguese_wikipedia
```

### Export Results
```bash
# Export experiment results
python scripts/export_results.py --format latex

# Generate model cards
python scripts/generate_model_card.py --model models/checkpoints/bertimbau_ft
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Docker Build Fails
```bash
# Clean build
docker-compose down
docker-compose build --no-cache
```

#### 2. GPU Not Detected
```bash
# Check NVIDIA Docker
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi

# Update Docker Compose
docker-compose down
export NVIDIA_VISIBLE_DEVICES=all
docker-compose up -d
```

#### 3. Memory Issues
```bash
# Increase shared memory
export DOCKER_SHARED_MEMORY=32gb
docker-compose down && docker-compose up -d

# Reduce batch size
export TRAIN_BATCH_SIZE=4
```

## 📊 Monitoring

### Resource Usage
```bash
# Monitor GPU usage
watch -n 1 nvidia-smi

# Monitor memory
docker stats bert-ml-lab

# Check disk space
df -h /workspace
```

### Experiment Tracking
- **TensorBoard**: http://localhost:6006 (if enabled)
- **MLflow**: http://localhost:5000 (if enabled)
- **Logs**: `results/logs/`

## 🎓 Learning Resources

### Tutorial Notebooks
1. `tutorials/01_bert_basics.ipynb` - BERT fundamentals
2. `tutorials/02_fine_tuning.ipynb` - Transfer learning
3. `tutorials/03_evaluation.ipynb` - Model evaluation
4. `tutorials/04_publication.ipynb` - Scientific writing

### Documentation
- Full documentation: `docs/`
- API reference: `docs/api/`
- Experiment catalog: `docs/experiment_catalog.md`
- Publication guide: `docs/publication_guide.md`

## 🤝 Getting Help

### Community Support
- **GitHub Issues**: Bug reports and feature requests
- **Discussions**: Questions and community help
- **Wiki**: Detailed documentation and tutorials

### Contact Maintainer
- **Email**: contato@erky.com.br
- **GitHub**: @erkylima

## 📈 Next Steps

### For Beginners
1. Complete tutorial notebooks
2. Run example experiments
3. Modify hyperparameters
4. Add your own dataset

### For Advanced Users
1. Implement new model architectures
2. Add custom evaluation metrics
3. Create publication-ready visualizations
4. Contribute to the codebase

### For Publication
1. Document your methodology
2. Generate reproducible results
3. Prepare supplementary materials
4. Follow publication guide

---

**Happy Experimenting!** 🧪🔬

Remember to cite this work if you use it in your research:
```bibtex
@software{bert_ml_lab_2026,
  author = {Erky Lima},
  title = {BERT Machine Learning Laboratory},
  year = {2026},
  url = {https://github.com/erkylima/bert-ml-lab}
}
```