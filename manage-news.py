#!/usr/bin/env python3
"""
Script para gerenciar notícias do GT IoT EDU
Permite adicionar e editar notícias de forma interativa
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Configurações
NEWS_DIR = Path("news")
ARTICLES_DIR = NEWS_DIR / "articles"
INDEX_FILE = NEWS_DIR / "index.json"

# Opções disponíveis
COLOR_SCHEMES = ["blue", "green", "purple", "orange", "teal"]
TAG_COLORS = ["green", "purple", "blue", "teal", "slate"]
ICONS = [
    "book-open", "graduation-cap", "handshake", "flask-conical", "code-2",
    "award", "presentation", "rocket", "beaker", "git-branch", "newspaper",
    "users", "calendar", "trophy", "star", "zap", "lightbulb", "wifi"
]

def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Imprime um cabeçalho estilizado"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60 + "\n")

def get_input(prompt, default=None, options=None):
    """
    Solicita entrada do usuário com valor padrão opcional
    
    Args:
        prompt: Texto do prompt
        default: Valor padrão (opcional)
        options: Lista de opções válidas (opcional)
    """
    if default:
        prompt_text = f"{prompt} [{default}]: "
    else:
        prompt_text = f"{prompt}: "
    
    if options:
        print(f"\nOpções disponíveis: {', '.join(options)}")
    
    value = input(prompt_text).strip()
    
    if not value and default:
        return default
    
    if options and value and value not in options:
        print(f"⚠️  Opção inválida! Usando padrão: {default}")
        return default
    
    return value if value else None

def get_date_info():
    """Solicita e retorna informações de data"""
    print("\n📅 Informações de Data")
    print("-" * 40)
    
    # Sugerir data atual
    now = datetime.now()
    default_date = now.strftime("%Y-%m")
    default_display = now.strftime("%B %Y")
    
    # Mapeamento de meses em português
    months_pt = {
        "January": "Janeiro", "February": "Fevereiro", "March": "Março",
        "April": "Abril", "May": "Maio", "June": "Junho",
        "July": "Julho", "August": "Agosto", "September": "Setembro",
        "October": "Outubro", "November": "Novembro", "December": "Dezembro"
    }
    
    for en, pt in months_pt.items():
        default_display = default_display.replace(en, pt)
    
    date = get_input("Data (formato YYYY-MM)", default_date)
    
    # Gerar display sugerido
    try:
        year, month = date.split("-")
        month_num = int(month)
        month_names = list(months_pt.values())
        suggested_display = f"{month_names[month_num - 1]} {year}"
    except:
        suggested_display = default_display
    
    date_display = get_input("Data para exibição", suggested_display)
    
    return date, date_display

def get_tags():
    """Solicita e retorna lista de tags"""
    print("\n🏷️  Tags da Notícia")
    print("-" * 40)
    print("Digite as tags uma por vez. Deixe em branco para finalizar.")
    
    tags = []
    while True:
        print(f"\n📌 Tag #{len(tags) + 1}")
        label = get_input("  Label da tag (deixe vazio para finalizar)")
        
        if not label:
            break
        
        icon = get_input("  Ícone da tag", "award", ICONS)
        color = get_input("  Cor da tag", "green", TAG_COLORS)
        
        tags.append({
            "label": label,
            "icon": icon,
            "color": color
        })
        
        print(f"  ✅ Tag '{label}' adicionada!")
    
    # Se não houver tags, adicionar uma padrão
    if not tags:
        print("\n⚠️  Nenhuma tag adicionada. Adicionando tag padrão...")
        tags.append({
            "label": "Notícia",
            "icon": "newspaper",
            "color": "blue"
        })
    
    return tags

def create_article():
    """Cria uma nova notícia"""
    clear_screen()
    print_header("📰 Criar Nova Notícia")
    
    # ID e nome do arquivo
    print("\n📝 Identificação")
    print("-" * 40)
    article_id = get_input("ID da notícia (ex: 2025-01-workshop)")
    
    if not article_id:
        print("❌ ID é obrigatório!")
        return None
    
    filename = f"{article_id}.json"
    filepath = ARTICLES_DIR / filename
    
    # Verificar se já existe
    if filepath.exists():
        overwrite = get_input(f"⚠️  Arquivo {filename} já existe. Sobrescrever? (s/N)", "n")
        if overwrite.lower() != 's':
            print("❌ Operação cancelada!")
            return None
    
    # Data
    date, date_display = get_date_info()
    
    # Informações principais
    print("\n📋 Informações Principais")
    print("-" * 40)
    title = get_input("Título da notícia")
    description = get_input("Descrição completa")
    link = get_input("Link externo")
    
    if not all([title, description, link]):
        print("❌ Título, descrição e link são obrigatórios!")
        return None
    
    # Aparência
    print("\n🎨 Aparência")
    print("-" * 40)
    icon = get_input("Ícone principal", "book-open", ICONS)
    color_scheme = get_input("Esquema de cores", "blue", COLOR_SCHEMES)
    
    # Tags
    tags = get_tags()
    
    # Criar objeto da notícia
    article = {
        "id": article_id,
        "date": date,
        "dateDisplay": date_display,
        "title": title,
        "description": description,
        "link": link,
        "icon": icon,
        "colorScheme": color_scheme,
        "tags": tags
    }
    
    # Mostrar resumo
    clear_screen()
    print_header("📋 Resumo da Notícia")
    print(json.dumps(article, indent=2, ensure_ascii=False))
    
    confirm = get_input("\n✅ Confirmar criação? (S/n)", "s")
    if confirm.lower() != 's':
        print("❌ Operação cancelada!")
        return None
    
    return filename, article

def list_articles():
    """Lista todas as notícias disponíveis"""
    try:
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index = json.load(f)
        
        articles = index.get('articles', [])
        
        if not articles:
            print("📭 Nenhuma notícia encontrada.")
            return []
        
        print("\n📚 Notícias Disponíveis:")
        print("-" * 60)
        
        for i, filename in enumerate(articles, 1):
            filepath = ARTICLES_DIR / filename
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    article = json.load(f)
                print(f"{i}. {filename}")
                print(f"   📰 {article.get('title', 'Sem título')}")
                print(f"   📅 {article.get('dateDisplay', 'Sem data')}")
                print()
            except:
                print(f"{i}. {filename} (erro ao ler)")
                print()
        
        return articles
    except FileNotFoundError:
        print("📭 Arquivo de índice não encontrado.")
        return []

def edit_article():
    """Edita uma notícia existente"""
    clear_screen()
    print_header("✏️  Editar Notícia")
    
    articles = list_articles()
    
    if not articles:
        return None
    
    try:
        choice = int(get_input("\nNúmero da notícia para editar (0 para cancelar)", "0"))
        
        if choice == 0 or choice > len(articles):
            print("❌ Operação cancelada!")
            return None
        
        filename = articles[choice - 1]
        filepath = ARTICLES_DIR / filename
        
        # Carregar notícia existente
        with open(filepath, 'r', encoding='utf-8') as f:
            article = json.load(f)
        
        clear_screen()
        print_header(f"✏️  Editando: {filename}")
        
        print("💡 Pressione ENTER para manter o valor atual\n")
        
        # Editar campos
        article['id'] = get_input("ID", article.get('id'))
        
        date, date_display = get_date_info()
        article['date'] = date if date else article.get('date')
        article['dateDisplay'] = date_display if date_display else article.get('dateDisplay')
        
        article['title'] = get_input("Título", article.get('title'))
        article['description'] = get_input("Descrição", article.get('description'))
        article['link'] = get_input("Link", article.get('link'))
        article['icon'] = get_input("Ícone", article.get('icon', 'book-open'), ICONS)
        article['colorScheme'] = get_input("Esquema de cores", article.get('colorScheme', 'blue'), COLOR_SCHEMES)
        
        # Editar tags
        edit_tags = get_input("\nEditar tags? (s/N)", "n")
        if edit_tags.lower() == 's':
            article['tags'] = get_tags()
        
        # Mostrar resumo
        clear_screen()
        print_header("📋 Notícia Atualizada")
        print(json.dumps(article, indent=2, ensure_ascii=False))
        
        confirm = get_input("\n✅ Confirmar alterações? (S/n)", "s")
        if confirm.lower() != 's':
            print("❌ Operação cancelada!")
            return None
        
        return filename, article
        
    except (ValueError, IndexError):
        print("❌ Opção inválida!")
        return None

def save_article(filename, article):
    """Salva a notícia no arquivo"""
    try:
        # Criar diretórios se não existirem
        ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
        
        # Salvar arquivo
        filepath = ARTICLES_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(article, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Notícia salva em: {filepath}")
        
        # Atualizar índice
        update_index(filename)
        
        return True
    except Exception as e:
        print(f"\n❌ Erro ao salvar: {e}")
        return False

def update_index(filename):
    """Atualiza o arquivo de índice"""
    try:
        # Carregar índice existente ou criar novo
        if INDEX_FILE.exists():
            with open(INDEX_FILE, 'r', encoding='utf-8') as f:
                index = json.load(f)
        else:
            index = {"articles": []}
        
        # Adicionar filename se não existir
        if filename not in index['articles']:
            index['articles'].insert(0, filename)  # Adicionar no início
            print(f"✅ Notícia adicionada ao índice")
        else:
            print(f"ℹ️  Notícia já existe no índice")
        
        # Salvar índice
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Índice atualizado em: {INDEX_FILE}")
        
    except Exception as e:
        print(f"⚠️  Erro ao atualizar índice: {e}")

def delete_article():
    """Remove uma notícia"""
    clear_screen()
    print_header("🗑️  Remover Notícia")
    
    articles = list_articles()
    
    if not articles:
        return
    
    try:
        choice = int(get_input("\nNúmero da notícia para remover (0 para cancelar)", "0"))
        
        if choice == 0 or choice > len(articles):
            print("❌ Operação cancelada!")
            return
        
        filename = articles[choice - 1]
        filepath = ARTICLES_DIR / filename
        
        # Confirmar remoção
        confirm = get_input(f"\n⚠️  Confirmar remoção de '{filename}'? (s/N)", "n")
        if confirm.lower() != 's':
            print("❌ Operação cancelada!")
            return
        
        # Remover arquivo
        filepath.unlink()
        print(f"✅ Arquivo removido: {filepath}")
        
        # Remover do índice
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            index = json.load(f)
        
        index['articles'] = [a for a in index['articles'] if a != filename]
        
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Removido do índice")
        
    except (ValueError, IndexError):
        print("❌ Opção inválida!")
    except Exception as e:
        print(f"❌ Erro ao remover: {e}")

def main_menu():
    """Menu principal"""
    while True:
        clear_screen()
        print_header("🚀 GT IoT EDU - Gerenciador de Notícias")
        
        print("1. 📝 Criar nova notícia")
        print("2. ✏️  Editar notícia existente")
        print("3. 📚 Listar todas as notícias")
        print("4. 🗑️  Remover notícia")
        print("5. 🚪 Sair")
        
        choice = get_input("\nEscolha uma opção", "1")
        
        if choice == "1":
            result = create_article()
            if result:
                filename, article = result
                save_article(filename, article)
                input("\n✅ Pressione ENTER para continuar...")
        
        elif choice == "2":
            result = edit_article()
            if result:
                filename, article = result
                save_article(filename, article)
                input("\n✅ Pressione ENTER para continuar...")
        
        elif choice == "3":
            clear_screen()
            print_header("📚 Todas as Notícias")
            list_articles()
            input("\n📌 Pressione ENTER para continuar...")
        
        elif choice == "4":
            delete_article()
            input("\n📌 Pressione ENTER para continuar...")
        
        elif choice == "5":
            clear_screen()
            print("\n👋 Até logo!\n")
            break
        
        else:
            print("❌ Opção inválida!")
            input("\n📌 Pressione ENTER para continuar...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("\n\n👋 Programa interrompido pelo usuário. Até logo!\n")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        input("\nPressione ENTER para sair...")