#!/bin/bash

# BERT ML Laboratory - Project Setup Script
# This script sets up the project environment for scientific experiments

set -e

echo "========================================="
echo "BERT ML Laboratory - Setup Script"
echo "========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    print_info "Checking prerequisites..."
    
    # Check Docker
    if command -v docker &> /dev/null; then
        print_info "Docker is installed"
    else
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    # Check Docker Compose
    if command -v docker-compose &> /dev/null || docker compose version &> /dev/null; then
        print_info "Docker Compose is available"
    else
        print_error "Docker Compose is not available. Please install it."
        exit 1
    fi
    
    # Check NVIDIA Docker if GPU is available
    if command -v nvidia-smi &> /dev/null; then
        print_info "NVIDIA GPU detected"
        if docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi &> /dev/null; then
            print_info "NVIDIA Docker runtime is working"
        else
            print_warning "NVIDIA Docker runtime may not be properly configured"
        fi
    else
        print_warning "No NVIDIA GPU detected. Running in CPU mode."
    fi
}

# Setup environment files
setup_environment() {
    print_info "Setting up environment files..."
    
    if [ ! -f .env ]; then
        print_info "Creating .env file from template..."
        cp .env.example .env
        print_info "Please edit .env file with your configuration"
    else
        print_info ".env file already exists"
    fi
    
    # Create necessary directories
    print_info "Creating project directories..."
    mkdir -p data/{raw,processed,external}
    mkdir -p models/{checkpoints,published}
    mkdir -p results/{metrics,visualizations,logs}
    mkdir -p docs/{methodology,results,references}
    
    print_info "Project structure created successfully"
}

# Build Docker image
build_docker() {
    print_info "Building Docker image..."
    
    if docker-compose build; then
        print_info "Docker image built successfully"
    else
        print_error "Failed to build Docker image"
        exit 1
    fi
}

# Start the laboratory
start_laboratory() {
    print_info "Starting BERT ML Laboratory..."
    
    if docker-compose up -d; then
        print_info "Laboratory started successfully"
        
        # Get container status
        sleep 2
        print_info "Container status:"
        docker-compose ps
        
        # Show access information
        JUPYTER_PORT=$(grep JUPYTER_PORT .env 2>/dev/null | cut -d '=' -f2 || echo "8888")
        print_info "========================================="
        print_info "Access Jupyter Lab at: http://localhost:${JUPYTER_PORT}"
        print_info "Default password: 'minha senha'"
        print_info "========================================="
        print_info "To view logs: docker-compose logs -f"
        print_info "To stop: docker-compose down"
        print_info "========================================="
    else
        print_error "Failed to start laboratory"
        exit 1
    fi
}

# Generate documentation
generate_documentation() {
    print_info "Generating project documentation..."
    
    # Create experiment documentation
    cat > docs/methodology/experiment_overview.md << 'EOF'
# Experiment Methodology Overview

## 1. BERTimbau Fine-tuning Experiment

### 1.1 Objective
Fine-tune the BERTimbau model (Portuguese BERT) on domain-specific Portuguese text to improve language understanding capabilities.

### 1.2 Methodology
- **Model**: neuralmind/bert-base-portuguese-cased
- **Dataset**: Portuguese biblical text (1.2M tokens)
- **Technique**: Masked Language Modeling (MLM)
- **Fine-tuning**: LoRA (Low-Rank Adaptation) for parameter efficiency
- **Training**: 3 epochs, batch size 8, learning rate 2e-5

### 1.3 Evaluation Metrics
- Perplexity on validation set
- Masked token prediction accuracy
- Semantic similarity scores

## 2. Sentiment Analysis Experiment

### 2.1 Objective
Build a sentiment classification system for Portuguese text using transfer learning.

### 2.2 Methodology
- **Base Model**: BERT-base-uncased
- **Dataset**: 10,000 labeled Portuguese sentences
- **Task**: Binary sentiment classification (positive/negative)
- **Training**: 3 epochs with class weighting

### 2.3 Evaluation Metrics
- Accuracy, Precision, Recall, F1-score
- Confusion matrix analysis
- ROC-AUC curve

## 3. Neural RAG Experiment

### 3.1 Objective
Implement a Retrieval-Augmented Generation system for Portuguese question answering.

### 3.2 Methodology
- **Retriever**: Sentence-BERT embeddings
- **Generator**: Mistral-7B fine-tuned on Portuguese
- **Dataset**: Portuguese Wikipedia + custom Q&A pairs
- **Evaluation**: ROUGE, BLEU, human evaluation

## 4. Reproducibility Measures

### 4.1 Environment
- Docker container with exact dependency versions
- Fixed random seeds (SEED=42)
- Version-controlled data preprocessing

### 4.2 Data Management
- Raw data preserved in data/raw/
- Processed data in data/processed/ with versioning
- External datasets documented in data/external/

### 4.3 Model Management
- Checkpoints saved at regular intervals
- Model cards with training details
- Performance metrics logged
EOF

    print_info "Documentation generated in docs/methodology/"
}

# Main execution
main() {
    echo "========================================="
    echo "BERT ML Laboratory Setup"
    echo "========================================="
    
    check_prerequisites
    setup_environment
    build_docker
    generate_documentation
    start_laboratory
    
    print_info "Setup completed successfully!"
    print_info "Your scientific ML laboratory is ready for experiments."
}

# Run main function
main "$@"