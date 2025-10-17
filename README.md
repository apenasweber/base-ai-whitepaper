# Base A.I - Whitepaper

Whitepaper oficial da Base A.I - Transformando infraestrutura de IA em classe de ativo real.

## 🚀 Acesso Rápido

**Site do Whitepaper**: [https://username.github.io/whitepaper](https://username.github.io/whitepaper)

## 📖 Conteúdo

Este whitepaper apresenta o modelo de negócio, estratégia e oportunidades de investimento da Base A.I:

1. **[Resumo Executivo](index.md)** - Visão geral da proposta de valor
2. **[Contexto de Mercado](contexto-de-mercado.md)** - Análise do setor de IA e infraestrutura
3. **[Modelo de Negócio](modelo-de-negocio.md)** - Como geramos valor para investidores
4. **[Infraestrutura e Tecnologia](infraestrutura.md)** - Stack tecnológico e parcerias
5. **[Governança e Transparência](governanca.md)** - Práticas de governança corporativa
6. **[Estrutura Financeira](estrutura-financeira.md)** - Modelo revenue share e projeções
7. **[Considerações Importantes](consideracoes.md)** - Riscos e limitações
8. **[Processo de Investimento](processo-de-investimento.md)** - Como participar
9. **[Anexos](anexos.md)** - Fontes, glossário e disclaimers

## 🛠️ Setup do GitHub Pages

### Pré-requisitos

- Conta no GitHub
- Repositório público ou GitHub Pro para repositórios privados

### Passos para Publicação

1. **Criar Repositório no GitHub**
   ```bash
   # No seu terminal local
   git remote add origin https://github.com/SEU_USUARIO/whitepaper.git
   git branch -M main
   git push -u origin main
   ```

2. **Configurar GitHub Pages**
   - Acesse seu repositório no GitHub
   - Vá em `Settings` > `Pages`
   - Em `Source`, selecione `Deploy from a branch`
   - Escolha `main` branch e `/ (root)`
   - Clique em `Save`

3. **Personalizar Configuração**
   - Edite o arquivo `_config.yml`
   - Altere a linha `url: "https://username.github.io"` 
   - Substitua `username` pelo seu usuário do GitHub
   - Commit e push das alterações

### Estrutura de Arquivos

```
whitepaper/
├── _config.yml              # Configuração do Jekyll/GitHub Pages
├── index.md                 # Página inicial (Resumo Executivo)
├── contexto-de-mercado.md   # Análise de mercado
├── modelo-de-negocio.md     # Modelo de negócio
├── infraestrutura.md        # Tecnologia e infraestrutura
├── governanca.md            # Governança e transparência
├── estrutura-financeira.md  # Estrutura financeira
├── consideracoes.md         # Riscos e considerações
├── processo-de-investimento.md # Processo de investimento
├── anexos.md               # Anexos e referências
└── README.md               # Este arquivo
```

## 🎨 Personalização

### Tema

O site usa o tema `minima` do Jekyll. Para personalizar:

1. **Cores e Estilos**: Crie um arquivo `assets/css/style.scss`
2. **Layout**: Sobrescreva templates na pasta `_layouts/`
3. **Componentes**: Adicione includes na pasta `_includes/`

### Navegação

A navegação lateral é configurada automaticamente através do `_config.yml`. Para modificar:

1. Edite a seção `sidebar` no `_config.yml`
2. Adicione ou remova páginas conforme necessário
3. Mantenha a ordem lógica do conteúdo

## 📱 Responsividade

O tema minima é totalmente responsivo e funciona bem em:
- Desktop (1200px+)
- Tablet (768px - 1199px)  
- Mobile (< 768px)

## 🔧 Desenvolvimento Local

Para testar localmente antes de publicar:

```bash
# Instalar Jekyll (requer Ruby)
gem install bundler jekyll

# Criar Gemfile
echo 'source "https://rubygems.org"' > Gemfile
echo 'gem "github-pages", group: :jekyll_plugins' >> Gemfile

# Instalar dependências
bundle install

# Executar servidor local
bundle exec jekyll serve

# Acesse http://localhost:4000
```

## 📊 Analytics (Opcional)

Para adicionar Google Analytics:

1. Obtenha seu tracking ID no Google Analytics
2. Edite `_config.yml` e descomente a linha:
   ```yaml
   google_analytics: UA-XXXXXXXX-X
   ```
3. Substitua pelo seu ID real

## 🔒 SEO

O site já inclui otimizações básicas de SEO:
- Meta tags automáticas
- Sitemap.xml gerado automaticamente
- Estrutura semântica HTML5
- Open Graph tags

## 📞 Suporte

Para dúvidas sobre o whitepaper ou processo de investimento:

- **Email**: info@baseai.com.br
- **Site**: [baseai.com.br](https://baseai.com.br)
- **Telefone**: +55 11 3000-0000

## ⚖️ Disclaimer

Este material é meramente informativo e não constitui oferta pública de valores mobiliários. A participação em captações privadas é restrita a investidores qualificados e está sujeita à análise individual.

---

**Base A.I** - Democratizando o acesso à economia de infraestrutura de IA
