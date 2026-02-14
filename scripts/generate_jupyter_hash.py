#!/usr/bin/env python3
"""
Script para gerar hash de senha do Jupyter
"""

import hashlib
import random
import string

def generate_jupyter_hash(password):
    """Gera hash no formato do Jupyter"""
    salt_len = 12
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=salt_len))
    h = hashlib.sha1(password.encode('utf-8') + salt.encode('ascii'))
    return 'sha1:' + salt + ':' + h.hexdigest()

if __name__ == "__main__":
    password = "minhasenha"
    hashed_password = generate_jupyter_hash(password)
    print(f"Senha: {password}")
    print(f"Hash Jupyter: {hashed_password}")
    
    # Também mostra como usar no .env
    print(f"\nPara usar no .env:")
    print(f"JUPYTER_TOKEN={hashed_password}")