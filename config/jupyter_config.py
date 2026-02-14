# Jupyter Lab Configuration for BERT ML Laboratory
# This configuration sets up Jupyter Lab for scientific experiments

import os
from jupyter_server.auth import passwd

# Get hashed password from environment variable
# The hash is already generated for password 'minhasenha'
hashed_password = os.getenv('JUPYTER_TOKEN', 'sha1:VLWq5gkwf1an:4f3377bb5da7e3a3b9f688139c1ffb04d51949eb')

# Server configuration
c.ServerApp.ip = os.getenv('JUPYTER_IP', '0.0.0.0')
c.ServerApp.port = int(os.getenv('JUPYTER_PORT', 8888))
c.ServerApp.open_browser = False
c.ServerApp.password = hashed_password
c.ServerApp.password_required = True
c.ServerApp.allow_password_change = False
c.ServerApp.allow_root = True
c.ServerApp.allow_remote_access = True

# Notebook configuration
c.ContentsManager.allow_hidden = False
c.FileContentsManager.delete_to_trash = True
c.FileContentsManager.always_delete_dir = False

# Kernel configuration
c.MultiKernelManager.default_kernel_name = 'python3'
c.KernelManager.autorestart = True
c.KernelManager.shutdown_wait_time = 5.0

# Terminal configuration
c.ServerApp.terminals_enabled = True

# Extensions configuration
c.ServerApp.jpserver_extensions = {
    'jupyterlab': True,
    'jupyter_server_terminals': True,
}

# Security configuration
c.ServerApp.disable_check_xsrf = False
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_credentials = True
c.ServerApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors 'self' *"
    }
}

# Logging configuration
c.ServerApp.log_level = 'INFO'
c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'
c.Application.log_format = '[%(name)s] %(message)s'

# File handling
c.ContentsManager.checkpoints_kwargs = {'root_dir': '.ipynb_checkpoints'}
c.FileCheckpoints.root_dir = '.ipynb_checkpoints'

# Notebook directory
notebook_dir = os.getenv('JUPYTER_NOTEBOOK_DIR', '/workspace/notebooks')
c.ServerApp.root_dir = notebook_dir
c.ServerApp.preferred_dir = notebook_dir

# Custom CSS for scientific work
c.ServerApp.jupyterlab_settings = {
    '@jupyterlab/apputils-extension:themes': {
        'theme': 'JupyterLab Dark'
    },
    '@jupyterlab/notebook-extension:tracker': {
        'codeCellConfig': {
            'lineNumbers': True,
            'autoClosingBrackets': True,
            'fontFamily': 'Monaco, "Courier New", monospace',
            'fontSize': 13,
            'lineHeight': 1.4,
            'wordWrapColumn': 80
        }
    }
}

# Extension recommendations for scientific work
c.ServerApp.default_url = '/lab'
c.LabApp.collaborative = False
c.LabApp.expose_app_in_browser = True

print(f"Jupyter Lab configured with hashed password")
print(f"Server will run on: {c.ServerApp.ip}:{c.ServerApp.port}")
print(f"Notebook directory: {notebook_dir}")
print(f"Password: 'minhasenha' (use this to login)")