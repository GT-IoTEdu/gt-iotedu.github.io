# Como Adicionar uma Nova Notícia

## Passo 1: Criar o Arquivo JSON

Crie um novo arquivo na pasta `news/articles/` com o formato: `YYYY-MM-titulo-curto.json`

Exemplo: `2025-02-workshop-iot.json`

## Passo 2: Preencher os Dados

Use este template:

```json
{
  "id": "2025-02-workshop-iot",
  "date": "2025-02",
  "dateDisplay": "Fevereiro 2025",
  "title": "Título da Notícia",
  "description": "Descrição completa da notícia...",
  "link": "https://link-externo.com",
  "icon": "nome-do-icone",
  "colorScheme": "blue",
  "tags": [
    {
      "label": "Tipo",
      "icon": "nome-icone",
      "color": "green"
    }
  ]
}
```

## Passo 3: Adicionar ao Índice

Edite o arquivo `news/index.json` e adicione o nome do seu arquivo no início da lista:

```json
{
  "articles": [
    "2025-02-workshop-iot.json",
    "2025-01-sbrc.json",
    ...
  ]
}
```

## Opções de Configuração

### Color Schemes Disponíveis
- `blue` - Azul (padrão)
- `green` - Verde
- `purple` - Roxo
- `orange` - Laranja
- `teal` - Azul-petróleo

### Ícones Disponíveis (Lucide)
- `book-open` - Livro aberto
- `graduation-cap` - Chapéu de formatura
- `handshake` - Aperto de mãos
- `flask-conical` - Frasco de laboratório
- `code-2` - Código
- `award` - Prêmio
- `presentation` - Apresentação
- `rocket` - Foguete
- `beaker` - Béquer
- `git-branch` - Branch Git

Veja todos os ícones em: https://lucide.dev/icons/

### Cores de Tags
- `green` - Verde
- `purple` - Roxo
- `blue` - Azul
- `teal` - Azul-petróleo
- `slate` - Cinza
## Traduções (EN e ES)

O site tem versões em inglês (`/en/`) e espanhol (`/es/`), que leem os mesmos arquivos JSON. A tradução de cada notícia fica no campo opcional `i18n`; qualquer campo ausente usa o texto em português.

```json
{
  "id": "2025-02-workshop-iot",
  "title": "Workshop de IoT na Unipampa",
  "...": "...",
  "i18n": {
    "en": {
      "title": "IoT Workshop at Unipampa",
      "dateDisplay": "February 2025",
      "tags": ["News"],
      "description": "<p>Texto traduzido...</p><p><img src=\"@img0\"></p>"
    },
    "es": {
      "title": "Taller de IoT en la Unipampa",
      "dateDisplay": "Febrero 2025",
      "tags": ["Noticia"],
      "description": "<p>Texto traducido...</p><p><img src=\"@img0\"></p>"
    }
  }
}
```

- `tags`: só os rótulos, na mesma ordem das tags em português (ícone e cor vêm do original).
- Imagens: para não repetir imagens embutidas (base64) em cada idioma, a tradução usa `src="@img0"`, `src="@img1"`..., que a página troca pela 1ª, 2ª... imagem da descrição em português.
- O `admin.html` tem a seção **Traduções**, que preenche esse campo automaticamente (inclusive a troca das imagens por `@imgN`).
