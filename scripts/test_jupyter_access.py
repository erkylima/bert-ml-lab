#!/usr/bin/env python3
"""
Script para testar acesso ao Jupyter Lab
"""

import requests
import time
import sys

def test_jupyter_access():
    """Testa se o Jupyter Lab está acessível"""
    url = "http://localhost:8888"
    
    print("Testando acesso ao Jupyter Lab...")
    print(f"URL: {url}")
    print(f"Senha configurada: 'minhasenha'")
    print(f"Hash no .env: sha1:VLWq5gkwf1an:4f3377bb5da7e3a3b9f688139c1ffb04d51949eb")
    
    try:
        # Testar conexão básica
        response = requests.get(url, timeout=10)
        print(f"\nStatus HTTP: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Jupyter está respondendo (página carregada)")
            return True
        elif response.status_code == 302:
            print("✅ Jupyter está redirecionando para login (esperado)")
            print("   Isso indica que a autenticação está habilitada")
            return True
        else:
            print(f"⚠️  Status inesperado: {response.status_code}")
            return False
            
    except requests.ConnectionError:
        print("❌ Não foi possível conectar ao Jupyter")
        print("   Verifique se o container está rodando: docker compose ps")
        return False
    except Exception as e:
        print(f"❌ Erro ao testar acesso: {str(e)}")
        return False

def check_container_status():
    """Verifica status do container Docker"""
    import subprocess
    
    print("\n" + "="*50)
    print("Verificando status do container...")
    
    try:
        # Verificar se container está rodando
        result = subprocess.run(
            ["docker", "compose", "ps"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if "bert-ml-lab" in result.stdout and "Up" in result.stdout:
            print("✅ Container está rodando")
            
            # Verificar logs recentes
            logs = subprocess.run(
                ["docker", "compose", "logs", "--tail=10", "bert-lab"],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if "Jupyter" in logs.stdout or "8888" in logs.stdout:
                print("✅ Jupyter detectado nos logs")
            else:
                print("⚠️  Jupyter não detectado nos logs recentes")
                
            return True
        else:
            print("❌ Container não está rodando")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao verificar container: {str(e)}")
        return False

def main():
    """Função principal"""
    print("="*50)
    print("BERT ML Laboratory - Teste de Acesso")
    print("="*50)
    
    # Verificar container
    container_ok = check_container_status()
    
    if not container_ok:
        print("\n❌ Container não está funcionando corretamente")
        print("   Execute: docker compose up -d")
        sys.exit(1)
    
    # Testar acesso
    print("\n" + "="*50)
    print("Testando acesso ao Jupyter Lab...")
    
    # Dar tempo para o Jupyter iniciar completamente
    time.sleep(2)
    
    access_ok = test_jupyter_access()
    
    if access_ok:
        print("\n" + "="*50)
        print("✅ TESTE CONCLUÍDO COM SUCESSO!")
        print("="*50)
        print("\nInstruções de acesso:")
        print("1. Abra o navegador em: http://localhost:8888")
        print("2. Use a senha: minhasenha")
        print("3. Os notebooks estão em: /workspace/notebooks")
        print("\nPara parar o laboratório: docker compose down")
        sys.exit(0)
    else:
        print("\n" + "="*50)
        print("❌ TESTE FALHOU")
        print("="*50)
        print("\nSolução de problemas:")
        print("1. Verifique logs: docker compose logs -f")
        print("2. Reinicie: docker compose restart")
        print("3. Reconstrua: docker compose up --build -d")
        sys.exit(1)

if __name__ == "__main__":
    main()