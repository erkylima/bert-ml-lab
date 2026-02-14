# ====================================================================
# Dockerfile: Ambiente BERT/PyTorch com Conda (Miniforge) e Acesso à GPU
# ATUALIZADO: Python 3.12 e PyTorch 2.9.1 para CUDA 12.4
# ====================================================================

# 🔹 Imagem Base: CUDA 12.4.1 (Base NVIDIA)
FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04

# ---------------------------------------------------------
# 🔹 Configurações Básicas
# ---------------------------------------------------------
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# ---------------------------------------------------------
# 🔹 Instalar Miniforge (Conda)
# ---------------------------------------------------------
ENV MINIFORGE_HOME=/opt/conda
ENV PATH=${MINIFORGE_HOME}/bin:$PATH
SHELL ["/bin/bash", "-c"]

# Instalação em uma única camada
RUN apt-get update && apt-get install -y --no-install-recommends \
        wget git curl bzip2 ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    # Instala Miniforge
    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O /tmp/miniforge.sh && \
    bash /tmp/miniforge.sh -b -p ${MINIFORGE_HOME} && rm /tmp/miniforge.sh && \
    conda clean -afy

# ---------------------------------------------------------
# 🔹 Criar Ambiente Conda 'bert' e Instalar Dependências
# ---------------------------------------------------------
# 🎯 Alterado para Python 3.12
RUN conda create -y -n bert python=3.12 && \
    \
    # Instala Jupyter/Ferramentas base via Conda-Forge
    conda run -n bert conda install -y jupyterlab notebook ipykernel ipywidgets -c conda-forge

    # 🎯 ATUALIZAÇÃO CRÍTICA: Instala PyTorch 2.9.1 (compatível com CUDA 12.4) via Pip.
    # Versão 2.9.1 requer cu124.
RUN conda run -n bert pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 
    
    # Instala bibliotecas de NLP
RUN conda run -n bert pip install --no-cache-dir transformers datasets tqdm scikit-learn matplotlib accelerate evaluate peft && \
    conda clean -afy && \
    \
    # Registra o kernel no ambiente Jupyter
    conda run -n bert python -m ipykernel install --user --name=bert-env --display-name="BERT (Conda)"

# ---------------------------------------------------------
# 🔹 Configurações de Execução
# ---------------------------------------------------------
WORKDIR /workspace
ENV HF_HOME=/workspace/.cache
ENV JUPYTER_CONFIG_DIR=/workspace/config

# Copy configuration files
COPY config/jupyter_config.py /workspace/config/jupyter_config.py
COPY config/project_config.yaml /workspace/config/project_config.yaml
COPY .env.example /workspace/.env.example

EXPOSE 8888

# ---------------------------------------------------------
# 🔹 Comando Padrão
# ---------------------------------------------------------
# Inicia o Jupyter Lab no ambiente 'bert' com configuração personalizada.
CMD ["bash", "-c", "conda run -n bert jupyter lab --config=/workspace/config/jupyter_config.py --notebook-dir=/workspace/notebooks"]