# Notebooks de Visão Computacional e Aprendizado Multimodal

## 🖼️ Sobre esta Pasta
Esta pasta contém notebooks para experimentos com visão computacional e aprendizado multimodal, combinando processamento de imagens com linguagem natural em português.

## 📋 Notebooks Disponíveis

### 1. `Convolutional Neural Network.ipynb` - Redes Neurais Convolucionais
**Objetivo**: Implementação e experimentação com CNNs para classificação de imagens, com integração multimodal para português.

**Conteúdo**:
- Carregamento e pré-processamento do dataset CIFAR-10
- Implementação de arquiteturas CNN (ResNet, VGG, custom)
- Treinamento e avaliação de modelos de visão computacional
- Integração com textos em português para aprendizado multimodal
- Visualização de features e camadas das redes

**Técnicas Utilizadas**:
- Convolutional Neural Networks (CNNs)
- Transfer learning com modelos pré-treinados
- Data augmentation para imagens
- Fine-tuning de modelos de visão
- Fusão multimodal (imagem + texto)

**Aplicações**:
- Classificação de imagens do CIFAR-10
- Extração de features visuais
- Geração de descrições em português
- Análise de similaridade visual-textual

## 🛠️ Pré-requisitos

### Dependências
```python
# Instaladas no ambiente Docker
torch >= 2.9.1
torchvision >= 0.20.0
PIL >= 9.0.0
matplotlib >= 3.7.0
transformers >= 4.36.0  # Para multimodal
```

### Recursos Necessários
- **GPU**: NVIDIA com 4GB VRAM mínimo (recomendado)
- **RAM**: 8GB mínimo para treinamento
- **Armazenamento**: 5GB para datasets de imagens

## 📊 Dataset CIFAR-10

### Características
- **Tamanho**: 60,000 imagens coloridas 32x32
- **Classes**: 10 categorias (avião, carro, pássaro, gato, veado, cachorro, sapo, cavalo, navio, caminhão)
- **Divisão**: 50,000 treino, 10,000 teste
- **Formato**: RGB, 32x32 pixels

### Estrutura no Projeto
```
data/cifar-10-batches-py/
├── data_batch_1  # 10,000 imagens
├── data_batch_2  # 10,000 imagens
├── data_batch_3  # 10,000 imagens
├── data_batch_4  # 10,000 imagens
├── data_batch_5  # 10,000 imagens
└── test_batch    # 10,000 imagens teste
```

## 🚀 Como Executar

### Opção 1: Treinamento Completo
1. Acesse `http://localhost:8888`
2. Navegue até `notebooks/imagens/`
3. Abra `Convolutional Neural Network.ipynb`
4. Execute seções na ordem:
   - Carregamento de dados
   - Definição do modelo
   - Treinamento
   - Avaliação
   - Visualização

### Opção 2: Modelo Customizado
```python
# Exemplo: CNN simples
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 8 * 8, 512)
        self.fc2 = nn.Linear(512, num_classes)
    
    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 8 * 8)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

## 📈 Métricas de Avaliação

### Classificação de Imagens
1. **Acurácia**: Porcentagem de classificações corretas
2. **Precisão por Classe**: Performance individual por categoria
3. **Matriz de Confusão**: Erros entre classes similares
4. **Loss de Treinamento**: Convergência do modelo

### Aprendizado Multimodal
1. **Retrieval Accuracy**: Recuperação de imagem baseada em texto
2. **Captioning Metrics**: ROUGE, BLEU para descrições
3. **Cross-modal Similarity**: Alinhamento imagem-texto
4. **Zero-shot Performance**: Generalização para novas classes

## 💾 Modelos Implementados

### Arquiteturas CNN
1. **SimpleCNN**: Arquitetura customizada simples
2. **ResNet-18/50**: Transfer learning com ResNet
3. **VGG-16**: Arquitetura clássica para visão
4. **EfficientNet**: Modelos eficientes computacionalmente

### Integração Multimodal
- **CLIP-like**: Alinhamento imagem-texto
- **VisualBERT**: BERT com features visuais
- **Custom Fusion**: Fusão personalizada para português

## 🔬 Experimentos Sugeridos

### 1. Otimização de Arquiteturas
- Grid search de hiperparâmetros
- Arquiteturas neural architecture search (NAS)
- Pruning e quantização para eficiência

### 2. Transfer Learning
- Fine-tuning em datasets específicos
- Domain adaptation para novos contextos
- Few-shot learning com poucos exemplos

### 3. Multimodalidade Avançada
- Geração de descrições em português
- Visual question answering (VQA)
- Image captioning com controle de estilo

## 📚 Referências

### Visão Computacional
- **AlexNet**: Krizhevsky et al. (2012) - ImageNet Classification
- **ResNet**: He et al. (2016) - Deep Residual Learning
- **Vision Transformers**: Dosovitskiy et al. (2020) - An Image is Worth 16x16 Words

### Aprendizado Multimodal
- **CLIP**: Radford et al. (2021) - Learning Transferable Visual Models
- **VisualBERT**: Li et al. (2019) - VisualBERT
- **ViLT**: Kim et al. (2021) - Vision-and-Language Transformer

## ⚠️ Limitações e Considerações

### Técnicas
- CNNs requerem grandes datasets para treinamento
- Transfer learning essencial para domínios específicos
- Integração multimodal complexa para português

### Éticas
- Viés em datasets de imagens
- Privacidade em reconhecimento facial
- Uso responsável de tecnologias de visão

## 🎯 Casos de Uso

### 1. Classificação Automática
- Categorização de produtos em e-commerce
- Controle de qualidade visual
- Organização de galerias de fotos

### 2. Análise Multimodal
- Descrição automática de imagens para acessibilidade
- Busca por conteúdo visual com texto em português
- Análise de sentimentos em imagens de mídia social

### 3. Aplicações Industriais
- Inspeção visual automatizada
- Reconhecimento de padrões em imagens médicas
- Monitoramento ambiental com câmeras

## 🤝 Contribuições

Para expandir experimentos de visão:
1. Adicione novos datasets de imagens
2. Implemente arquiteturas state-of-the-art
3. Desenvolva aplicações multimodais em português
4. Crie visualizações e ferramentas de análise

## 📧 Contato

Para desenvolvimento em visão computacional:
- **Autor**: Erky Lima
- **Email**: contato@erky.com.br
- **Repositório**: https://github.com/erkylima/bert-ml-lab

---

**Última Atualização**: Fevereiro 2026  
**Versão**: 1.0.0  
**Status**: Experimentos em Andamento