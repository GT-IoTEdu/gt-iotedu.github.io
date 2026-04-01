# static

Este repositório usa includes do Jekyll (GitHub Pages) para manter a landing page organizada.

- Página principal: [index.html](index.html)
- Parciais: [_includes/index/](./_includes/index/)


docker run --rm -it \
  -p 4000:4000 \
  -v "$PWD":/srv/jekyll \
  jekyll/builder:4 \
  bash -lc "bundle install && bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --trace"

pra rodar

## Preview local (Jekyll)

Abrir o [index.html](index.html) direto no navegador **não** processa os `{% include %}`. Para ver a página montada igual ao deploy do GitHub Pages, rode um servidor Jekyll local.

### Opção A (recomendado): Docker

1) Suba o servidor:

```bash
docker run --rm -it \
	-p 4000:4000 \
	-v "$PWD":/srv/jekyll \
	-u "$(id -u):$(id -g)" \
	jekyll/jekyll:4 \
	jekyll serve --host 0.0.0.0 --port 4000 --livereload
```

2) Abra no navegador:

http://localhost:4000

> Se você não tiver Docker instalado, use a opção B.

### Opção B: Ruby + Jekyll (instalação local)

1) Instale Ruby e ferramentas básicas (Debian/Ubuntu):

```bash
sudo apt-get update
sudo apt-get install -y ruby-full build-essential zlib1g-dev
```

2) Instale Jekyll e Bundler:

```bash
gem install jekyll bundler
```

3) Rode o servidor:

```bash
jekyll serve --livereload
```

4) Abra no navegador:

http://localhost:4000

> Observação: em alguns ambientes Ruby/Jekyll pode ser necessário instalar `webrick` (ex.: `gem install webrick`).