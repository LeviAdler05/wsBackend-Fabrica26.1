# 🧪 Rickpedia - Rick and Morty Manager API

[![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-A30000?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)

O **Rickpedia** é uma plataforma backend robusta construída com Django e Django REST Framework (DRF) que consome a API oficial de **Rick and Morty**. O projeto permite que usuários gerenciem seus personagens favoritos, criem listas personalizadas e explorem o multiverso da série.

---

## 🚀 Tecnologias e Arquitetura

- **Python 3.11+** e **Django 6.0**
- **Django REST Framework (DRF):** Para construção da API.
- **PostgreSQL:** Banco de dados relacional robusto.
- **Docker & Docker Compose:** Containerização completa da aplicação e banco.
- **Swagger (drf-yasg):** Documentação interativa da API.
- **Integração Externa:** Consumo da [Rick and Morty API](https://rickandmortyapi.com/).
- **Arquitetura Clean:** Lógica de negócio isolada em `services.py` para consumo de APIs externas.

---

## ⚙️ Funcionalidades principais

- **Autenticação:** Sistema de Login com geração de **Token DRF**.
- **Gestão de Personagens:** Busca automática na API externa e cache no banco de dados local.
- **Favoritos:** Usuários podem marcar personagens como favoritos.
- **Listas Customizadas (CRUD):** Criação, edição e exclusão de listas de personagens (Ex: "Vilões que eu gosto", "Versões do Rick").
- **Interface Visual:** Home page amigável desenvolvida com Django Templates e CSS personalizado.
- **Documentação:** Endpoints documentados via Swagger e Redoc.

---

## 🐳 Como Rodar o Projeto (Recomendado: Docker)

A maneira mais rápida de subir o projeto é utilizando o Docker Compose, que já configura o banco de dados PostgreSQL automaticamente.

### 1. Clone o Repositório
```bash
git clone https://github.com/LeviAdler05/wsBackend-Fabrica26.1
cd wsBackend-Fabrica26.1
```

### 2. Configure as Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto (se não existir) com base no exemplo abaixo:
```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=*
DB_NAME=rickpedia
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
```

### 3. Suba os Containers
```bash
docker-compose up --build
```
*A API estará disponível em `http://localhost:8000`.*

### 4. Execute as Migrações e Crie o Admin
Em um novo terminal, rode:
```bash
# Criar tabelas no banco
docker-compose exec web python manage.py migrate

# Criar usuário administrador
docker-compose exec web python manage.py createsuperuser
```

---

## 🛠️ Desenvolvimento Local (Sem Docker)

Caso prefira rodar sem Docker, você precisará de um banco PostgreSQL instalado localmente.

1.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Linux/Mac
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute as migrações:**
    ```bash
    python src/manage.py migrate
    ```
4.  **Inicie o servidor:**
    ```bash
    python src/manage.py runserver
    ```

---

## 📂 Estrutura de Pastas

```text
src/
├── apps/
│   ├── accounts/     # Autenticação e Usuários
│   ├── characters/   # Integração com API e Model de Personagens
│   └── lists/        # CRUD de Listas e Favoritos
├── rickpedia/        # Configurações do Projeto (Settings/URLs)
├── templates/        # Páginas HTML (Django Templates)
└── manage.py
```

---

## 📖 Acesso e Documentação

- **Página Inicial:** `http://localhost:8000/` (Interface amigável).
- **Swagger UI:** `http://localhost:8000/swagger/` (Melhor lugar para testar a API).
- **Admin Django:** `http://localhost:8000/admin/` (Gestão de dados).

---

## 📝 Autor

Desenvolvido por **Levi Adler** - [GitHub](https://github.com/LeviAdler05)
