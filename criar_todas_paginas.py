#!/usr/bin/env python3
import os
import re

# Template HTML base
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Base A.I</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #2d3748;
            background: #ffffff;
        }}
        
        .container {{
            display: flex;
            min-height: 100vh;
        }}
        
        .sidebar {{
            width: 280px;
            background: #f7fafc;
            border-right: 1px solid #e2e8f0;
            padding: 2rem 0;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            transform: translateX(-100%);
            transition: transform 0.3s ease;
            z-index: 1000;
        }}
        
        .sidebar.active {{
            transform: translateX(0);
        }}
        
        @media (min-width: 769px) {{
            .sidebar {{
                transform: translateX(0);
                position: sticky;
                top: 0;
            }}
        }}
        
        .sidebar-header {{
            padding: 0 1.5rem 1rem;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 1rem;
        }}
        
        .sidebar-header h1 {{
            font-size: 1.5rem;
            color: #1a365d;
            margin-bottom: 0.5rem;
        }}
        
        .sidebar-header p {{
            font-size: 0.875rem;
            color: #718096;
        }}
        
        .nav-list {{
            list-style: none;
        }}
        
        .nav-item {{
            margin: 0;
        }}
        
        .nav-link {{
            display: flex;
            align-items: center;
            padding: 0.75rem 1.5rem;
            text-decoration: none;
            color: #2d3748;
            border-left: 3px solid transparent;
            transition: all 0.2s ease;
        }}
        
        .nav-link:hover {{
            background: #edf2f7;
            color: #3182ce;
        }}
        
        .nav-link.active {{
            background: #bee3f8;
            color: #3182ce;
            border-left-color: #3182ce;
            font-weight: 600;
        }}
        
        .nav-number {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 1.5rem;
            height: 1.5rem;
            margin-right: 0.75rem;
            font-size: 0.75rem;
            font-weight: 600;
            background: #e2e8f0;
            color: #718096;
            border-radius: 50%;
        }}
        
        .nav-link.active .nav-number {{
            background: #3182ce;
            color: white;
        }}
        
        .sidebar-footer {{
            margin-top: auto;
            padding: 1.5rem;
            border-top: 1px solid #e2e8f0;
            font-size: 0.75rem;
            color: #718096;
        }}
        
        .sidebar-footer a {{
            color: #3182ce;
            text-decoration: none;
        }}
        
        .main-content {{
            flex: 1;
            margin-left: 0;
            padding: 2rem;
        }}
        
        @media (min-width: 769px) {{
            .main-content {{
                margin-left: 280px;
                padding: 3rem 2rem;
            }}
        }}
        
        .content {{
            max-width: 800px;
            margin: 0 auto;
        }}
        
        .mobile-toggle {{
            display: block;
            position: fixed;
            top: 1rem;
            left: 1rem;
            z-index: 1001;
            background: #1a365d;
            color: white;
            border: none;
            padding: 0.5rem;
            border-radius: 0.375rem;
            cursor: pointer;
        }}
        
        @media (min-width: 769px) {{
            .mobile-toggle {{
                display: none;
            }}
        }}
        
        .overlay {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5);
            z-index: 999;
        }}
        
        .overlay.active {{
            display: block;
        }}
        
        h1, h2, h3 {{
            color: #1a365d;
            margin: 2rem 0 1rem;
        }}
        
        h1 {{
            font-size: 2.25rem;
            margin-bottom: 1.5rem;
        }}
        
        h2 {{
            font-size: 1.875rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e2e8f0;
        }}
        
        h3 {{
            font-size: 1.5rem;
        }}
        
        p {{
            margin: 1rem 0;
            line-height: 1.7;
        }}
        
        blockquote {{
            margin: 2rem 0;
            padding: 1.5rem;
            background: #f7fafc;
            border-left: 4px solid #3182ce;
            border-radius: 0 0.375rem 0.375rem 0;
            font-style: italic;
        }}
        
        ul, ol {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        
        li {{
            margin: 0.5rem 0;
        }}
        
        a {{
            color: #3182ce;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        strong {{
            font-weight: 600;
            color: #1a365d;
        }}
        
        .page-nav {{
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #e2e8f0;
            display: flex;
            justify-content: space-between;
            gap: 1rem;
        }}
        
        .nav-btn {{
            padding: 1rem 1.5rem;
            background: #f7fafc;
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            text-decoration: none;
            color: #2d3748;
            transition: all 0.2s ease;
            flex: 1;
            max-width: 45%;
        }}
        
        .nav-btn:hover {{
            background: #edf2f7;
            border-color: #3182ce;
            transform: translateY(-1px);
        }}
        
        .nav-btn-next {{
            text-align: right;
        }}
        
        .nav-direction {{
            font-size: 0.875rem;
            color: #718096;
            display: block;
            margin-bottom: 0.25rem;
        }}
        
        .nav-title {{
            font-weight: 600;
            color: #1a365d;
        }}
        
        @media (max-width: 768px) {{
            .page-nav {{
                flex-direction: column;
            }}
            .nav-btn {{
                max-width: 100%;
            }}
            .content {{
                margin-top: 3rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Mobile Toggle -->
        <button class="mobile-toggle" onclick="toggleSidebar()">☰</button>
        
        <!-- Overlay -->
        <div class="overlay" onclick="toggleSidebar()"></div>
        
        <!-- Sidebar -->
        <nav class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h1><a href="index.html" style="color: inherit; text-decoration: none;">Base A.I</a></h1>
                <p>Whitepaper</p>
            </div>
            
            <ul class="nav-list">
                <li class="nav-item">
                    <a href="index.html" class="nav-link {active_1}">
                        <span class="nav-number">1</span>
                        <span>Introdução</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="contexto-de-mercado.html" class="nav-link {active_2}">
                        <span class="nav-number">2</span>
                        <span>Contexto de Mercado</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="modelo-de-negocio.html" class="nav-link {active_3}">
                        <span class="nav-number">3</span>
                        <span>Modelo de Negócio</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="infraestrutura.html" class="nav-link {active_4}">
                        <span class="nav-number">4</span>
                        <span>Infraestrutura</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="estrutura-financeira.html" class="nav-link {active_5}">
                        <span class="nav-number">5</span>
                        <span>Estrutura Financeira</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="processo-de-investimento.html" class="nav-link {active_6}">
                        <span class="nav-number">6</span>
                        <span>Processo de Investimento</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="governanca.html" class="nav-link {active_7}">
                        <span class="nav-number">7</span>
                        <span>Governança</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="consideracoes.html" class="nav-link {active_8}">
                        <span class="nav-number">8</span>
                        <span>Considerações</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a href="anexos.html" class="nav-link {active_9}">
                        <span class="nav-number">9</span>
                        <span>Anexos</span>
                    </a>
                </li>
            </ul>
            
            <div class="sidebar-footer">
                <p><strong>Contato:</strong></p>
                <p><a href="mailto:contato@baseai.capital">contato@baseai.capital</a></p>
                <p><a href="https://baseai.capital" target="_blank">baseai.capital</a></p>
            </div>
        </nav>
        
        <!-- Main Content -->
        <main class="main-content">
            <div class="content">
                {content}
                
                <!-- Navigation -->
                <div class="page-nav">
                    {nav_buttons}
                </div>
            </div>
        </main>
    </div>

    <script>
        function toggleSidebar() {{
            const sidebar = document.getElementById('sidebar');
            const overlay = document.querySelector('.overlay');
            
            sidebar.classList.toggle('active');
            overlay.classList.toggle('active');
        }}

        // Close sidebar when clicking on nav links (mobile)
        document.querySelectorAll('.nav-link').forEach(link => {{
            link.addEventListener('click', () => {{
                if (window.innerWidth <= 768) {{
                    toggleSidebar();
                }}
            }});
        }});
    </script>
</body>
</html>'''

def markdown_to_html(text):
    """Converte markdown básico para HTML"""
    # Headers
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    
    # Blockquotes
    text = re.sub(r'^> (.+)$', r'<blockquote><p>\1</p></blockquote>', text, flags=re.MULTILINE)
    
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    
    # Links
    text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
    
    # Lists
    lines = text.split('\n')
    in_list = False
    result_lines = []
    
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            result_lines.append(f'<li>{line.strip()[2:]}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            if line.strip():
                result_lines.append(f'<p>{line}</p>')
            else:
                result_lines.append('')
    
    if in_list:
        result_lines.append('</ul>')
    
    return '\n'.join(result_lines)

# Configuração das páginas
pages = [
    {
        'file': 'index.md',
        'title': 'Introdução',
        'active': 1,
        'prev': None,
        'next': ('contexto-de-mercado.html', 'Contexto de Mercado')
    },
    {
        'file': 'contexto-de-mercado.md',
        'title': 'Contexto de Mercado',
        'active': 2,
        'prev': ('index.html', 'Introdução'),
        'next': ('modelo-de-negocio.html', 'Modelo de Negócio')
    },
    {
        'file': 'modelo-de-negocio.md',
        'title': 'Modelo de Negócio',
        'active': 3,
        'prev': ('contexto-de-mercado.html', 'Contexto de Mercado'),
        'next': ('infraestrutura.html', 'Infraestrutura')
    },
    {
        'file': 'infraestrutura.md',
        'title': 'Infraestrutura',
        'active': 4,
        'prev': ('modelo-de-negocio.html', 'Modelo de Negócio'),
        'next': ('estrutura-financeira.html', 'Estrutura Financeira')
    },
    {
        'file': 'estrutura-financeira.md',
        'title': 'Estrutura Financeira',
        'active': 5,
        'prev': ('infraestrutura.html', 'Infraestrutura'),
        'next': ('processo-de-investimento.html', 'Processo de Investimento')
    },
    {
        'file': 'processo-de-investimento.md',
        'title': 'Processo de Investimento',
        'active': 6,
        'prev': ('estrutura-financeira.html', 'Estrutura Financeira'),
        'next': ('governanca.html', 'Governança')
    },
    {
        'file': 'governanca.md',
        'title': 'Governança',
        'active': 7,
        'prev': ('processo-de-investimento.html', 'Processo de Investimento'),
        'next': ('consideracoes.html', 'Considerações')
    },
    {
        'file': 'consideracoes.md',
        'title': 'Considerações',
        'active': 8,
        'prev': ('governanca.html', 'Governança'),
        'next': ('anexos.html', 'Anexos')
    },
    {
        'file': 'anexos.md',
        'title': 'Anexos',
        'active': 9,
        'prev': ('consideracoes.html', 'Considerações'),
        'next': None
    }
]

# Gerar todas as páginas
for page in pages:
    # Ler arquivo markdown
    with open(page['file'], 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remover front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    
    # Converter para HTML
    html_content = markdown_to_html(content)
    
    # Configurar navegação ativa
    active_states = {f'active_{i}': '' for i in range(1, 10)}
    active_states[f'active_{page["active"]}'] = 'active'
    
    # Configurar botões de navegação
    nav_buttons = ''
    if page['prev']:
        nav_buttons += f'''
        <a href="{page['prev'][0]}" class="nav-btn">
            <span class="nav-direction">← Anterior</span>
            <span class="nav-title">{page['prev'][1]}</span>
        </a>'''
    else:
        nav_buttons += '<div></div>'
    
    if page['next']:
        nav_buttons += f'''
        <a href="{page['next'][0]}" class="nav-btn nav-btn-next">
            <span class="nav-direction">Próximo →</span>
            <span class="nav-title">{page['next'][1]}</span>
        </a>'''
    
    # Gerar HTML final
    html = HTML_TEMPLATE.format(
        title=page['title'],
        content=html_content,
        nav_buttons=nav_buttons,
        **active_states
    )
    
    # Salvar arquivo HTML
    output_file = page['file'].replace('.md', '.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Criado: {output_file}")

print("Todas as páginas HTML foram criadas com sucesso!")
