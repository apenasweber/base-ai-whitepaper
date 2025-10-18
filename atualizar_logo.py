#!/usr/bin/env python3
import os
import re

# Lista de arquivos HTML para atualizar (exceto index.html que já foi corrigido)
html_files = [
    'contexto-de-mercado.html',
    'modelo-de-negocio.html', 
    'infraestrutura.html',
    'estrutura-financeira.html',
    'processo-de-investimento.html',
    'governanca.html',
    'consideracoes.html',
    'anexos.html'
]

# Adicionar CSS para o logo
logo_css = '''        .sidebar-header {
            padding: 0 1.5rem 1rem;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        .logo {
            width: 120px;
            height: auto;
            margin-bottom: 0.5rem;
        }'''

# HTML do logo para substituir o h1
logo_html = '''            <div class="sidebar-header">
                <img src="logo.png" alt="Base A.I Logo" class="logo">
                <p>Whitepaper</p>
            </div>'''

for filename in html_files:
    if os.path.exists(filename):
        print(f"Atualizando {filename}...")
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Atualizar CSS do sidebar-header
        content = re.sub(
            r'        \.sidebar-header \{[^}]+\}',
            logo_css,
            content,
            flags=re.DOTALL
        )
        
        # Adicionar CSS do logo após sidebar-header
        if '.logo {' not in content:
            content = content.replace(
                logo_css,
                logo_css + '''
        
        .sidebar-header h1 {
            font-size: 1.5rem;
            color: #1a365d;
            margin-bottom: 0.5rem;
        }'''
            )
        
        # Substituir o header HTML
        content = re.sub(
            r'            <div class="sidebar-header">.*?</div>',
            logo_html,
            content,
            flags=re.DOTALL
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ {filename} atualizado")

print("Todos os arquivos foram atualizados com o logo!")
