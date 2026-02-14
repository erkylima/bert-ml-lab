#!/usr/bin/env python3
"""
BERT ML Laboratory - Setup Verification Script
Verifies that the laboratory is properly configured for scientific experiments.
"""

import os
import sys
import subprocess
import json
import yaml
from pathlib import Path

class SetupVerifier:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        self.errors = []
        self.warnings = []
        self.successes = []
        
    def print_header(self, text):
        print(f"\n{'='*60}")
        print(f" {text}")
        print(f"{'='*60}")
    
    def print_success(self, text):
        print(f"✅ {text}")
        self.successes.append(text)
    
    def print_warning(self, text):
        print(f"⚠️  {text}")
        self.warnings.append(text)
    
    def print_error(self, text):
        print(f"❌ {text}")
        self.errors.append(text)
    
    def check_directory_structure(self):
        """Verify project directory structure"""
        self.print_header("Checking Directory Structure")
        
        required_dirs = [
            'data/raw',
            'data/processed', 
            'data/external',
            'models/checkpoints',
            'models/published',
            'results/metrics',
            'results/visualizations',
            'results/logs',
            'docs/methodology',
            'docs/results',
            'docs/references',
            'scripts',
            'config',
            'notebooks'
        ]
        
        for dir_path in required_dirs:
            full_path = self.project_root / dir_path
            if full_path.exists():
                self.print_success(f"Directory exists: {dir_path}")
            else:
                self.print_error(f"Missing directory: {dir_path}")
    
    def check_required_files(self):
        """Verify required configuration files"""
        self.print_header("Checking Required Files")
        
        required_files = [
            'README.md',
            'QUICKSTART.md',
            'LICENSE',
            'CITATION.cff',
            '.env.example',
            'docker-compose.yml',
            'Dockerfile',
            'config/project_config.yaml',
            'config/jupyter_config.py',
            'scripts/setup_project.sh'
        ]
        
        for file_path in required_files:
            full_path = self.project_root / file_path
            if full_path.exists():
                self.print_success(f"File exists: {file_path}")
            else:
                self.print_error(f"Missing file: {file_path}")
    
    def check_docker_configuration(self):
        """Verify Docker configuration"""
        self.print_header("Checking Docker Configuration")
        
        # Check docker-compose.yml
        compose_path = self.project_root / 'docker-compose.yml'
        if compose_path.exists():
            with open(compose_path) as f:
                content = f.read()
                
            # Check for environment variables
            if '${JUPYTER_TOKEN}' in content:
                self.print_success("Docker Compose uses environment variables")
            else:
                self.print_warning("Docker Compose may have hardcoded values")
            
            # Check for GPU configuration
            if 'nvidia' in content.lower():
                self.print_success("GPU configuration detected")
            else:
                self.print_warning("No GPU configuration found")
        else:
            self.print_error("docker-compose.yml not found")
    
    def check_environment_configuration(self):
        """Verify environment configuration"""
        self.print_header("Checking Environment Configuration")
        
        env_example = self.project_root / '.env.example'
        if env_example.exists():
            with open(env_example) as f:
                content = f.read()
            
            # Check for required variables
            required_vars = ['JUPYTER_TOKEN', 'HF_TOKEN', 'BERTIMBAU_MODEL']
            for var in required_vars:
                if f'{var}=' in content:
                    self.print_success(f"Environment variable defined: {var}")
                else:
                    self.print_warning(f"Missing environment variable: {var}")
            
            # Check for default password
            if 'minha senha' in content:
                self.print_success("Default Jupyter password is set")
            else:
                self.print_warning("Default Jupyter password not found")
        else:
            self.print_error(".env.example not found")
    
    def check_jupyter_configuration(self):
        """Verify Jupyter configuration"""
        self.print_header("Checking Jupyter Configuration")
        
        jupyter_config = self.project_root / 'config' / 'jupyter_config.py'
        if jupyter_config.exists():
            with open(jupyter_config) as f:
                content = f.read()
            
            # Check for password configuration
            if 'minha senha' in content:
                self.print_success("Jupyter password configured")
            else:
                self.print_warning("Jupyter password not configured")
            
            # Check for security settings
            if 'password_required = True' in content:
                self.print_success("Password authentication enabled")
            else:
                self.print_warning("Password authentication may be disabled")
        else:
            self.print_error("Jupyter configuration not found")
    
    def check_notebooks(self):
        """Verify notebook structure"""
        self.print_header("Checking Notebooks")
        
        notebooks_dir = self.project_root / 'notebooks'
        if notebooks_dir.exists():
            # Count notebooks
            notebook_files = list(notebooks_dir.rglob('*.ipynb'))
            self.print_success(f"Found {len(notebook_files)} notebook files")
            
            # Check for experiment categories
            categories = ['livro', 'sentimentos', 'neuralRag', 'imagens']
            for category in categories:
                category_dir = notebooks_dir / category
                if category_dir.exists():
                    category_notebooks = list(category_dir.rglob('*.ipynb'))
                    self.print_success(f"Category '{category}': {len(category_notebooks)} notebooks")
                else:
                    self.print_warning(f"Missing notebook category: {category}")
        else:
            self.print_error("Notebooks directory not found")
    
    def check_documentation(self):
        """Verify documentation completeness"""
        self.print_header("Checking Documentation")
        
        docs_files = [
            'docs/experiment_catalog.md',
            'docs/publication_guide.md',
            'docs/methodology/experiment_overview.md'
        ]
        
        for doc_file in docs_files:
            full_path = self.project_root / doc_file
            if full_path.exists():
                file_size = full_path.stat().st_size
                if file_size > 1000:  # More than 1KB
                    self.print_success(f"Documentation complete: {doc_file}")
                else:
                    self.print_warning(f"Documentation may be minimal: {doc_file}")
            else:
                self.print_error(f"Missing documentation: {doc_file}")
    
    def check_reproducibility(self):
        """Verify reproducibility measures"""
        self.print_header("Checking Reproducibility Measures")
        
        # Check for seed configuration
        env_example = self.project_root / '.env.example'
        if env_example.exists():
            with open(env_example) as f:
                content = f.read()
            
            if 'SEED=' in content:
                self.print_success("Random seed configuration found")
            else:
                self.print_warning("Random seed not configured")
        
        # Check for version pinning
        dockerfile = self.project_root / 'Dockerfile'
        if dockerfile.exists():
            with open(dockerfile) as f:
                content = f.read()
            
            if 'python=3.12' in content and 'torch==2.9.1' in content:
                self.print_success("Dependency versions are pinned")
            else:
                self.print_warning("Dependency versions may not be pinned")
    
    def run_system_checks(self):
        """Run system-level checks"""
        self.print_header("Running System Checks")
        
        # Check Docker availability
        try:
            result = subprocess.run(['docker', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                self.print_success(f"Docker available: {result.stdout.strip()}")
            else:
                self.print_error("Docker not available")
        except FileNotFoundError:
            self.print_error("Docker command not found")
        
        # Check Docker Compose
        try:
            result = subprocess.run(['docker-compose', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                self.print_success(f"Docker Compose available: {result.stdout.strip()}")
            else:
                self.print_warning("Docker Compose not available")
        except FileNotFoundError:
            # Try docker compose (v2)
            try:
                result = subprocess.run(['docker', 'compose', 'version'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    self.print_success(f"Docker Compose V2 available: {result.stdout.strip()}")
                else:
                    self.print_warning("Docker Compose not available")
            except FileNotFoundError:
                self.print_error("Docker Compose not found")
    
    def generate_summary(self):
        """Generate verification summary"""
        self.print_header("Verification Summary")
        
        print(f"\n📊 Summary:")
        print(f"  Successes: {len(self.successes)}")
        print(f"  Warnings:  {len(self.warnings)}")
        print(f"  Errors:    {len(self.errors)}")
        
        if self.errors:
            print(f"\n❌ Critical Errors (must fix):")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print(f"\n⚠️  Warnings (recommended to fix):")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            print(f"\n🎉 All checks passed! The laboratory is ready for scientific experiments.")
        elif not self.errors:
            print(f"\n⚠️  Some warnings found, but the laboratory is functional.")
        else:
            print(f"\n❌ Critical errors found. Please fix them before proceeding.")
        
        return len(self.errors) == 0
    
    def run_all_checks(self):
        """Run all verification checks"""
        print("BERT ML Laboratory - Setup Verification")
        print("="*60)
        
        checks = [
            self.check_directory_structure,
            self.check_required_files,
            self.check_docker_configuration,
            self.check_environment_configuration,
            self.check_jupyter_configuration,
            self.check_notebooks,
            self.check_documentation,
            self.check_reproducibility,
            self.run_system_checks
        ]
        
        for check in checks:
            try:
                check()
            except Exception as e:
                self.print_error(f"Check failed with error: {str(e)}")
        
        return self.generate_summary()

def main():
    """Main entry point"""
    verifier = SetupVerifier()
    success = verifier.run_all_checks()
    
    if success:
        print("\n✅ Setup verification completed successfully!")
        print("   You can now run: ./scripts/setup_project.sh")
        return 0
    else:
        print("\n❌ Setup verification failed!")
        print("   Please fix the errors above before proceeding.")
        return 1

if __name__ == "__main__":
    sys.exit(main())